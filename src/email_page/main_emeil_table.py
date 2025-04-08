from PySide6.QtWidgets import QTableWidgetItem,QAbstractItemView,QCheckBox,QPushButton,QHeaderView,QApplication,QLabel,QWidget,QHBoxLayout
from PySide6.QtCore import Qt,Signal
import src.db_function.db_email_function as db_email
import math
import sqlite3
import logging
import json
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

def create_tag_widget(tag_names, color_manager,user_id,self):
    container = QWidget()
    layout = QHBoxLayout()
    layout.setContentsMargins(2, 2, 2, 2)
    layout.setSpacing(4)

    for tag in tag_names:
        color = color_manager[tag]
        btn = ClickableLabel(tag)
        btn.setStyleSheet(f"""
            background-color: {color};
            color: white;
            border-radius: 6px;
            padding: 2px 6px;
            font-size: 11px;
            border: none;
        """)
        btn.clicked.connect(lambda uid=user_id: self.open_tag_selector(uid))
        layout.addWidget(btn)

    container.setLayout(layout)

    
    return container

def create_main_email_tale(self,data):
        for row_idx, row_data in enumerate(data):
            user_id = row_data[0]
            #dodanie ukrytej kolumn col = 0 przechowującej id(emaila)
            item_id = QTableWidgetItem(str(user_id))
            self.ui.tableWidget.setItem(row_idx, 0, item_id)
            self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            
            for col_idx, cell_data in enumerate(row_data[1:]):
                #przesunięcie o 1 bo kolumne 0 zejmuje ukryta kolumna zawierająca id
                real_col_idx = col_idx + 1 
                if real_col_idx == 4:
                    if isinstance(cell_data, bytes): 
                        cell_data = cell_data.decode("utf-8") 
                    elif cell_data is None:  
                        cell_data = ""
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                if real_col_idx == 5:
                    checkbox = QCheckBox()
                    checkbox.setChecked(bool(cell_data))
                    checkbox.setFocusPolicy(Qt.NoFocus)
                    checkbox.stateChanged.connect(
                        lambda state, uid=user_id: db_email.update_flag(self.db_connection,uid, state)
                    )
                    self.ui.tableWidget.setCellWidget(row_idx, real_col_idx, checkbox)
                elif real_col_idx == 8:
                    
                    if cell_data is not None:
                        tag_widget = create_tag_widget(cell_data.split(','), self.tag_color,user_id,self)
                        btn = QPushButton()
                        self.ui.tableWidget.setCellWidget(row_idx, 6, tag_widget)
                    else:
                         btn = QPushButton("")
                         self.ui.tableWidget.setCellWidget(row_idx, 6, btn)

                    btn.clicked.connect(lambda _, uid=user_id: self.open_tag_selector(uid))
                    btn.setFocusPolicy(Qt.NoFocus)  
                else:
                    if real_col_idx != 6:
                        item = QTableWidgetItem(str(cell_data) if cell_data else "")
                        self.ui.tableWidget.setItem(row_idx, real_col_idx, item)
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.tableWidget.setColumnWidth(5, 50)
        logger.info("Dane zostały załadowane do tabeli.")
        # print(f"Liczba kolumn w tabeli: {self.ui.tableWidget.columnCount()}")

def load_data_from_database(self) -> None:
        
        """
        Wczytuje dane z bazy SQLite i wypełnia tabelę widżetem.
        Używa zapytania SQL z lewym łączeniem, aby zebrać informacje o użytkownikach oraz ich tagach.
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
        # określa który pakiet email trzeba pobrać  
        offset = self.current_page * self.emails_per_page
        if not self.db_connection:
            logger.error("Brak połączenia z bazą danych.")
            print("Brak połączenia z bazą danych.")
            QApplication.restoreOverrideCursor()
            logger.error(f"Błąd podczas wykonywania zapytania: {e}")
            return
            
        if self.active_filters['tag']=="":
            query = f'''
                SELECT e.id, e.sender_name, e.recipients, e.subject, e.date, e.flag, e.cc,e.bcc,
                    GROUP_CONCAT(t.tag_name) AS tags 
                FROM emails e
                LEFT JOIN email_tags et ON e.id = et.email_id
                LEFT JOIN tags t ON et.tag_id = t.id
                {db_email.apply_filters(self.active_filters)}
                GROUP BY e.id
                LIMIT {self.emails_per_page} OFFSET {offset}
            '''
        else: 
            query = db_email.tag_query(self.active_filters) + f" LIMIT {self.emails_per_page} OFFSET {offset}"
        
        print(query)
        try:
            cursor = self.db_connection.cursor()
            logger.info(f"Wysyła zapytanie")
            cursor.execute(query)
            logger.info(f"Zapytanie wykonane, pobiera dane z cursora")
            data = cursor.fetchall()
            logger.info(f"dane zapisane do zmiennej")
            cursor.execute(f'''SELECT COUNT() FROM emails 
            {db_email.apply_filters(self.active_filters)}''')

            emailc_count = cursor.fetchall()[0][0]
            self.all_emails_count = emailc_count

            self.max_page = math.ceil((int(self.all_emails_count)/int(self.emails_per_page)))
            self.ui.dataAnalysisPage.findChild(QLabel,"pageNumberLabel").setText(f"{self.current_page+1}/{self.max_page}")
            
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(7)
            #print(data)
            
            create_main_email_tale(self,data)
            
            

            self.ui.tableWidget.verticalHeader().setVisible(False)
            QApplication.restoreOverrideCursor()
            logger.info(f"END")
        except sqlite3.Error as e:
                QApplication.restoreOverrideCursor()
                logger.error(f"Błąd podczas wykonywania zapytania: {e}")
                print(f"Błąd podczas wykonywania zapytania: {e}")

def load_color_dictionery(self):
        all_tags = db_email.get_all_tags(self.db_connection)
        json_path = ".\\tagColor.json"
        with open(json_path, 'r') as file:
            color_json = json.load(file)
        self.tag_color ={}
        if len(all_tags) > 0:
            for i in range(len(all_tags)):
                self.tag_color.setdefault(all_tags[i][1], color_json.get(str(i)))
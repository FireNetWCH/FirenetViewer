import os
import sqlite3
import logging
from typing import Any, List, Dict, Optional
import pandas as pd
from PySide6.QtCore import Qt, QSettings, QDir, QPoint,QEasingCurve,QRect
from PySide6.QtGui import QFont, QFontDatabase, QAction,QStandardItem, QPixmap, QImage, QPainter
from PySide6.QtWidgets import (
    QCheckBox, QPushButton, QGraphicsScene, QTableWidgetItem, QMenu, QFileSystemModel,QSplitter,QFrame,QApplication,QTableWidget,QDialog,QCalendarWidget,
    QTreeView, QVBoxLayout, QFileDialog, QGraphicsView, QTreeWidgetItem,QListWidgetItem, QTreeWidget, QMainWindow,QListWidget,QHeaderView,QAbstractItemView
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import fitz
from PySide6.QtCore import QPropertyAnimation as QAnimation
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.multi_tag_dialog import MultiTagInputDialog
from src.multi_tag_selector import MultiTagSelector
from src.gui_function import display_file_content
from src.key_press_filter import KeyPressFilter
from src.calendar_dialog_widget import get_selected_date
from datetime import datetime
import math
import json
import shutil

# from src.viewers.pdf_viewer import display_pdf_content
# from src.viewers.img_viewer import display_img_content
# from src.viewers.video_viewer import display_vidoe_content
# from src.viewers.dir_viewers import display_dir_content

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GUIFunctions:
    """ Klasa zawierająca funkcje obsługujące interfejs graficzny i logikę aplikacji. """
    def __init__(self, main_window: QMainWindow) -> None:
        self.main = main_window
        self.ui = main_window.ui
        self.db_connection: Optional[sqlite3.Connection] = None
        self.active_filters: Dict[str, str] = {'sender_name': "", "cc": "", "subject": "", "date_fr": "", 'date_to':"","folder_id" : "1","body":""}
        self.columns_hidden: List[bool] = [False] * 7
        self.filtering_active: bool = False
        self.current_sort_order: Dict[int, Any] = {}

        #Parametry do obsługi emeil
        file_config = open(".\\config.json")
        config = json.load(file_config)
        base_path = config['path']
        self.path = base_path
        self.sql_name = ""
        self.id_selected_email = 0
        self.is_expanded_serch_frame = False

        self.max_page = 0
        self.all_emails_count = 0
        self.current_page = 0
        self.emails_per_page = 500

        #self.key_filter = KeyPressFilter()
        #self._connect_to_database("D:\\SQL\\archiw_rpabich_2020\\archiw_rpabich_2020.sqlite")
        self._setup_ui(self.path)

        header = self.ui.tableWidget.horizontalHeader()
        for col in range(self.ui.tableWidget.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)
        splitter = QSplitter(Qt.Horizontal)
        dada_layout = self.ui.dataAnalysisPage.layout()
        splitter.addWidget(self.ui.tableWidget)
        splitter.addWidget(self.ui.EmailtabWidget)
        
        dada_layout.addWidget(splitter)

        # splitter2 = QSplitter(Qt.Horizontal)
        # dada_layout2 = self.ui.centralwidget.layout()
        
        # splitter2.addWidget(self.ui.centerMenu)
        # splitter2.addWidget(self.ui.mainBody)
        
        
        # dada_layout2.addWidget(splitter2)

        
        #self.load_data_from_database()
        #self.load_data_and_plot()
        


    def _setup_ui(self,path_database) -> None:
        """Inicjalizacja interfejsu – ustawienia czcionki, motywu oraz połączenia sygnałów."""
        self.enable_column_rearrangement()
        self.load_product_sans_font()
        self.initialize_app_theme()
        self.display_folders_in_help_page()
        self.display_database(path_database)
        self._connect_signals()

        # Konfiguracja widoku drzewa katalogów
        self.ui.select_directory.clicked.connect(self.select_directory)
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath('')
        self.tree_view = QTreeView(self.main)
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setVisible(False)
        layout = QVBoxLayout(self.main)
        layout.addWidget(self.tree_view)

        # Ustawie parametrów Ramki Wysukiwania Email i jej animacji
        frame = self.ui.dataAnalysisPage.findChild(QFrame, "serchEmailFrame")
        self.animation = QAnimation(frame, b'maximumHeight')
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.is_expanded_serch_frame = True


    def _connect_signals(self) -> None:
        """Łączy sygnały z odpowiednimi metodami."""
        # Menu (centralne i boczne)
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())

        # Obsługa wyszukiwania i filtrów
        self.ui.searchBtn.clicked.connect(self.show_search_results)
        self.ui.filter_table_btn.clicked.connect(self.join_search)
        self.ui.seachSurname.returnPressed.connect(self.join_search)
        self.ui.seachName.returnPressed.connect(self.join_search)
        self.ui.searchBody.returnPressed.connect(self.join_search)
        self.ui.searchDate.returnPressed.connect(self.join_search)
        self.ui.show_table_btn.clicked.connect(self.show_all_columns)
        self.ui.show_flags_btn.clicked.connect(self.toggle_filter_flags)
        self.ui.export_pdf.clicked.connect(self.export_to_pdf)
        self.ui.export_excel.clicked.connect(self.export_to_excel)
        self.ui.pst_files_btn.clicked.connect(self.upload_pst_file)
        #self.ui.checkBoxData.checkStateChanged.connect(self.date_state_box)

        self.ui.startDataLabel.selectionChanged.connect(self.serch_by_date_start)
        self.ui.endDataLabel.selectionChanged.connect(self.serch_by_date_end)
        self.ui.startDataBtn.clicked.connect(self.serch_by_date_start)
        self.ui.endDataBtn.clicked.connect(self.serch_by_date_end)
        self.ui.startDataLabel.textChanged.connect(self.join_search)
        self.ui.endDataLabel.textChanged.connect(self.join_search)

        # Obsługa Event Tabeli Email
        self.ui.tableWidget.cellClicked.connect(self.load_clicked_email)
        self.ui.tableWidget.cellActivated.connect(self._get_id_flags_item_email)
        self.key_filter = KeyPressFilter(self.ui.tableWidget, self._get_id_flags_item_email,self.load_clicked_email)
        self.ui.tableWidget.installEventFilter(self.key_filter)
        self.ui.prevEmailTableBtn.clicked.connect(self.previous_page)
        self.ui.nextEmailTableBtn.clicked.connect(self.next_page)
        self.ui.showSearchPanelBtn.clicked.connect(self.toggle_frame)
        # Obłsuga kliknięcia w drzewo katalogów Email
        tw = self.ui.helpPage.findChild(QTreeWidget,"folders_tree")
        tw.itemClicked.connect(self.tree_email_dir_clicked)

        # Obsługa Wyboru Bazy Emaili
        db_list = self.ui.helpPage.findChild(QListWidget, "db_list")
        db_list.itemClicked.connect(self.selec_sqlit_db)

        # Obsługa wyświetlania mutlimediów z załącznków email
        la = self.ui.EmailtabWidget.findChild(QListWidget,"listAttachments")
        la.itemClicked.connect(self.email_copy_attachments)


        # Konfiguracja menu nagłówka tabeli
        header = self.ui.tableWidget.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_column_menu)

        self.ui.dataAnalysisPage.setStyleSheet("""
       QTabWidget {
        border: 0px solid black;
    }
""")

        self.ui.EmailtabWidget.setStyleSheet("""
    QFrame {
        border: 1px solid black;
    }
    QLabel {
        border: 0px solid black;
    }
       QTabWidget {
        border: 0px solid black;
    }
    QPushButton{
           flat:False                                  }                                        
""")
        
        self.ui.serchEmailFrame.setStyleSheet("""
            QLineEdit{
                        border: 1px solid black;}
            QPushButton{border: 1px solid black
                                              ;}
        """)
        
        


        self.ui.tableWidget.setStyleSheet("""
    QTableWidget::item:selected {
        background-color: lightblue;  /* Intensywny kolor zaznaczonego wiersza */
        color: black;
       /*border: 2px solid blue;   Ramka wokół zaznaczonego wiersza */
    }

    QTableWidget::item:selected:!active {
        background-color: #A0C8FF;  /* Kolor dla nieaktywnego zaznaczenia */
        color: black;
        /*border: 2px solid #0078D7;   Podkreślenie, gdy tabela traci fokus */
    }
""")
    def serch_by_date_start(self):
        print(self)
        date = get_selected_date(self)
        if date is not None:
            self.ui.startDataLabel.setText(date.toString("yyyy-MM-dd"))
        else:
            self.ui.startDataLabel.setText("")
    def serch_by_date_end(self):
        print(self)
        date = get_selected_date(self)
        if date is not None:
            self.ui.endDataLabel.setText(date.toString("yyyy-MM-dd"))
        else:
            self.ui.endDataLabel.setText("")
    def toggle_frame(self):
        if self.is_expanded_serch_frame:
            self.animation.setStartValue(self.ui.dataAnalysisPage.findChild(QFrame,"serchEmailFrame").height())
            self.animation.setEndValue(0)
        else:
            self.animation.setStartValue(self.ui.dataAnalysisPage.findChild(QFrame,"serchEmailFrame").height())
            self.animation.setEndValue(100) 
        self.animation.start()

        self.is_expanded_serch_frame = not self.is_expanded_serch_frame

    def next_page(self):
        if self.current_page < self.max_page-1:
            self.current_page += 1
        self.load_data_from_database()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        self.load_data_from_database()

    def _get_id_flags_item_email(self,row,column):
        id = self.ui.tableWidget.item(row,0).text()
        check_box = self.ui.tableWidget.cellWidget(row,5)
        flags = int(check_box.isChecked())
        if flags == 1:
            flags = 0
            check_box.setChecked(False)
        else:
            flags = 1
            check_box.setChecked(True)
        self.update_flag(id,flags)
        
    def date_state_box(self):
        pom = self.ui.checkBoxData.isChecked()
        self.ui.seachOd.setEnabled(pom)
        self.ui.seachDo.setEnabled(pom)


    def selec_sqlit_db(self,item):
        print(os.path.join(self.path,item.text().split('.')[0],item.text()))
        if not self.db_connection is None: 
            self.db_connection.close()
            print("zamknięto polaczenie")
        db_path = os.path.join(self.path,item.text().split('.')[0],item.text())
        self._connect_to_database(db_path)
        sql_name = db_path.split('\\')[-1]
        sql_name = sql_name.removesuffix('.sqlite')
        self.sql_name = sql_name
        self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(sql_name)
        self.load_data_from_database()
        self.display_folders_in_help_page()
        tw = self.ui.helpPage.findChild(QTreeWidget,"folders_tree")
        tw.itemClicked.connect(self.tree_email_dir_clicked)
        self.clear_filtr()

    def _connect_to_database(self, db_name: str) -> None:
        """Nawiązuje połączenie z bazą danych SQLite."""
        try:
            self.db_connection = sqlite3.connect(db_name)
            logger.info(f"Połączono z bazą danych {db_name}")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas łączenia z bazą danych: {e}")
            self.db_connection = None
    
    def load_clicked_email(self,row,column):
        id = self.ui.tableWidget.item(row,0).text()
        self.id_selected_email = id
        query =f'''
        SELECT * from emails WHERE id = {id}
        '''

        body_label = self.ui.EmailtabWidget.findChild(QLabel, "body")
        subject_label = self.ui.EmailtabWidget.findChild(QLabel, "subject")
        sender_label = self.ui.EmailtabWidget.findChild(QLabel, "sender")
        date_label = self.ui.EmailtabWidget.findChild(QLabel, "date")
        cc_label = self.ui.EmailtabWidget.findChild(QLabel, "cc")
        
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        emai_value = cursor.fetchall()

        query_attachments = f'''SELECT * FROM attachments WHERE email_id ={emai_value[0][0]}'''
        cursor.execute(query_attachments)
        attachments_value = cursor.fetchall()
        listAttachments = self.ui.EmailtabWidget.findChild(QListWidget, "listAttachments")
        listAttachments.clear()
        for _, file_name, extra_value in attachments_value:
            item = QListWidgetItem(f"{file_name}")  
            #item.setData(extra_value) 
            listAttachments.addItem(item)
            print(item)
        listAttachments.setFixedHeight(60)
        search_term = self.active_filters['body']
        pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        

        if isinstance(emai_value[0][8],str):
            tekst = emai_value[0][8]
            tekst_html = tekst.replace('\n', '<br>')
            if(search_term ==""):
                body_label.setText(tekst_html)
            else:
                print(search_term)
                highlighted_content = pattern.sub(lambda match: f"<span style='background-color: yellow;'>{match.group()}</span>",tekst_html)
                body_label.setTextFormat(Qt.TextFormat.RichText)    
                body_label.setText(highlighted_content)
                
        
        else:
            tekst = emai_value[0][8].decode("utf-8")
            tekst_html = tekst.replace('\n', '<br>')

            print("TEKST CZYSTY: "+emai_value[0][8].decode("utf-8"))
            docoda_text = emai_value[0][8].decode("utf-8")
            if(search_term ==""):
                body_label.setText(tekst_html)
            else:
                print(search_term)
                highlighted_content = pattern.sub(lambda match: f"<span style='background-color: yellow;'>{match.group()}</span>",tekst_html)
                body_label.setTextFormat(Qt.TextFormat.RichText) 
                body_label.setText(highlighted_content)
                print(" TEKST OCZYSZCZONY : "+ highlighted_content)

        subject_label.setText(emai_value[0][7])
        sender_label.setText(emai_value[0][3])
        date_label.setText(emai_value[0][1])
        cc_label.setText(emai_value[0][5])
        # cc_label.setFrameStyle(QFrame.Box | QFrame.Plain)
        # cc_label.setLineWidth(2)
        # cc_label.setStyleSheet("border: 2px solid red; background-color: yellow; padding: 5px;")

    def clear_filtr(self):
        self.ui.seachName.setText("")
        self.ui.seachSurname.setText("")
        self.ui.searchDate.setText("")
        self.ui.searchBody.setText("")
        self.active_filters["sender_name"] = ""
        self.active_filters["cc"] = ""
        self.active_filters["subject"] = ""
        self.active_filters["body"] = ""
        
    def tree_email_dir_clicked(self,item ,column):
        self.active_filters["folder_id"] = item.data(0,1)
        self.clear_filtr()
        

        self.load_data_from_database()
        self.current_page = 0
        

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
            return
        
        query = f'''
            SELECT e.id, e.sender_name, e.cc, e.subject, e.date, e.flag,
                   GROUP_CONCAT(t.tag_name) AS tags 
            FROM emails e
            LEFT JOIN email_tags et ON e.id = et.email_id
            LEFT JOIN tags t ON et.tag_id = t.id
            {self.apply_filters()}
            GROUP BY e.id
            LIMIT {self.emails_per_page} OFFSET {offset}
        '''
        print(query)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            cursor.execute
            #print(f"{cursor.arraysize}")
            data = cursor.fetchall()
            cursor.execute(f'''SELECT COUNT(DISTINCT e.id) AS total_count FROM emails e
            {self.apply_filters()}''')
            emailc_count = cursor.fetchall()[0][0]
            self.all_emails_count = emailc_count
            self.max_page = math.ceil((int(self.all_emails_count)/int(self.emails_per_page)))
            self.ui.dataAnalysisPage.findChild(QLabel,"pageNumberLabel").setText(f"{self.current_page+1}/{self.max_page}")
            
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(7)
            #print(data)
            self.create_main_email_tale(data)
            self.ui.tableWidget.verticalHeader().setVisible(False)
            QApplication.restoreOverrideCursor()
        except sqlite3.Error as e:
                logger.error(f"Błąd podczas wykonywania zapytania: {e}")
                print(f"Błąd podczas wykonywania zapytania: {e}")


    def email_copy_attachments(self,item):
        source_path = os.path.join(self.path,self.sql_name,"Attachments",str(self.id_selected_email),item.text())
        destination_path, _ = QFileDialog.getSaveFileName(None, "Zapisz plik jako",item.text(), item.text().split('.')[-1])
        try:
         if destination_path:  
            shutil.copy(source_path, destination_path)
            print(f"Plik został skopiowany do: {destination_path}")
            logger.info(f"Plik został skopiowany do: {destination_path}")
        except Exception as e:
            print(f"Błąd podczas kopiowania pliku: {e}")
            logger.error(f"Błąd podczas kopiowania pliku: {e}")

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
                        lambda state, uid=user_id: self.update_flag(uid, state)
                    )
                    self.ui.tableWidget.setCellWidget(row_idx, real_col_idx, checkbox)
                elif real_col_idx == 6:
                    btn = QPushButton("Pokaż tagi")
                    btn.clicked.connect(lambda _, uid=user_id: self.open_tag_selector(uid))
                    btn.setFocusPolicy(Qt.NoFocus)
                    self.ui.tableWidget.setCellWidget(row_idx, real_col_idx, btn)
                else:
                    item = QTableWidgetItem(str(cell_data) if cell_data else "")
                    self.ui.tableWidget.setItem(row_idx, real_col_idx, item)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.tableWidget.setColumnWidth(5, 50)
        logger.info("Dane zostały załadowane do tabeli.")
        # print(f"Liczba kolumn w tabeli: {self.ui.tableWidget.columnCount()}")

    def open_tag_selector(self, user_id: int) -> None:
        """Otwiera okno dialogowe do edycji tagów użytkownika."""
        dialog = MultiTagSelector(user_id, self.db_connection, self.main)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika {user_id}")
            self.load_data_from_database()

    def update_flag(self, user_id: int, state: int) -> None:
        """Aktualizuje flagę użytkownika w bazie danych."""
        
        flag_value = 1 if state else 0
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE emails SET flag = ? WHERE id = ?", (flag_value, user_id))
            self.db_connection.commit()
            logger.info(f"Updated flag for emails ID {user_id} to {flag_value}.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizacji flagi: {e}")
            print(f"Błąd podczas aktualizacji flagi: {e}")
    def update_tag(self, user_id: int, tag_name: str) -> None:
        """Aktualizuje tag przypisany do użytkownika."""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id FROM tags WHERE tag_name = ?", (tag_name,))
            tag_id = cursor.fetchone()
            if tag_id:
                cursor.execute("UPDATE emails SET tag_id = ? WHERE id = ?", (tag_id[0], user_id))
                self.db_connection.commit()
                logger.info(f"Updated tag for emails ID {user_id} to {tag_name}.")
            else:
                logger.warning(f"Tag name '{tag_name}' not found.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizacji tagu: {e}")

    def close_database_connection(self) -> None:
        if self.db_connection:
            self.db_connection.close()

    def show_search_results(self) -> None:
        """Wyświetla wyszukane wyniki (przykładowo – pokazuje tooltip)."""
        search_phrase = self.ui.searchinp.text()
        if not search_phrase:
            return
        try:
            self.searchToolTip.show()
        except AttributeError:
            self.create_search_tip_overlay()
            self.searchToolTip.show()
        self.searchToolTip.setDescription("Wyszukuję informację dla... " + search_phrase)

    def initialize_app_theme(self) -> None:
        """Inicjalizuje motyw aplikacji na podstawie ustawień."""
        settings = QSettings()
        current_theme = settings.value("THEME")
        self.populate_theme_list(current_theme)
        self.ui.themeList.currentTextChanged.connect(self.change_app_theme)

    def populate_theme_list(self, current_theme: str) -> None:
        """Wypełnia listę dostępnych motywów."""
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            if theme.defaultTheme or theme.name == current_theme:
                index = self.ui.themeList.findData(theme.name)
                self.ui.themeList.setCurrentIndex(index)

    def change_app_theme(self) -> None:
        """Zmienia motyw aplikacji."""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")
        if current_theme != selected_theme:
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    def load_product_sans_font(self) -> None:
        """Ładuje czcionkę Product Sans i ustawia ją dla aplikacji."""
        font_id = QFontDatabase.addApplicationFont("./fonts/...")
        if font_id == -1:
            logger.error("Failed to load Product Sans font")
            return 
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        product_sans = QFont(font_families[0] if font_families else 'Sans Serif')
        self.main.setFont(product_sans)

    def load_filtr_dict(self) -> None:
        self.active_filters["sender_name"] = self.ui.seachName.text().lower()
        self.active_filters["cc"] = self.ui.seachSurname.text().lower()
        self.active_filters["subject"] = self.ui.searchDate.text().lower()
        self.active_filters["date_fr"] = self.ui.startDataLabel.text().lower()
        self.active_filters["date_to"] = self.ui.endDataLabel.text().lower()
        self.active_filters["body"] = self.ui.searchBody.text().lower()

    def join_search(self):
        self.load_filtr_dict()
        self.load_data_from_database()


    def apply_filters(self) -> None:
        """
        Zwraca fragmęt zapytania SQL zawierający filtry 
        """
        query_part = ""
        firtFiltr = True
        #print(self.active_filters)
        for key, value in self.active_filters.items():
            if key == "folder_id" and str(value) == "1":
                print(f"{key} +{value}")
            elif (key == "date_fr"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE date > '{value}'"
                        firtFiltr = False
                    else:
                        query_part = query_part +f"AND date > '{value}'"
            elif (key == "date_to"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE date < '{value}'"
                        firtFiltr = False
                    else:
                        query_part = query_part +f"AND date < '{value}'"
            elif(key == "body"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE REPLACE(body, X'200C', '') LIKE '%{value}%' COLLATE NOCASE"
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND REPLACE(body, X'200C', '') LIKE '%{value}%' COLLATE NOCASE"
            else:
                if value != "" :
                    if firtFiltr:
                        query_part = f"WHERE {key} LIKE '%{value}%' COLLATE NOCASE "
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND {key} LIKE '%{value}%' COLLATE NOCASE "

        return query_part    

    def show_column_menu(self, position: QPoint) -> None:
        """Wyświetla menu kontekstowe dla nagłówka kolumny."""
        header = self.ui.tableWidget.horizontalHeader()
        column = header.logicalIndexAt(position)
        menu = QMenu(self.main)
        sort_asc_action = QAction("Sortuj rosnąco", self.main)
        sort_desc_action = QAction("Sortuj malejąco", self.main)
        hide_column_action = QAction("Ukryj kolumnę", self.main)

        if column == 5:
            add_tag_action = QAction("Dodaj tag", self.main)
            add_tag_action.triggered.connect(self.open_add_tag_dialog)
            menu.addAction(add_tag_action)

        sort_asc_action.triggered.connect(lambda: self.sort_column(column, Qt.AscendingOrder))
        sort_desc_action.triggered.connect(lambda: self.sort_column(column, Qt.DescendingOrder))
        hide_column_action.triggered.connect(lambda: self.hide_columns(column))

        menu.addAction(sort_asc_action)
        menu.addAction(sort_desc_action)
        menu.addSeparator()
        menu.addAction(hide_column_action)
        menu.exec(header.mapToGlobal(position))

    def set_data(line_edit,text):
        line_edit.setText(text)

    def sort_column(self, column_index: int, order: Any) -> None:
        """Sortuje tabelę według wybranej kolumny."""
        self.ui.tableWidget.sortItems(column_index, order)

    def hide_columns(self, column_index: int) -> None:
        """Przełącza widoczność wskazanej kolumny."""
        self.columns_hidden[column_index] = not self.columns_hidden[column_index]
        self.ui.tableWidget.setColumnHidden(column_index, self.columns_hidden[column_index])

    def show_all_columns(self) -> None:
        """Przywraca widoczność wszystkich kolumn."""
        for i in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnHidden(i, False)
        self.columns_hidden = [False] * self.ui.tableWidget.columnCount()

    def enable_column_rearrangement(self) -> None:
        """Umożliwia przeciąganie i zmienianie kolejności kolumn w tabeli."""
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionsMovable(True)
        header.setDragEnabled(True)

    def plot_data(self, ages: List[int]) -> None:
        """Tworzy histogram wieku użytkowników i wyświetla go na widżecie."""
        scene = QGraphicsScene()
        fig, ax = plt.subplots(figsize=(5, 4))
        if ages:
            bins = range(min(ages), max(ages) + 2)
            ax.hist(ages, bins=bins, alpha=0.7, color='blue')
        ax.set_title("Wiek ludzi z danych z tabeli")
        ax.set_xlabel("Wiek")
        ax.set_ylabel("Częstotliwość")
        canvas = FigureCanvas(fig)
        canvas.draw()
        scene.addWidget(canvas)
        self.ui.graphicsView.setScene(scene)

    def open_add_tag_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        dialog = MultiTagInputDialog(self.db_connection, self.main)
        if dialog.exec():
            logger.info("Nowy tag został dodany.")
            self.load_data_from_database()

    def toggle_filter_flags(self) -> None:
        """Przełącza tryb filtrowania według zaznaczonych flag."""
        if self.filtering_active:
            self.reset_filters()
        else:
            self.filter_checked_flags()
        self.filtering_active = not self.filtering_active

    def filter_checked_flags(self) -> None:
        """Ukrywa wiersze, w których flaga nie jest zaznaczona."""
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox = self.ui.tableWidget.cellWidget(row, 4)
            if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                self.ui.tableWidget.showRow(row)
            else:
                self.ui.tableWidget.hideRow(row)

    def reset_filters(self) -> None:
        """Przywraca widoczność wszystkich wierszy tabeli."""
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.showRow(row)

    def export_to_pdf(self) -> None:
        """Eksportuje widoczne dane tabeli do pliku PDF."""
        file_path, _ = QFileDialog.getSaveFileName(
            self.main, "Zapisz plik PDF", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if not file_path:
            return
        if not file_path.endswith(".pdf"):
            file_path += ".pdf"
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 30, "Przefiltrowane dane z tabeli")
        c.setFont("Helvetica", 12)
        row_height = 20
        start_y = height - 60

        for row in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.isRowHidden(row):
                continue
            row_data = []
            for column in range(self.ui.tableWidget.columnCount()):
                if column == 4:
                    widget = self.ui.tableWidget.cellWidget(row, column)
                    row_data.append("Tak" if isinstance(widget, QCheckBox) and widget.isChecked() else "Nie")
                else:
                    item = self.ui.tableWidget.item(row, column)
                    row_data.append(item.text() if item else "")
            c.drawString(30, start_y - row * row_height, ", ".join(row_data))
        c.save()
        logger.info(f"Plik PDF zapisany jako: {file_path}")

    def export_to_excel(self) -> None:
        """Eksportuje widoczne dane tabeli do pliku Excel."""
        file_path, _ = QFileDialog.getSaveFileName(
            self.main, "Zapisz plik Excel", "", "Excel Files (*.xlsx);;All Files (*)"
        )
        if not file_path:
            return
        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"
        data = []
        for row in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.isRowHidden(row):
                continue
            row_data = []
            for column in range(self.ui.tableWidget.columnCount()):
                if column == 4:
                    widget = self.ui.tableWidget.cellWidget(row, column)
                    row_data.append("Tak" if isinstance(widget, QCheckBox) and widget.isChecked() else "Nie")
                else:
                    item = self.ui.tableWidget.item(row, column)
                    row_data.append(item.text() if item else "")
            data.append(row_data)
        df = pd.DataFrame(data, columns=["Imię", "Nazwisko", "Data urodzenia", "Wiek", "Flagi", "Tagi"])
        df.to_excel(file_path, index=False)
        logger.info(f"Plik Excel zapisany jako: {file_path}")

    def select_directory(self) -> None:
        """Pozwala wybrać katalog, a następnie wyświetla jego zawartość."""
        directory = QFileDialog.getExistingDirectory(self.main, "Wybierz katalog", "", options=QFileDialog.Options())
        if directory:
            self.replace_label_with_treeview(directory)
            self.switch_to_file_reader()

    def switch_to_file_reader(self) -> None:
        """Przełącza widok na czytnik plików."""
        self.ui.fileBtn.click()

    def replace_label_with_treeview(self, directory: str) -> None:
        """Zamienia etykietę na widok drzewa katalogów."""
        self.file_system_model.setRootPath(directory)
        self.file_system_model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.tree_view.setRootIndex(self.file_system_model.index(directory))
        for col in [1, 2, 3]:
            self.tree_view.setColumnHidden(col, True)
        layout = self.ui.fileReader.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.fileReader)
            self.ui.fileReader.setLayout(layout)
        # Usunięcie starych widżetów
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)
        layout.addWidget(self.tree_view)
        self.tree_view.setVisible(True)
        self.tree_view.selectionModel().selectionChanged.connect(self.on_file_selection_changed)

    def on_file_selection_changed(self) -> None:
        """Wywoływana po zmianie zaznaczenia – wyświetla zawartość wybranego pliku."""
        selected_indexes = self.tree_view.selectedIndexes()
        if selected_indexes:
            selected_file_path = self.file_system_model.filePath(selected_indexes[0])
            display_file_content(self,selected_file_path)

    # def display_file_content(self, file_path: str) -> None:
    #     """W zależności od rozszerzenia, wyświetla zawartość pliku lub komunikat o braku wsparcia."""
    #     try:
    #         _, ext = os.path.splitext(file_path.lower())
    #         if ext in ['.txt', '.csv', '.py', '.log']:
    #             with open(file_path, 'r', encoding='utf-8') as file:
    #                 content = file.read()
    #             self.ui.label_11.setText(content)
    #         elif ext == '.pdf':
    #             display_pdf_content(self,0,1, file_path)
    #         elif ext in ['.jpg','.jpeg','.png','.gif','.bmp','.ppm']:
    #             display_img_content(self,file_path)
    #         elif ext == '.pst':
    #             self.display_image_message("PST files are in progress.")
    #         elif ext in ['.mp4','.avi','.mkv','.mov','.wmv','.flv','.ogv']:
    #             display_vidoe_content(self,file_path)
    #         elif os.path.isdir(file_path):
    #             display_dir_content(self,file_path)
    #         else:
    #             self.ui.label_11.setText("Selected file type is not supported.")
    #     except Exception as e:
    #         self.ui.label_11.setText(f"Could not read file: {e}")

    def display_image_message(self, message: str) -> None:
        """Wyświetla komunikat (np. informujący o niedostępnej funkcjonalności)."""
        self.ui.label_11.setText(message)

    def upload_pst_file(self) -> None:
        """Pozwala wybrać plik PST i wywołuje funkcję jego przetwarzania."""
        pst_file, _ = QFileDialog.getOpenFileName(self.main, "Wybierz plik .pst", "", "PST Files (*.pst)")
        if pst_file:
            self.process_pst_file(pst_file)

    def process_pst_file(self, pst_file: str) -> None:
        """Przetwarza plik PST (implementację uzupełnij według potrzeb)."""
        logger.info(f"Przetwarzanie pliku PST: {pst_file}")

    def display_folders_in_help_page(self):
        self.folders_tree = QTreeWidget()
        self.folders_tree.setHeaderLabel("Struktura folderów (z bazy)")
        self.folders_tree.setObjectName("folders_tree")
        layout = self.ui.helpPage.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.helpPage)
            self.ui.helpPage.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                print(w.objectName)
                if (w) and not (isinstance(w ,QListWidget)):
                    w.setParent(None)
        layout.addWidget(self.folders_tree)
        self.load_folders_data_into_tree()
        

    def load_folders_data_into_tree(self):
        if not self.db_connection:
            return
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT path, id FROM folders")
            rows = cursor.fetchall()
            tree_dict = {}
            for row in rows:
                full_path = row[0]
                dir_id = row[1]
                parts = full_path.split("\\")
                current_level = tree_dict

                for part in parts:
                    if part not in current_level:
                        current_level[part] = {"id": dir_id, "subfolders": {}}
                    current_level = current_level[part]["subfolders"]
            self.folders_tree.clear()
            self.add_items_to_tree(self.folders_tree,tree_dict)
            
        except sqlite3.Error as e:
            print(f"Błąd zapytania do bazy: {e}")

    def add_items_to_tree(self, parent, tree_level: dict):
        for folder_name, folder_data in tree_level.items():
            item = QTreeWidgetItem([folder_name])
            item.setData(0, 1, folder_data["id"])
            if isinstance(parent, QTreeWidget):
                parent.addTopLevelItem(item)
            else:
                parent.addChild(item)
            if folder_data["subfolders"]:
                self.add_items_to_tree(item, folder_data["subfolders"])

    def display_database(self,path_to_dir):
        self.list_widget = QListWidget()
        self.list_widget.setObjectName("db_list")
        sql_list_file = []
        dir_content =  os.scandir(path_to_dir)
        for file in dir_content:
            if os.path.isdir(os.path.join(path_to_dir,file)):
                list_file = os.scandir(os.path.join(path_to_dir,file))
                for sq_file in list_file:
                    if os.path.isfile(os.path.join(path_to_dir,file,sq_file)) :
                        _, ext = os.path.splitext(sq_file.name.lower())
                        if ext == '.sqlite':
                            sql_list_file.append(sq_file.name)


        if self.db_connection is None and len(sql_list_file) > 0 :
            try:
                self._connect_to_database(path_to_dir+"\\"+sql_list_file[0].split('.')[-2]+"\\"+sql_list_file[0])
                self.load_data_from_database()
                self.sql_name =sql_list_file[0].split('.')[-2]
                self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(self.sql_name)
                logger.info(f"Połączono z pierwszą odnalezioną bazą SQLite: {self.sql_name}")
            except Exception as e:
                logger.error(f"Bład przy pierwszym łaczeniu do SQLite: {e}")
        print(sql_list_file)
        self.list_widget.addItems(sql_list_file)    
        layout = self.ui.helpPage.layout()
        layout.addWidget(self.list_widget)

    
from PySide6.QtWidgets import QTableWidgetItem,QAbstractItemView,QPushButton,QHeaderView,QLabel,QListWidget,QListWidgetItem,QComboBox
from PySide6.QtCore import Qt
import src.db_function.db_email_function as db_email
import logging
import os
import re
from src.db_function.db_email_function import select_all_label
from src.atachment_list_widget import FileListItem
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def load_all_labels(self):
    data = select_all_label(self.db_connection)
    self.ui.LabelTableWidget.setRowCount(0)
    self.ui.LabelTableWidget.setRowCount(len(data))
    #self.ui.LabelTableWidget.setHorizontalHeaderItem(len(data[0]), QTableWidgetItem("Usuń"))

    for row_idx, row_data in enumerate(data):
        label_id = row_data[0]  

        labes_name = db_email.get_all_labels_name(self.db_connection)
        
        all_labels = [(label[0], label[1]) for label in labes_name]
        item_id = QTableWidgetItem(str(label_id))
        self.ui.LabelTableWidget.setItem(row_idx, 0, item_id)
        self.ui.LabelTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        for col_idx, cell_data in enumerate(row_data):
            if col_idx == 2:
                combo_box = QComboBox()
                for id_, name in all_labels:
                    combo_box.addItem(name, id_) 
                combo_box.setCurrentText(str(cell_data))
                combo_box.setFocusPolicy(Qt.NoFocus)
                combo_box.wheelEvent = lambda event: event.ignore()
                combo_box.currentIndexChanged.connect(lambda _, row=label_id, cb=combo_box: label_name_changed(self, self.db_connection, row, cb.currentData()))
                self.ui.LabelTableWidget.setCellWidget(row_idx, col_idx, combo_box)
            else:
                item = QTableWidgetItem(str(cell_data) if cell_data else "")
                self.ui.LabelTableWidget.setItem(row_idx, col_idx, item)
        delete_button = QPushButton("Usuń")
        delete_button.clicked.connect(lambda _, id=label_id: delete_row(self,id))
        delete_button.setFocusPolicy(Qt.NoFocus)
        self.ui.LabelTableWidget.setCellWidget(row_idx, len(row_data), delete_button)

    self.ui.LabelTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
    self.ui.LabelTableWidget.setColumnWidth(0, 50)

    logger.info("Dane zostały załadowane do tabeli.")

def label_name_changed(self,db_connection,id_email_label,id_label):
    db_email.update_id_labels_name(db_connection,id_email_label,id_label)
    load_all_labels(self)

def delete_row (self,id_email_label):
    db_email.delate_email_labels(self.db_connection,id_email_label)
    load_all_labels(self)
    

def load_clicked_email_on_labels(self, row):
    self.last_clicket_row = row
    id = self.ui.LabelTableWidget.item(row, 3).text()
    search_term = self.ui.LabelTableWidget.item(row, 1).text().strip()
    self.id_selected_label = self.ui.LabelTableWidget.item(row, 0).text()
    self.id_selected_email = id
    query = f"SELECT * FROM emails WHERE id = {id}"

    for x in range(self.ui.EmailtabWidget.count() - 1, 0, -1):
        self.ui.EmailtabWidget.removeTab(x)

    body_label = self.ui.EmailtabWidget_2.findChild(QLabel, "body_2")
    subject_label = self.ui.EmailtabWidget_2.findChild(QLabel, "subject_2")
    sender_label = self.ui.EmailtabWidget_2.findChild(QLabel, "sender_2")
    date_label = self.ui.EmailtabWidget_2.findChild(QLabel, "date_2")
    cc_label = self.ui.EmailtabWidget_2.findChild(QLabel, "cc_2")
    fraze_label = self.ui.EmailtabWidget_2.findChild(QLabel, "frazeLabel")
    cursor = self.db_connection.cursor()
    cursor.execute(query)
    email_value = cursor.fetchall()

    query_attachments = f"SELECT * FROM attachments WHERE email_id = {email_value[0][0]}"
    cursor.execute(query_attachments)
    attachments_value = cursor.fetchall()
    listAttachments = self.ui.EmailtabWidget_2.findChild(QListWidget, "listAttachments_2")
    listAttachments.clear()
    def on_item_clicked(item):
            widget = listAttachments.itemWidget(item)
            if widget:  
                widget.preview_file()
    for _, file_name, extra_value in attachments_value:
        file_path = os.path.join(self.path, self.sql_name, "Attachments", str(self.id_selected_email), file_name)
        widget = FileListItem(f"{file_name}", file_path, self.ui.EmailtabWidget_2)
        item = QListWidgetItem(listAttachments)
        item.setSizeHint(widget.sizeHint())
        listAttachments.addItem(item)
        listAttachments.setItemWidget(item, widget)

    listAttachments.itemClicked.connect(on_item_clicked)
    
    listAttachments.setFixedHeight(60)

  
    if isinstance(email_value[0][8], str):
        tekst = email_value[0][8]
    else:
        tekst = email_value[0][8].decode("utf-8")


    if not search_term:
        tekst_html = tekst.replace('\n', '<br>')
        body_label.setText(tekst_html)
        return  
    
    escaped_term = re.escape(search_term)  
    pattern_str = re.sub(r"\\\s+", r"\\s*+", escaped_term) 
    
    pattern = re.compile(pattern_str, re.IGNORECASE)

    highlighted_content = pattern.sub(lambda match: f"<span style='background-color: yellow;'>{match.group()}</span>", tekst)
    highlighted_content = highlighted_content.replace('\n', '<br>')

    body_label.setTextFormat(Qt.TextFormat.RichText)
    body_label.setText(highlighted_content)

    subject_label.setText(email_value[0][7])
    sender_label.setText(email_value[0][3])
    date_label.setText(email_value[0][1])
    cc_label.setText(email_value[0][5])
    fraze_label.setText(search_term)
        

from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QDialog,QLineEdit,QHBoxLayout,QWidget,QRadioButton,QButtonGroup
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize,QCoreApplication
from src.db_function.db_email_function import delate_label,updata_label_name,connect_to_database
import os
from src.email_page.tag_dialog import DeleteConfirmDialog
import logging
import sqlite3
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class LabelsCrud(QDialog):
    """Dialog do edycji labelek użytkownika."""
    def __init__(self, connection,path, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.path = path
        self.setWindowTitle(QCoreApplication.translate("label_dialog","Wybierz etykiete"))
        self.label_list = QListWidget(self)
        self.label_list.setObjectName("labelCrud")
        self.ok_btn = QPushButton("OK", self)
        self.add_btn = QPushButton(QCoreApplication.translate("label_dialog","Dodaj nową etykiete..."), self)
        # self.setObjectName("tagger")

        self.ok_btn.clicked.connect(self.accept)
        self.add_btn.clicked.connect(self.open_add_label_dialog)

        layout = QVBoxLayout(self)       
        layout.addWidget(self.label_list)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        self.load_labels(connection)

    def load_labels(self,connection) -> None:
        """Ładuje wszystkie labelki."""
        cursor = self.connection.cursor()
        self.label_list.clear()
        cursor.execute("SELECT id, label_name FROM labels_name")
        all_tags = cursor.fetchall()
        #name_tags = {row[0] for row in cursor.fetchall()}
        for tag_id, label_name in all_tags:
            item = QListWidgetItem(self.label_list)
            item.setSizeHint(QSize(200, 30))
            tag_edit = QLineEdit(label_name)
            tag_edit.setReadOnly(False)  
            remove_button = QPushButton()
            remove_button.setIcon((QIcon(":feather\\icons\\feather\\trash.png")))
            remove_button.setFixedSize(30, 30)
            remove_button.clicked.connect(lambda _, id=tag_id,label_name = label_name: delete_and_refresh(self,connection, id,label_name))
            save_button = QPushButton()
            save_button.setIcon((QIcon(":feather\\icons\\feather\\save.png")))
            save_button.setFixedSize(30, 30)
            save_button.clicked.connect(lambda _, id=tag_id, edit=tag_edit: updata_label_name(connection, id, edit.text()))
            labels_layout = QHBoxLayout()
            labels_layout.addWidget(tag_edit)
            labels_layout.addWidget(remove_button)
            labels_layout.addWidget(save_button)
            labels_layout.setContentsMargins(0, 0, 0, 0)
            container = QWidget()
            container.setLayout(labels_layout)
            self.label_list.addItem(item)
            self.label_list.setItemWidget(item, container)
    
    def open_add_label_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        dialog = LabelInputDialog(self.connection,path = self.path)
        if dialog.exec():
            print("Nowy tag został dodany.")
            self.load_labels(self.connection)

def delete_and_refresh(self, connection, tag_id,label_name):
    """Usuwa labelke, a następnie odświeża listę."""
    dialog = DeleteConfirmDialog(self)
    result = dialog.exec()
    if result == QDialog.Accepted:
        if dialog.is_global_delete():
            try:
                all_dir = os.scandir(self.path)
                for path in all_dir:
                    # print(os.path.join(self.path,path.name,path.name+'.sqlite'))
                    connect_to_database(self,os.path.join(self.path,path.name,path.name+'.sqlite'))
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM labels_name WHERE label_name = ?", (label_name,))
                    self.db_connection.commit()
            except sqlite3.Error as e:
                    logger.error(f"Błąd podczas usuwania lokalnie etykiety: {e} z bazy {path.name}")
                    print(f"Błąd podczas usuwania lokalnie etykiety: {e} z bazy {path.name}")
            self.load_labels(connection)
        else:
            try:
                delate_label(connection, tag_id) 
            except sqlite3.Error as e:    
                logger.error(f"Błąd podczas usuwania lokalnie etykiety: {e}")
                print(f"Błąd podczas usuwania lokalnie etykiety: {e}")

            self.load_labels(connection)
    


class LabelInputDialog(QDialog):
    """Dialog do dodawania nowej labelki."""
    def __init__(self, connection,path, parent=None ):
        super().__init__(parent)
        self.connection = connection
        self.path = path
        self.db_connection = None
        self.setWindowTitle(QCoreApplication.translate("label_dialog","Dodaj nową etykete"))
        self.new_tag_input = QLineEdit(self)
        self.new_tag_input.setPlaceholderText(QCoreApplication.translate("label_dialog","Wpisz nową etykete tutaj..."))

        self.radio_local = QRadioButton(QCoreApplication.translate("label_dialog","Dodaj etykiete loklanie"))
        self.radio_global = QRadioButton(QCoreApplication.translate("label_dialog","Dodaj etykiete globalnie"))
        self.radio_local.setChecked(True)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_local)
        self.button_group.addButton(self.radio_global)

        


        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.clicked.connect(self.add_new_tag)
        layout = QVBoxLayout(self)
        layout.addWidget(self.new_tag_input)
        layout.addWidget(self.radio_local)
        layout.addWidget(self.radio_global)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)

    def add_new_tag(self) -> None:
        """Dodaje nową etykete do bazy danych."""
        new_label_name = self.new_tag_input.text().strip()
        if new_label_name:
            if self.radio_local.isChecked():
                try:
                    cursor = self.connection.cursor()
                    cursor.execute("INSERT OR IGNORE INTO labels_name (label_name) VALUES (?)", (new_label_name,))
                    self.connection.commit()
                except sqlite3.Error as e:    
                    logger.error(f"Błąd podczas usuwania lokalnie etykiety: {e}")
                    print(f"Błąd podczas usuwania lokalnie etykiety: {e}")
                self.accept()
            else:
                all_dir = os.scandir(self.path)
                try:
                    for path in all_dir:
                        # print(os.path.join(self.path,path.name,path.name+'.sqlite'))
                        connect_to_database(self,os.path.join(self.path,path.name,path.name+'.sqlite'))
                        cursor = self.db_connection.cursor()
                        print("IGNORE TEST2")
                        cursor.execute("INSERT OR IGNORE INTO labels_name (label_name) VALUES (?)", (new_label_name,))
                        self.db_connection.commit()
                except:
                    logger.error(f"Błąd podczas dodawania globalnie etykiety: {e} do bazy {path.name}")
                    print(f"Błąd podczas dodawania globalnie etykiety: {e} do bazy {path.name}")
                self.accept()
            
            
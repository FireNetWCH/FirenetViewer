from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QDialog,QLineEdit,QHBoxLayout,QWidget,QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from src.db_function.db_email_function import delate_tag,updata_tag
from src.email_page.multi_tag_dialog import MultiTagInputDialog
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLineEdit,QRadioButton,QButtonGroup
import os
import src.db_function.db_email_function as db_email
class TagCrud(QDialog):
    """Dialog do edycji tagów użytkownika."""
    def __init__(self, connection, sql_name,parent=None,path = None):
        super().__init__(parent)
        self.connection = connection
        self.sql_name=sql_name
        self.path = path
        self.setWindowTitle("Wybierz kategorie")
        self.tag_list = QListWidget(self)
        self.tag_list.setObjectName("sekectorTag")
        self.ok_btn = QPushButton("OK", self)
        self.add_btn = QPushButton("Dodaj nową kategorie...", self)
        self.setObjectName("tagger")

        self.ok_btn.clicked.connect(self.accept)
        self.add_btn.clicked.connect(self.open_add_tag_dialog)

        layout = QVBoxLayout(self) 
        label = QLabel(f"Skrzynki Email: {self.sql_name}")
        layout.addWidget(label)      
        layout.addWidget(self.tag_list)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        self.load_tags(connection)
        

    def load_tags(self,connection) -> None:
        """Ładuje wszystkie tagi do edycji"""
        cursor = self.connection.cursor()
        self.tag_list.clear()
        cursor.execute("SELECT id, tag_name FROM tags")
        all_tags = cursor.fetchall()
        
        
        #name_tags = {row[0] for row in cursor.fetchall()}
        for tag_id, tag_name in all_tags:
            item = QListWidgetItem(self.tag_list)
            item.setSizeHint(QSize(200, 30))
            tag_edit = QLineEdit(tag_name)
            tag_edit.setReadOnly(False)  
            trash_button = QPushButton()
            trash_button.setIcon((QIcon(":feather\\icons\\feather\\trash.png")))
            trash_button.setFixedSize(30, 30)
            trash_button.clicked.connect(lambda _, id=tag_id,tag_name = tag_name: delete_and_refresh(self,connection, id,tag_name))
            save_button = QPushButton()
            save_button.setIcon((QIcon(":feather\\icons\\feather\\save.png")))
            save_button.setFixedSize(30, 30)
            save_button.clicked.connect(lambda _, id=tag_id, edit=tag_edit: updata_tag(connection, id, edit.text()))
            tag_layout = QHBoxLayout()
            tag_layout.addWidget(tag_edit)
            tag_layout.addWidget(trash_button)
            tag_layout.addWidget(save_button)
            tag_layout.setContentsMargins(0, 0, 0, 0)
            container = QWidget()
            container.setLayout(tag_layout)
            self.tag_list.addItem(item)
            self.tag_list.setItemWidget(item, container)

    def open_add_tag_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        print(self.path)
        dialog = MultiTagInputDialog(self.connection,path=self.path)
        if dialog.exec():
            print("Nowy tag został dodany.")
            self.load_tags(self.connection)

def delete_and_refresh(self, connection, tag_id,tag_name):
    """Usuwa tag, a następnie odświeża listę."""
    dialog = DeleteConfirmDialog(self)
    result = dialog.exec()
    if result == QDialog.Accepted:
        if dialog.is_global_delete():
            all_dir = os.scandir(self.path)
            for path in all_dir:
                print(os.path.join(self.path,path.name,path.name+'.sqlite'))
                db_email.connect_to_database(self,os.path.join(self.path,path.name,path.name+'.sqlite'))
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM tags WHERE tag_name = ?", (tag_name,))
                self.db_connection.commit()
            self.load_tags(connection)
        else:
            delate_tag(connection, tag_id) 
            self.load_tags(connection)
            
class DeleteConfirmDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Zakres usunięcia")
        layout = QVBoxLayout()
        self.label = QLabel("Czy usunąć lokalnie czy globalnie?")
        layout.addWidget(self.label)
        self.radio_local = QRadioButton("Usuń tylko lokalnie dla tej skrzynki")
        self.radio_global = QRadioButton("Usuń ze wszystkich skrzynek pocztowych")
        self.radio_local.setChecked(True)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_local)
        self.button_group.addButton(self.radio_global)

        layout.addWidget(self.radio_local)
        layout.addWidget(self.radio_global)

        btn_layout = QHBoxLayout()
        self.ok_btn = QPushButton("OK")
        self.cancel_btn = QPushButton("Anuluj")
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def is_global_delete(self):
        return self.radio_global.isChecked()
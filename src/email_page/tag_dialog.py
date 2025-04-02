from PySide6.QtWidgets import QListWidget, QListWidgetItem, QCheckBox, QPushButton, QVBoxLayout, QDialog,QLineEdit,QHBoxLayout,QWidget
from PySide6.QtCore import QSize
from src.db_function.db_email_function import delate_tag,updata_tag
from src.email_page.multi_tag_dialog import MultiTagInputDialog
class TagCrud(QDialog):
    """Dialog do edycji tagów użytkownika."""
    def __init__(self, connection, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.setWindowTitle("Wybierz tagi")
        self.tag_list = QListWidget(self)
        self.tag_list.setObjectName("sekectorTag")
        self.ok_btn = QPushButton("OK", self)
        self.add_btn = QPushButton("Dodaj nowy tag...", self)
        self.setObjectName("tagger")

        self.ok_btn.clicked.connect(self.accept)
        self.add_btn.clicked.connect(self.open_add_tag_dialog)

        layout = QVBoxLayout(self)       
        layout.addWidget(self.tag_list)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        self.load_tags(connection)

    def load_tags(self,connection) -> None:
        """Ładuje wszystkie tagi i zaznacza te przypisane do użytkownika."""
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
            plus_button = QPushButton("-")
            plus_button.setFixedSize(30, 30)
            plus_button.clicked.connect(lambda _, id=tag_id: delete_and_refresh(self,connection, id))
            save_button = QPushButton("S")
            save_button.setFixedSize(30, 30)
            save_button.clicked.connect(lambda _, id=tag_id, edit=tag_edit: updata_tag(connection, id, edit.text()))
            tag_layout = QHBoxLayout()
            tag_layout.addWidget(tag_edit)
            tag_layout.addWidget(plus_button)
            tag_layout.addWidget(save_button)
            tag_layout.setContentsMargins(0, 0, 0, 0)
            container = QWidget()
            container.setLayout(tag_layout)
            self.tag_list.addItem(item)
            self.tag_list.setItemWidget(item, container)
    
    def open_add_tag_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        dialog = MultiTagInputDialog(self.connection)
        if dialog.exec():
            print("Nowy tag został dodany.")
            self.load_tags(self.connection)

def delete_and_refresh(self, connection, tag_id):
    """Usuwa tag, a następnie odświeża listę."""
    delate_tag(connection, tag_id) 
    self.load_tags(connection)

from PySide6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLineEdit


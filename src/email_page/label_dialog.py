from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QDialog,QLineEdit,QHBoxLayout,QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from src.db_function.db_email_function import delate_label,updata_label_name

class LabelsCrud(QDialog):
    """Dialog do edycji labelek użytkownika."""
    def __init__(self, connection, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.setWindowTitle("Wybierz etykiete")
        self.label_list = QListWidget(self)
        self.label_list.setObjectName("labelCrud")
        self.ok_btn = QPushButton("OK", self)
        self.add_btn = QPushButton("Dodaj nową etykiete...", self)
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
        """Ładuje wszystkie tagi i zaznacza te przypisane do użytkownika."""
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
            remove_button.clicked.connect(lambda _, id=tag_id: delete_and_refresh(self,connection, id))
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
        dialog = LabelInputDialog(self.connection)
        if dialog.exec():
            print("Nowy tag został dodany.")
            self.load_labels(self.connection)

def delete_and_refresh(self, connection, tag_id):
    """Usuwa labelke, a następnie odświeża listę."""
    delate_label(connection, tag_id) 
    self.load_labels(connection)


class LabelInputDialog(QDialog):
    """Dialog do dodawania nowej labelki."""
    def __init__(self, connection, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.setWindowTitle("Dodaj nową etykete")
        self.new_tag_input = QLineEdit(self)
        self.new_tag_input.setPlaceholderText("Wpisz nową etykete tutaj...")
        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.clicked.connect(self.add_new_tag)
        layout = QVBoxLayout(self)
        layout.addWidget(self.new_tag_input)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)

    def add_new_tag(self) -> None:
        """Dodaje nową etykete do bazy danych."""
        new_label_name = self.new_tag_input.text().strip()
        if new_label_name:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO labels_name (label_name) VALUES (?)", (new_label_name,))
            self.connection.commit()
            self.accept()

            
            
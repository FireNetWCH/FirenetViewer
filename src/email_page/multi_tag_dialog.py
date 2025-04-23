from PySide6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLineEdit,QRadioButton,QButtonGroup
import os
import src.db_function.db_email_function as db_email
class MultiTagInputDialog(QDialog):
    """Dialog do dodawania nowego tagu."""
    def __init__(self, connection, parent=None,path = None):
        super().__init__(parent)
        self.db_connection = connection
        self.path = path
        self.setWindowTitle("Dodaj nową kategorię")
        self.new_tag_input = QLineEdit(self)
        self.new_tag_input.setPlaceholderText("Wpisz nową kategorię tutaj...")
        
        self.radio_btn_local = QRadioButton("Dodaj lokalnie")
        self.radio_btn_local.setChecked(True)
        self.radio_btn_global = QRadioButton("Dodaj globalnie")

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_btn_local)
        self.button_group.addButton(self.radio_btn_global)

        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.clicked.connect(self.add_new_tag)
        layout = QVBoxLayout(self)
        layout.addWidget(self.new_tag_input)
        layout.addWidget(self.radio_btn_local)
        layout.addWidget(self.radio_btn_global)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)

    def add_new_tag(self) -> None:
        """Dodaje nowy tag do bazy danych."""
        new_tag_name = self.new_tag_input.text().strip()
        if new_tag_name:
            if self.radio_btn_local.isChecked():
                cursor = self.db_connection.cursor()
                cursor.execute("INSERT INTO tags (tag_name) VALUES (?)", (new_tag_name,))
                self.db_connection.commit()
                self.accept()
            else:
                all_dir = os.scandir(self.path)
                for path in all_dir:
                    print(os.path.join(self.path,path.name,path.name+'.sqlite'))
                    db_email.connect_to_database(self,os.path.join(self.path,path.name,path.name+'.sqlite'))
                    cursor = self.db_connection.cursor()
                    cursor.execute("INSERT OR IGNORE INTO tags (tag_name) VALUES (?)", (new_tag_name,))
                    self.db_connection.commit()
                self.accept()

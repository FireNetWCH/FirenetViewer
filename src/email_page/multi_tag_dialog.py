from PySide6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLineEdit

class MultiTagInputDialog(QDialog):
    """Dialog do dodawania nowego tagu."""
    def __init__(self, connection, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.setWindowTitle("Dodaj nową kategorię")
        self.new_tag_input = QLineEdit(self)
        self.new_tag_input.setPlaceholderText("Wpisz nową kategorię tutaj...")
        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.clicked.connect(self.add_new_tag)
        layout = QVBoxLayout(self)
        layout.addWidget(self.new_tag_input)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)

    def add_new_tag(self) -> None:
        """Dodaje nowy tag do bazy danych."""
        new_tag_name = self.new_tag_input.text().strip()
        if new_tag_name:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO tags (tag_name) VALUES (?)", (new_tag_name,))
            self.connection.commit()
            self.accept()

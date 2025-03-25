from PySide6.QtWidgets import QListWidget, QListWidgetItem, QCheckBox, QPushButton, QVBoxLayout, QDialog

class MultiTagSelector(QDialog):
    """Dialog do edycji tagów użytkownika."""
    def __init__(self, user_id, connection, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.connection = connection
        self.setWindowTitle("Wybierz tagi")
        self.tag_list = QListWidget(self)
        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.clicked.connect(self.apply_changes)
        layout = QVBoxLayout(self)
        layout.addWidget(self.tag_list)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        self.load_tags()

    def load_tags(self) -> None:
        """Ładuje wszystkie tagi i zaznacza te przypisane do użytkownika."""
        cursor = self.connection.cursor()
        self.tag_list.clear()
        cursor.execute("SELECT id, tag_name FROM tags")
        all_tags = cursor.fetchall()
        cursor.execute("SELECT tag_id FROM email_tags WHERE email_id = ?", (self.user_id,))
        user_tags = {row[0] for row in cursor.fetchall()}
        for tag_id, tag_name in all_tags:
            item = QListWidgetItem(self.tag_list)
            checkbox = QCheckBox(tag_name)
            checkbox.setChecked(tag_id in user_tags)
            self.tag_list.addItem(item)
            self.tag_list.setItemWidget(item, checkbox)

    def apply_changes(self) -> None:
        """Aktualizuje tagi użytkownika według zaznaczonych pól."""
        selected_tag_ids = []
        cursor = self.connection.cursor()
        for i in range(self.tag_list.count()):
            item = self.tag_list.item(i)
            checkbox = self.tag_list.itemWidget(item)
            if checkbox.isChecked():
                tag_name = checkbox.text()
                cursor.execute("SELECT id FROM tags WHERE tag_name = ?", (tag_name,))
                tag_id = cursor.fetchone()[0]
                selected_tag_ids.append(tag_id)
        cursor.execute("DELETE FROM email_tags WHERE email_id = ?", (self.user_id,))
        for tag_id in selected_tag_ids:
            cursor.execute("INSERT INTO email_tags (email_id, tag_id) VALUES (?, ?)", (self.user_id, tag_id))
        self.connection.commit()
        self.accept()

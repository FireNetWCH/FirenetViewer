from PySide6.QtWidgets import QListWidget, QListWidgetItem, QCheckBox, QPushButton, QVBoxLayout, QDialog
from PySide6.QtCore import QSize
class SekectorTag(QDialog):
    """Dialog do edycji tagów użytkownika."""
    def __init__(self, connection,user_tag, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.setWindowTitle("Wybierz kategorie")
        self.tag_list = QListWidget(self)
        self.tag_list.setObjectName("sekectorTag")
        self.ok_btn = QPushButton("OK", self)
        self.setObjectName("tagger")
        self.ok_btn.clicked.connect(lambda :self.set_tag(user_tag))
        layout = QVBoxLayout(self)
        layout.addWidget(self.tag_list)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        
        self.load_tags(user_tag)

    def load_tags(self,user_tags) -> None:
        """Ładuje wszystkie tagi i zaznacza te przypisane do skrzynki."""
        cursor = self.connection.cursor()
        self.tag_list.clear()
        default_item = QListWidgetItem(self.tag_list)
        default_item.setSizeHint(QSize(150, 28))
        default_checkbox = QCheckBox("BEZ KATEGORI")
        tag_list = user_tags['tag'].strip("()").replace("'", "").split(',')
        if "#_empty_#" in tag_list:
            default_checkbox.setChecked(True)
        else:
            default_checkbox.setChecked(False)
        self.tag_list.addItem(default_item)
        self.tag_list.setItemWidget(default_item, default_checkbox)
        cursor.execute("SELECT id, tag_name FROM tags")
        all_tags = cursor.fetchall()
        #name_tags = {row[0] for row in cursor.fetchall()}
        for tag_id, tag_name in all_tags:
            item = QListWidgetItem(self.tag_list)
            item.setSizeHint(QSize(150, 28))
            checkbox = QCheckBox(tag_name)
            checkbox.setChecked(tag_name in tag_list)
            self.tag_list.addItem(item)
            self.tag_list.setItemWidget(item, checkbox)

    def set_tag(self,user_tag):
        string = ""        
        for i in range(self.tag_list.count()):
            item = self.tag_list.item(i)
            checkbox = self.tag_list.itemWidget(item)
            if checkbox.isChecked():
                if checkbox.text() !="BEZ KATEGORI":
                    if string !="":
                        string += ",'"+checkbox.text()+"'"
                    else:
                        string+= "'"+checkbox.text()+"'"
                else:
                    if string !="":
                        string += ",'"+"#_empty_#"+"'"
                    else:
                        string+= "'"+"#_empty_#"+"'"
        if string != "":
            user_tag['tag'] = "("+string+")"
        else:
            user_tag['tag'] = ""
            
        self.accept()
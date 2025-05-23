from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QTextEdit,QWidget,QVBoxLayout
class TxtViewers (QTextEdit):
    def __init__(self,parent = None):
        super().__init__()
        self.setReadOnly(True)
 
def display_txt_content(txt):
    txt_viewers = TxtViewers()

    txt_viewers.setText(txt)
    tab_content = QWidget()
    tab_layout = QVBoxLayout(tab_content)
    
    tab_layout.addWidget(txt_viewers)
    return tab_content
    
     
 
    
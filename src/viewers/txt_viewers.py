from PySide6.QtWidgets import QTextEdit
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget
import olefile
from PySide6.QtWidgets import QTextEdit,QWidget
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget,QVBoxLayout
#import olefile
import re
import string
class TxtViewers (QTextEdit):
    def __init__(self,parent = None):
        super().__init__()
        self.setReadOnly(True)
 
def display_txt_content(parent,txt):
    txt_viewers = TxtViewers()
    layout = parent.ui.reportsPage.layout()
    
    txt_viewers.setText(txt)
      
    # else:
    #     with olefile.OleFileIO(txt_path) as ole:
    #         if ole.exists("WordDocument"):
    #             data = ole.openstream("WordDocument").read()
    #             text = data.decode("utf-16", errors="ignore")
    #             text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
    #             txt_viewers.setText(text)
    #             ole.close()
                 #efekt wmiare podobny bez wykorzystania olefile
                 # with open(txt_path, "rb") as file:
                 # content = file.read() 
                 # text = content.decode("utf-16", errors="ignore")
                 # text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
                 # txt_viewers.setText(text)
            # else:
            #     return "Brak strumienia 'WordDocument' w pliku"
         # with olefile.OleFileIO(txt_path) as ole:
         #     if ole.exists("WordDocument"):
         #         data = ole.openstream("WordDocument").read()
         #         text = data.decode("utf-16", errors="ignore")
         #         text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
         #         txt_viewers.setText(text)
         #         ole.close()
         #         #efekt wmiare podobny bez wykorzystania olefile
         #         # with open(txt_path, "rb") as file:
         #         # content = file.read() 
         #         # text = content.decode("utf-16", errors="ignore")
         #         # text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
         #         # txt_viewers.setText(text)
         #     else:
        #return "Brak strumienia 'WordDocument' w pliku"
    #meta_data_system_file = MetaDataTableWiget(txt_path)
    view_cleaer(layout,parent)
    q_tab = parent.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget")
    tab_content = QWidget()
    tab_layout = QVBoxLayout(tab_content)
 
 
    #layoutRP = context.ui.rightMenu.layout()
    #layoutRP.addWidget(meta_data_system_file)
    layout.addWidget(txt_viewers)
    tab_layout.addWidget(txt_viewers)
    return tab_content
    
     
 
    
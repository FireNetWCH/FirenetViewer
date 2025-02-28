from PySide6.QtWidgets import QTextEdit
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget
import olefile
import re
import string
class TxtViewers (QTextEdit):
    def __init__(self,parent = None):
        super().__init__()
        self.setReadOnly(True)

def display_txt_content(context,txt_path,ext):
    txt_viewers = TxtViewers()
    layout = context.ui.reportsPage.layout()
    if (ext != ".doc") & (ext != ".doc"):
        try:
            with open(txt_path, "r", encoding="utf-8") as file:
                content = file.read()
                txt_viewers.setText(content)
        except Exception as e:
            print(f"ERROR TXT: {e}")
    else:
        with olefile.OleFileIO(txt_path) as ole:
            if ole.exists("WordDocument"):
                data = ole.openstream("WordDocument").read()
                text = data.decode("utf-16", errors="ignore")
                text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
                txt_viewers.setText(text)
                ole.close()
                #efekt wmiare podobny bez wykorzystania olefile
                # with open(txt_path, "rb") as file:
                # content = file.read() 
                # text = content.decode("utf-16", errors="ignore")
                # text = re.sub(r'[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s'+re.escape(string.punctuation)+']', '', text)
                # txt_viewers.setText(text)
            else:
                return "Brak strumienia 'WordDocument' w pliku"
    meta_data_system_file = MetaDataTableWiget(txt_path)
    view_cleaer(layout,context)
    layoutRP = context.ui.rightMenu.layout()
    layoutRP.addWidget(meta_data_system_file)
    layout.addWidget(txt_viewers)


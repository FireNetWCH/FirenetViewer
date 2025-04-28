from PySide6.QtWidgets import QVBoxLayout,QTableView,QTableWidget,QTableWidgetItem
import os
from PIL import Image
from PIL.ExifTags import TAGS
import time

def view_cleaer(layout,context):
    layout_rm = context.ui.rightMenu.layout()

    if layout_rm is None:
        layout_rm = QVBoxLayout(context.ui.rightMenu)
        context.ui.rightMenu.setLayout(layout_rm)
    for i in reversed(range(layout_rm.count())):
        widget_to_remove = layout_rm.itemAt(i).widget()
        widget_to_remove.deleteLater() 

    if layout is None:
        layout = QVBoxLayout(context.ui.reportsPage)
        context.ui.reportsPage.setLayout(layout)
    for i in reversed(range(layout.count())):
        widget_to_remove = layout.itemAt(i).widget()
        if (widget_to_remove.objectName() != "function_bar"):
            #widget_to_remove.setParent(None)
            widget_to_remove.deleteLater()   

def prev_item(self,path_now=str ):
    path_parts = path_now.split("/")
    if len(path_parts) > 1:
        file_path = path_parts[-1]
    else:
        file_path = path_parts[0]
    self.ui.pathLabel.setText(file_path)
    return path_now.replace("/"+file_path,"")

def get_image_metadata(image_path):
        image = Image.open(image_path)
        exif_data = image.getexif()
        if exif_data is not None:
            metadata = {}
            print(exif_data)
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if isinstance(value, bytes):
                    try:
                        value = value.decode(errors="ignore") 
                    except UnicodeDecodeError:
                        value = str(value)
                metadata[tag_name] = value
                print(metadata)
            return metadata
        else:
            return {"Brak metadanych":"Brak Danych"}

def get_system_metadata(file_path):
    file_matadata = os.stat(file_path)
    create_file = file_matadata.st_birthtime 
    last_modification = file_matadata.st_mtime
    size_file = file_matadata.st_size / (1024 * 3)
    last_used = file_matadata.st_atime
    owner = file_matadata.st_uid
    device = file_matadata.st_dev
    created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(create_file))
    modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modification))
    last_used_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_used))
    return {"Rozmiar":size_file,"Ostania modyfikacja":modified_time,"Utworzony":created_time,"Włąściciel":owner,"Urządenie":device,"Ostatnio urzywane": last_used_time}
   
class MetaDataTableWiget(QTableWidget):
    def __init__(self, path ,parent=None):
        super().__init__(parent)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Nazwa','Wartość'])
        dictionery_metadata = get_system_metadata(path)
        self.setRowCount(len(dictionery_metadata))
        for row, (tag, value) in enumerate(dictionery_metadata.items()):
                self.setItem(row, 0, QTableWidgetItem(str(tag)))
                self.setItem(row, 1, QTableWidgetItem(str(value)))


# funkcje obsługujące logike przycsków histori przeglądania
# def go_back(self):
#     from src.viewers.display_chenger import display_file_content
#     self.back_hisotry.append_history(self.histor.peek_history())
#     display_file_content(self, self.histor.seve_pop(), history_flag=0)

# def go_forward(self):
#     from src.viewers.display_chenger import display_file_content
#     self.histor.append_history(self.back_hisotry.peek_history()),  
#     display_file_content(self,self.back_hisotry.seve_pop(),history_flag=0)


class histor_stack():
    """Klasa do przechowywania chistori przeglądanych katalogów"""
    pass
#     def __init__(self):
#         self.stack = []

#     def append_history(self,item):
#         print(len(self.stack))
#         if len(self.stack) == 0:
#             self.stack.append(item)
#         elif item != self.peek_history():
#             if len(self.stack) <= 10: 
#                 self.stack.append(item)
#             else:
#                 self.stack.pop(0)
#                 self.stack.append(item)
                
#     def seve_pop(self):
#         print(len(self.stack))
#         if len(self.stack) > 1:
#             #self.stack.pop()
#             return self.stack.pop()
#         else:
#             return self.stack[0]
        
#     def peek_history(self):
#         return self.stack[len(self.stack)-1]
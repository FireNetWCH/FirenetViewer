from PySide6.QtWidgets import QVBoxLayout
from PIL import Image
from PIL.ExifTags import TAGS

def view_cleaer(layout,context):
    layout_rm = context.ui.rightMenu.layout()
    print(layout_rm)
    if layout_rm is None:
        layout_rm = QVBoxLayout(context.ui.rightMenu)
        context.ui.rightMenu.setLayout(layout_rm)
    for i in reversed(range(layout_rm.count())):
        widget_to_remove = layout_rm.itemAt(i).widget()
        if (widget_to_remove.objectName() != "function_bar"):
            #widget_to_remove.setParent(None)
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
    self.ui.label_11.setText(file_path)
    return path_now.replace("/"+file_path,"")

def go_back(self):
    from src.viewers.display_chenger import display_file_content
    self.back_hisotry.append_history(self.histor.peek_history())
    display_file_content(self, self.histor.seve_pop(), history_flag=0)

def go_forward(self):
    from src.viewers.display_chenger import display_file_content
    self.histor.append_history(self.back_hisotry.peek_history()),  
    display_file_content(self,self.back_hisotry.seve_pop(),history_flag=0)

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

class histor_stack():
    def __init__(self):
        self.stack = []

    def append_history(self,item):
        print(len(self.stack))
        if len(self.stack) == 0:
            self.stack.append(item)
        elif item != self.peek_history():
            if len(self.stack) <= 10: 
                self.stack.append(item)
            else:
                self.stack.pop(0)
                self.stack.append(item)
                
    def seve_pop(self):
        print(len(self.stack))
        if len(self.stack) > 1:
            #self.stack.pop()
            return self.stack.pop()
        else:
            return self.stack[0]
        
    def peek_history(self):
        return self.stack[len(self.stack)-1]
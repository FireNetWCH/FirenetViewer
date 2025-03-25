from PySide6.QtCore import QObject, Qt
from PySide6.QtCore import Qt, QEvent, QObject
class KeyPressFilter(QObject):
    def __init__(self, parent,callback,arrow_callback,multi_colback):
        super().__init__()
        self.parent_widget = parent  
        self.callback = callback
        self.arrow_colback = arrow_callback
        self.multi_colback = multi_colback
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Space:
                selected_indexes = self.parent_widget.selectedIndexes()
                selected_rows = set(index.row() for index in selected_indexes)
                selected_rows_list = list(selected_rows)
                if len(selected_rows_list) < 1: 
                    self.callback(selected_rows_list[0]) 
                else:
                    self.multi_colback(selected_rows_list)
                return True 
            elif event.key() == Qt.Key_Up:
                current_index = self.parent_widget.currentIndex()
                row = current_index.row()
                column = current_index.column()
                self.arrow_colback(row-1, column)
                return False
            elif event.key() == Qt.Key_Down:
                current_index = self.parent_widget.currentIndex()
                row = current_index.row()
                column = current_index.column()
                self.arrow_colback(row+1, column)
                return False
            if event.type() == 10:
                event.ignore()  
                return True
        
        return super().eventFilter(obj, event)
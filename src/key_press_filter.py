from PySide6.QtCore import QObject, Qt
from PySide6.QtCore import Qt, QEvent, QObject
class KeyPressFilter(QObject):
    def __init__(self, parent,callback,arrow_callback):
        super().__init__()
        self.parent_widget = parent  
        self.callback = callback
        self.arrow_colback = arrow_callback

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Space:
                current_index = self.parent_widget.currentIndex()
                row = current_index.row()
                column = current_index.column()
                self.callback(row, column)  
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
        return super().eventFilter(obj, event)
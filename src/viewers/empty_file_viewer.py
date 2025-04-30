from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout
from PySide6.QtCore import Qt

class EmptyFileView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("Ten plik jest pusty.")
        self.label.setAlignment(Qt.AlignCenter)  
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(20, 20, 20, 20) 
        self.setLayout(layout)
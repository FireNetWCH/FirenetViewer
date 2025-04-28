from PySide6.QtWidgets import QPushButton,QSizePolicy
from PySide6.QtGui import QIcon
from src.disc_image_reader.download_menager import download_manager

class downloadButton(QPushButton):
    def __init__(self,text,on_click_function = None ,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setText(f"{text}")
        self.setIcon(QIcon(":feather/icons/feather/download.png")) 
        if on_click_function:
            self.clicked.connect(on_click_function)
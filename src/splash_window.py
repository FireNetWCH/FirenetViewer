from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
class CustomSplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setFont(QFont("Arial", 12))
        self.loading_text = "Ładowanie..."

    def update_message(self, text):
        self.loading_text = text
        self.showMessage(self.loading_text, Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        self.repaint()
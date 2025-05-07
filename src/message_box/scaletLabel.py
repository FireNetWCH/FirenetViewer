from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ScalableLabel(QLabel):
    def __init__(self, image_path=None, parent=None):
        super().__init__(parent)
        self.original_pixmap = QPixmap(image_path) if image_path else None
        if self.original_pixmap:
            self.setPixmap(self.original_pixmap)
        self.setAlignment(Qt.AlignCenter)

    def setPixmap(self, pixmap):
        self.original_pixmap = pixmap
        scaled = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().setPixmap(scaled)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.original_pixmap:
            scaled = self.original_pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            super().setPixmap(scaled)

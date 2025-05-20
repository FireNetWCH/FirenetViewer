from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout
from PySide6.QtCore import Qt,QCoreApplication

class NotSupportFileView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel(QCoreApplication.translate("not_suppoet_file","Ten format pliku nie jest obsługiwany."))
        self.label.setAlignment(Qt.AlignCenter)  
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(20, 20, 20, 20) 
        self.setLayout(layout)
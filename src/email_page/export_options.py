from PySide6.QtWidgets import QVBoxLayout, QDialog,QRadioButton,QDialogButtonBox,QCheckBox
from PySide6.QtCore import QCoreApplication
class ExportSelector(QDialog):
    """Tworzy okno dialogowe zawierające opcje eksportu wiadomości email"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EKSPORTUJ WIADOMOŚCI: ")  
        
        layout = QVBoxLayout()

        self.radio1 = QRadioButton(QCoreApplication.translate("export_options","Wiadomości oznaczone flagami"))
        self.radio2 = QRadioButton(QCoreApplication.translate("export_options","Wiadomości spełniające aktualny filtr"))
        self.radio3 = QRadioButton(QCoreApplication.translate("export_options","Wiadomości zaznaczone"))
        self.radio1.setChecked(True)

        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        
        self.checkBox = QCheckBox(QCoreApplication.translate("export_options","Eksport załączników"),tristate=False,)
        self.checkBox.setChecked(True)
       
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.on_accepted)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.checkBox)
        layout.addWidget(self.buttons)
        
        self.setLayout(layout)

    def on_accepted(self):
        """Obsługuje kliknięcie przycisku OK"""
        
        if self.radio1.isChecked():
            selected_option = "1"
        elif self.radio2.isChecked():
            selected_option = "2"
        elif self.radio3.isChecked():
            selected_option = "3"
        
        is_checkBox_checked = self.checkBox.isChecked()
        
        self.selected_option = selected_option
        self.is_checkBox_checked = is_checkBox_checked

        self.accept()  

    def get_selected_option(self):
        """Zwraca wybraną opcję"""
        return getattr(self, 'selected_option', None)

    def get_checkBox_state(self):
        """Zwraca stan checkboxa"""
        return getattr(self, 'is_checkBox_checked', None)
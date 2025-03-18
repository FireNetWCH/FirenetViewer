
from PySide6.QtWidgets import (QPushButton,QDialog,QCalendarWidget, QVBoxLayout)

def get_selected_date(self):
        '''Tworzy okno z kalendarzem i zwraca wybraną datę.'''

        dialog = QDialog()
        dialog.setWindowTitle("Wybierz datę")
        layout = QVBoxLayout()
        calendar = QCalendarWidget()
        layout.addWidget(calendar)
        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Anuluj")
          
        def on_ok_clicked():
            dialog.accept()
            print(calendar.selectedDate())
            return calendar.selectedDate()

        def on_cancel_clicked():
            dialog.reject() 
            return None
        
        button_ok.clicked.connect(on_ok_clicked)
        button_cancel.clicked.connect(on_cancel_clicked)

        layout.addWidget(button_ok)
        layout.addWidget(button_cancel)

        dialog.setLayout(layout)
        result = dialog.exec()

        if result == QDialog.Accepted:
            return calendar.selectedDate()
        else:
            return None
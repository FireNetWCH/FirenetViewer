from PySide6.QtWidgets import (QPushButton, QDialog, QCalendarWidget, QVBoxLayout, QLabel)
from src.message_box import date_warning

class DateRangeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wybierz datę")
        self.layout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)
        
        self.label1 = QLabel("Wybierz początek zakresu")
        self.layout.addWidget(self.label1)
        self.label2 = QLabel("")
        self.layout.addWidget(self.label2)

        self.label3 = QLabel("Wybierz koniec zakresu")
        self.layout.addWidget(self.label3)
        self.label4 = QLabel("")
        self.layout.addWidget(self.label4)

        self.button_ok = QPushButton("OK")
        self.button_cancel = QPushButton("Anuluj")

        self.layout.addWidget(self.button_ok)
        self.layout.addWidget(self.button_cancel)
        self.setLayout(self.layout)

        self.first = True  # Flaga do przełączania pomiędzy label2 i label4
        self.calendar.selectionChanged.connect(self.setLabelData)
        
        self.label1.mousePressEvent = self.selectLabel3
        self.label3.mousePressEvent = self.selectLabel4

        self.button_ok.clicked.connect(self.validate_dates)
        self.button_cancel.clicked.connect(self.reject)

    def setLabelData(self):
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        if self.first:
            self.label2.setText(selected_date)
        else:
            self.label4.setText(selected_date)
    
    def selectLabel3(self, event):
        self.first = True
        self.label2.setStyleSheet("border: 2px solid blue;")
        self.label4.setStyleSheet("")
    
    def selectLabel4(self, event):
        self.first = False
        self.label4.setStyleSheet("border: 2px solid blue;")
        self.label2.setStyleSheet("")

    def get_selected_dates(self):
        if self.exec() == QDialog.Accepted:
            return self.label2.text(), self.label4.text()
        return None, None

    def validate_dates(self):
        start_date = self.label2.text()
        end_date = self.label4.text()
        if start_date and end_date and start_date > end_date:
            date_warning.rights_date_wornig()  
        else:
            self.accept()

from PySide6.QtWidgets import (QPushButton, QDialog, QCalendarWidget, QVBoxLayout, QLabel,QHBoxLayout)
from PySide6.QtGui import (QTextCharFormat, QColor)
from PySide6.QtCore import (QDate)
from src.message_box import date_warning

class DateRangeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wybierz datę")
        self.layout = QVBoxLayout()
        self.calendar_layout = QHBoxLayout()
        self.last_data_start = QDate()
        self.last_data_end = QDate()

        self.fmt = QTextCharFormat()
        self.fmt.setBackground(QColor("#4f88ca"))
        self.fmt.setForeground(QColor("4f88ca"))

        self.fmt2 = QTextCharFormat()
        self.fmt2.setBackground(QColor("white"))
        self.fmt2.setForeground(QColor("white"))

        self.calendar1 = QCalendarWidget()
#         self.calendar1.setStyleSheet("""{background-color: #FFFFFF;
#     border: 1px solid #D8D8D8;
#     border-radius: 4px; }
#   """)
        self.label1 = QLabel("Wybierz początek zakresu")
        self.label2 = QLabel("")

        self.calendar2 = QCalendarWidget()
        self.label3 = QLabel("Wybierz koniec zakresu")
        self.label4 = QLabel("")

        self.calendar_layout.addWidget(self.calendar1)
        self.calendar_layout.addWidget(self.calendar2)

        
        self.labels_layout = QHBoxLayout()
        self.labels_layout.addWidget(self.label1)
        self.labels_layout.addWidget(self.label2)
        self.labels_layout.addWidget(self.label3)
        self.labels_layout.addWidget(self.label4)

        self.layout.addLayout(self.calendar_layout)
        self.layout.addLayout(self.labels_layout)

        self.button_ok = QPushButton("OK")
        self.button_clear = QPushButton("Wyczść daty")
        self.button_cancel = QPushButton("Anuluj")

        self.layout.addWidget(self.button_ok)
        self.layout.addWidget(self.button_clear)
        self.layout.addWidget(self.button_cancel)

        self.setLayout(self.layout)

        self.first = True 
        
        self.calendar1.selectionChanged.connect(self.setLabelData1)
        self.calendar2.selectionChanged.connect(self.setLabelData2)

        self.button_ok.clicked.connect(self.validate_dates)
        self.button_clear.clicked.connect(self.cleae_data)

    def cleae_data(self):
        self.label2.setText("")
        self.label4.setText("")
        self.label2.setStyleSheet("background-color: #ffffff")
        self.label4.setStyleSheet("background-color: #ffffff")
    def setLabelData1(self):
        if self.last_data_start is not None:
            self.calendar1.setDateTextFormat(self.last_data_start, self.fmt2)
        selected_date = self.calendar1.selectedDate().toString("yyyy-MM-dd")
        self.label2.setText(selected_date)
        self.label2.setStyleSheet("background-color: #4f88ca")
        current_date = QDate.currentDate()
        selected_date = self.calendar1.selectedDate()
        while  selected_date < current_date:
            self.calendar1.setDateTextFormat(selected_date, self.fmt)
            selected_date = selected_date.addDays(1)
        self.calendar1.setDateTextFormat(self.calendar1.selectedDate(), self.fmt)

    def setLabelData2(self):
        if self.last_data_start is not None:
            self.calendar2.setDateTextFormat(self.last_data_start, self.fmt2)
        selected_date = self.calendar2.selectedDate().toString("yyyy-MM-dd")
        self.label4.setText(selected_date)
        self.label4.setStyleSheet("background-color: #4f88ca")

        #current_date = QDate.currentDate()
        current_date = QDate(1990, 1, 1)
        selected_date = self.calendar2.selectedDate()

        while current_date  < selected_date:
            self.calendar2.setDateTextFormat(current_date, self.fmt)
            current_date = current_date.addDays(1)



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

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QCoreApplication

def left_date_wornig():
    '''Funkca wyświetla okno dialogowe z komuniektem:
      "Data poczotkowa nie może \nbyć datą pużniejszą niż końcowa" '''
    msgBox = QMessageBox()
    msgBox.setText(QCoreApplication.translate("date_warning","Data poczotkowa nie może \nbyć datą pużniejszą niż końcowa"))
    msgBox.exec()

def rights_date_wornig():
    '''Funkca wyświetla okno dialogowe z komuniektem:
      "Data końcowa nie może \nbyć datą wcześniejszą niż data początkowa" '''
    msgBox = QMessageBox()
    msgBox.setText(QCoreApplication.translate("date_warning","Data końcowa nie może \nbyć datą wcześniejszą niż data początkowa"))
    msgBox.exec()

def add_labels_worning():
    '''Funkca wyświetla okno dialogowe z komuniektem:
      "Etykieta dodana do bazy danych" '''
    msgBox = QMessageBox()
    msgBox.setText(QCoreApplication.translate("date_warning", "Labelka dodana do bazy danych"))
    msgBox.exec()
    
from PySide6.QtWidgets import QMessageBox
def left_date_wornig():
    '''Funkca wyświetla okno dialogowe z komuniektem:
      "Data poczotkowa nie może \nbyć datą pużniejszą niż końcowa" '''
    msgBox = QMessageBox()
    msgBox.setText("Data poczotkowa nie może \nbyć datą pużniejszą niż końcowa")
    msgBox.exec()

def rights_date_wornig():
    '''Funkca wyświetla okno dialogowe z komuniektem:
      "Data końcowa nie może \nbyć datą wcześniejszą niż data początkowa" '''
    msgBox = QMessageBox()
    msgBox.setText("Data końcowa nie może \nbyć datą wcześniejszą niż data początkowa")
    msgBox.exec()
    
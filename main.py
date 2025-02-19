import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.functions import GUIFunctions
from src.ui_interface import Ui_MainWindow
from Custom_Widgets import *
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from Custom_Widgets.QAppSettings import QAppSettings

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})
        self.show()
        QAppSettings.updateAppSettings(self)
        self.app_functions = GUIFunctions(self)

    def scssCompilationProgress(self, n: int) -> None:
        self.ui.activityProgress.setValue(n)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

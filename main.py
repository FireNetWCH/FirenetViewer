import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide6.QtCore import Slot
from src.functions import GUIFunctions
from src.ui_interface import Ui_MainWindow
from Custom_Widgets import *
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from Custom_Widgets.QAppSettings import QAppSettings

 
import os
import _icons_rc
def get_resource_path(relative_path):
    """Zwraca poprawną ścieżkę do zasobów, obsługując tryb onefile"""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS  
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        json_style_path = get_resource_path("json-styles/style.json")
        loadJsonStyle(self, self.ui, jsonFiles={json_style_path})

        self.show()
        QAppSettings.updateAppSettings(self,generateIcons=False,reloadJson=False)
        self.app_functions = GUIFunctions(self)

    def scssCompilationProgress(self, n: int) -> None:
        self.ui.activityProgress.setValue(n)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # pixmap = QPixmap("logo.jpg") 
    # splash = CustomSplashScreen(pixmap)
    # splash.show()
    # app.processEvents()
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="top-center",duration=1000)
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    if getattr(sys, 'frozen', False):
        import pyi_splash
        if getattr(sys, 'frozen', False):
            pyi_splash.close()
    
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.functions import GUIFunctions
from src.ui_interface import Ui_MainWindow
from Custom_Widgets import *
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from Custom_Widgets.QAppSettings import QAppSettings
from PySide6.QtCore import QtMsgType, qInstallMessageHandler
import datetime

import _icons_rc

def qt_message_handler(mode, context, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg_type = {
        QtMsgType.QtDebugMsg: "DEBUG",
        QtMsgType.QtInfoMsg: "INFO",
        QtMsgType.QtWarningMsg: "WARNING",
        QtMsgType.QtCriticalMsg: "CRITICAL",
        QtMsgType.QtFatalMsg: "FATAL"
    }.get(mode, "UNKNOWN")

    full_message = f"[{timestamp}] {msg_type}: {message}"
    print(full_message)
    with open("qt_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(full_message + "\n")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})
        #self.show()
        QAppSettings.updateAppSettings(self,generateIcons=False,reloadJson=False)
        self.app_functions = GUIFunctions(self)
        
if __name__ == "__main__":
    qInstallMessageHandler(qt_message_handler)
    app = QApplication(sys.argv)
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="top-center",duration=1000)
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

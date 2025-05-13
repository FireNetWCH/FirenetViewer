import src.db_function.pc_db as pc_db
from PySide6.QtWidgets import QTableWidgetItem,QTableWidget, QHeaderView
from PySide6.QtCore import Qt,QTimer

from typing import Any, List, Dict, Optional
from urllib.parse import urlparse
from datetime import datetime
from PySide6.QtGui import QStandardItemModel, QStandardItem
from src.db_function.export_file_db import database_file_export_menager
class export_file_browser:
    def __init__(self,parent ,db_menager : database_file_export_menager):
        self.db_menager = db_menager
        self.parent = parent
        self.focus_file_type = None
        self.table_dict : Dict[str, str] = {}

    def get_branch_tree_list(self):
        table_list = self.db_menager.get_all_table_list()
        branch_list = []
        other_file = False
        for table_name in table_list:
            print(table_name[0])
            if table_name[0] == "exported_audio":
                branch_list.append("Audio")
                self.table_dict["Audio"] = table_name[0]
            elif table_name[0] == "exported_docs":
                branch_list.append("Dokunty")
                self.table_dict["Dokunty"] = table_name[0]
            elif table_name[0] == "exported_videos":
                branch_list.append("Wideo")
                self.table_dict["Wideo"] = table_name[0]
            elif table_name[0] == "exported_pdfs":
                branch_list.append("Pliki PDF")
                self.table_dict["Pliki PDF"] = table_name[0]
            elif table_name[0] == "exported_sheets":
                branch_list.append("Arkusze kalkulacyjne")
                self.table_dict["Arkusze kalkulacyjne"] = table_name[0]
            elif table_name[0] == ("exported_images"):
                branch_list.append("Obrazy")
                self.table_dict["Obrazy"] = table_name[0]
            elif table_name[0] == "exported_presentations":
                branch_list.append("Prezentacjie")
                self.table_dict["Prezentacjie"] = table_name[0]
            elif other_file == False:
                branch_list.append("Pozostałe")
                self.table_dict["Pozostałe"] = table_name[0]
                other_file = True
        return branch_list
    
    def load_exported_file(self):
        rows = self.db_menager.get_contents_from_table(self.table_dict[self.focus_file_type])
        self.parent.ui.ExportFileTableWidget.setRowCount(0)
        self.parent.ui.ExportFileTableWidget.setColumnCount(0)
        self.parent.ui.ExportFileTableWidget.setColumnCount(4)

        self.parent.ui.ExportFileTableWidget.setHorizontalHeaderLabels(["Id","Nazwa Pliku","Rozmiar","Data utworzenia"])
       
        for row in rows:
            row_position = self.parent.ui.ExportFileTableWidget.rowCount()
            self.parent.ui.ExportFileTableWidget.insertRow(row_position)
            for i, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.parent.ui.ExportFileTableWidget.setItem(row_position, i, item)
        self.parent.ui.ExportFileTableWidget.cellClicked.connect(lambda : print("click"))
        self.parent.ui.ExportFileTableWidget.verticalHeader().setVisible(False)                
        self.parent.ui.ExportFileTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
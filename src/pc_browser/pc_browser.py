import src.db_function.pc_db as pc_db
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt

class pc_browser:
    def __init__(self,name,prent,db_menager):
        self.db_menager = db_menager
        self.pc_name = name
        self.parent = prent
        
    def load_device_info(self):
        self.parent.ui.deviceInfoTableWidget.setRowCount(0)
        self.parent.ui.deviceInfoTableWidget.setColumnCount(0)
        self.parent.ui.deviceInfoTableWidget.setColumnCount(3)
        self.parent.ui.deviceInfoTableWidget.setHorizontalHeaderLabels(["Nazwa", "Wartość", "Typ"])
        self.parent.ui.deviceInfoTableWidget.setColumnWidth(0, 200)
        self.parent.ui.deviceInfoTableWidget.setColumnWidth(1, 200)
        self.parent.ui.deviceInfoTableWidget.setColumnWidth(2, 100)

        
        rows = self.db_menager.get_device_info()
        if rows:
            print(rows)
            for row in rows:
                print(row)
                row_position = self.parent.ui.deviceInfoTableWidget.rowCount()
                self.parent.ui.deviceInfoTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.parent.ui.deviceInfoTableWidget.setItem(row_position, i, item)
    
    def load_software_info(self):
        self.parent.ui.softwareInfoTableWidget.setRowCount(0)
        self.parent.ui.softwareInfoTableWidget.setColumnCount(0)
        self.parent.ui.softwareInfoTableWidget.setColumnCount(3)
        self.parent.ui.softwareInfoTableWidget.setHorizontalHeaderLabels(["Nazwa", "Wartość", "Typ"])
        self.parent.ui.softwareInfoTableWidget.setColumnWidth(0, 200)
        self.parent.ui.softwareInfoTableWidget.setColumnWidth(1, 200)
        self.parent.ui.softwareInfoTableWidget.setColumnWidth(2, 100)

        
        rows = self.db_menager.get_software_info()
        if rows:
            print(rows)
            for row in rows:
                print(row)
                row_position = self.parent.ui.softwareInfoTableWidget.rowCount()
                self.parent.ui.softwareInfoTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.parent.ui.softwareInfoTableWidget.setItem(row_position, i, item)

    def load_network_config(self):
        self.parent.ui.networkConfigTableWidget.setRowCount(0)
        self.parent.ui.networkConfigTableWidget.setColumnCount(0)
        self.parent.ui.networkConfigTableWidget.setColumnCount(4)
        self.parent.ui.networkConfigTableWidget.setHorizontalHeaderLabels(["Id","Nazwa", "Wartość", "Typ"])
        self.parent.ui.networkConfigTableWidget.setColumnWidth(0, 200)
        self.parent.ui.networkConfigTableWidget.setColumnWidth(1, 200)
        self.parent.ui.networkConfigTableWidget.setColumnWidth(2, 100)
        self.parent.ui.networkConfigTableWidget.setColumnWidth(3, 100)

        
        rows = self.db_menager.get_network_config()
        if rows:
            for row in rows:
                row_position = self.parent.ui.networkConfigTableWidget.rowCount()
                self.parent.ui.networkConfigTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.parent.ui.networkConfigTableWidget.setItem(row_position, i, item)

    def load_installed_software(self):
        self.parent.ui.installedSoftwareTableWidget.setRowCount(0)
        self.parent.ui.installedSoftwareTableWidget.setColumnCount(0)
        self.parent.ui.installedSoftwareTableWidget.setColumnCount(3)
        self.parent.ui.installedSoftwareTableWidget.setHorizontalHeaderLabels(["Nazwa", "Wartość", "Typ"])
        self.parent.ui.installedSoftwareTableWidget.setColumnWidth(0, 200)
        self.parent.ui.installedSoftwareTableWidget.setColumnWidth(1, 200)
        self.parent.ui.installedSoftwareTableWidget.setColumnWidth(2, 100)

        
        rows = self.db_menager.get_instaled_software()
        if rows:
            for row in rows:
                row_position = self.parent.ui.installedSoftwareTableWidget.rowCount()
                self.parent.ui.installedSoftwareTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.parent.ui.installedSoftwareTableWidget.setItem(row_position, i, item)
    
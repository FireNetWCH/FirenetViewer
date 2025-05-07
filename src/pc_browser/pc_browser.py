import src.db_function.pc_db as pc_db
from PySide6.QtWidgets import QTableWidgetItem,QTableWidget, QHeaderView
from PySide6.QtCore import Qt
import tldextract
from urllib.parse import urlparse
from datetime import datetime
from PySide6.QtGui import QStandardItemModel, QStandardItem
from src.db_function.pc_db import database_pc_manager
class pc_browser:
    def __init__(self,name,prent ,db_menager : database_pc_manager):
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
            for row in rows:
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
    
    def load_borowser_download_history(self, browser_name):
        rows = self.db_menager.get_url_paths_from_browsers("google_chrome_downloads")

        self.parent.ui.networkBrowserTable.setRowCount(0)
        self.parent.ui.networkBrowserTable.setColumnCount(0)
        self.parent.ui.networkBrowserTable.setColumnCount(3)
        self.parent.ui.networkBrowserTable.setHorizontalHeaderLabels(["id","Domena", "Nazwa pliku"])
        if rows:
            for row in rows:
                row_position = self.parent.ui.networkBrowserTable.rowCount()
                self.parent.ui.networkBrowserTable.insertRow(row_position)
                for i, value in enumerate(row):
                    if i == 0:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.networkBrowserTable.setItem(row_position, i, item)
                    if i == 1:
                        if value is not None:
                            sufix = tldextract.extract(value).suffix
                            #subdomain = tldextract.extract(value).subdomain
                            domein = tldextract.extract(value).domain
                            item = QTableWidgetItem(str(f"{domein}.{sufix}"))
                            self.parent.ui.networkBrowserTable.setItem(row_position, i, item)
                    if i ==2 :
                        if value is not None:
                            file_name = value.split("\\")[-1]
                            item = QTableWidgetItem(str(file_name))
                            self.parent.ui.networkBrowserTable.setItem(row_position, i, item) 
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Interactive)                   
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Interactive)
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.parent.ui.networkBrowserTable.cellClicked.connect(self.load_download_deteils)

    def load_download_deteils(self, row, column):
        id = self.parent.ui.networkBrowserTable.item(row, 0).text()
        rows = self.db_menager.get_download_deteils("google_chrome_downloads",id)
        if rows:
            if rows[0][1] is not None:
                self.parent.ui.urlLabel.setText(str(rows[0][1]))
            else:
                self.parent.ui.urlLabel.setText("Brak URL")
            if rows[0][2] is not None:
                self.parent.ui.pathDownloadLabel.setText(str(rows[0][2]))
            else:
                self.parent.ui.pathDownloadLabel.setText("Brak ścieżki")
            if rows[0][3] is not None:
                kilobajty = int(rows[0][3]) / 8 / 1024
                self.parent.ui.sizeFileLabel.setText(f"{kilobajty:.2f} KB")
            else:
                self.parent.ui.sizeFileLabel.setText("Brak rozmiaru")
            if rows[0][4] is not None:
                self.parent.ui.startTimeLabel.setText(str(rows[0][4]))
            else:
                self.parent.ui.startTimeLabel.setText("Brak czasu rozpoczęcia")
            if rows[0][5] is not None:
                self.parent.ui.endTimeLabel.setText(str(rows[0][5]))
            else:
                self.parent.ui.endTimeLabel.setText("Brak czasu zakończenia")
            if rows[0][4] is not None and rows[0][5] is not None:
                fmt = "%Y-%m-%d %H:%M:%S"
                start_time = datetime.strptime(rows[0][4], fmt)
                end_time = datetime.strptime(rows[0][5], fmt)
                self.parent.ui.downloadTimeLabel.setText(str(end_time - start_time))
            else:
                self.parent.ui.downloadTimeLabel.setText("Brak czasu pobierania")
            
            #self.parent.ui.downloadDetailsTableWidget.setItem(row_position, i, item)

    def load_history_browser(self):

        self.parent.ui.historyBrowserTablet.setRowCount(0)
        self.parent.ui.historyBrowserTablet.setColumnCount(0)
        self.parent.ui.historyBrowserTablet.setColumnCount(9)
        self.parent.ui.historyBrowserTablet.setHorizontalHeaderLabels(["Id","Domena","Tytuł","Liczba Wizyt","Data Wizyty","Profil","Urzytkownik","Przeglądarka"])
        #print(self.db_menager.get_history_browser_list())
        rows = self.db_menager.get_history_browser_from_all_browser(self.db_menager.get_history_browser_list(),self.parent.history_browser_filters,self.parent.history_browser_marge_filters,100000000,0)

        for row in rows:
            #print(row)
            row_position = self.parent.ui.historyBrowserTablet.rowCount()
            self.parent.ui.historyBrowserTablet.insertRow(row_position)
            for i, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.parent.ui.historyBrowserTablet.setItem(row_position, i, item)
                if i == 1:
                    parsed = urlparse(value)   
                    if parsed.scheme in ('http', 'https', 'ftp'):
                        sufix = tldextract.extract(value).suffix
                        domein = tldextract.extract(value).domain
                        item = QTableWidgetItem(str(f"{domein}.{sufix}"))
                        self.parent.ui.historyBrowserTablet.setItem(row_position, i, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.historyBrowserTablet.setItem(row_position, i, item)
        self.parent.ui.historyBrowserTablet.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        for i in range(self.parent.ui.historyBrowserTablet.columnCount()):
            if i != 2:
                self.parent.ui.historyBrowserTablet.resizeColumnToContents(i)
        self.parent.ui.historyBrowserTablet.cellClicked.connect(self.load_history_deteils)
        self.parent.ui.historyBrowserTablet.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)


    def load_history_deteils(self, row, column):
        id = self.parent.ui.historyBrowserTablet.item(row, 0).text()
        browser_name = self.parent.ui.historyBrowserTablet.item(row,7).text()
        browser_name = browser_name.lower()
        browser_name = browser_name.replace(" ","_")
        rows = self.db_menager.get_history_deteils(browser_name+"_history",id)
        if rows:
            if rows[0][6] is not None:
                self.parent.ui.profileNameLabel.setText(str(rows[0][6]))
            else:
                self.parent.ui.profileNameLabel.setText("Brak nazwy profilu")
            if rows[0][1] is not None:
                self.parent.ui.historyUrlLabel.setText(str(rows[0][1]))
            else:
                self.parent.ui.historyUrlLabel.setText("Brak URL")
            if rows[0][2] is not None:
                self.parent.ui.titleTabLabel.setText(str(rows[0][2]))
            else:
                self.parent.ui.titleTabLabel.setText("Brak tytułu")
            if rows[0][4] is not None:
                self.parent.ui.dateVisitLabel.setText(str(rows[0][4]))
            else:
                self.parent.ui.dateVisitLabel.setText("Brak daty wizyty")
            if rows[0][5] is not None:
                self.parent.ui.lastVisitLabel.setText(str(rows[0][5]))
            else:
                self.parent.ui.lastVisitLabel.setText("Brak ostatniej wizyty")
            if rows[0][3] is not None:
                self.parent.ui.countVisit.setText(str(rows[0][3]))
            else:
                self.parent.ui.countVisit.setText("Brak liczby wizyt")

    def generate_pc_tree(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Zawartość systemu"])

        hisotry_browser_liset = self.db_menager.get_history_browser_list()
        
        browser_branch = []

        if hisotry_browser_liset:
            browser_branch.append("Historia przegladarek")

        data = {
            "Informacje o urządzeniu": ["Wiinformacje o Systemie", "Połączenia Sieciowe", "GPU"],
            "Przeglądarki": browser_branch,
            "Pliki wyeksportowane": ["Pliki graficzne", "Pliki Wide", "json"]
        }

        for global_name, sub_items in data.items():
                item = QStandardItem(global_name)
                for sub_item in sub_items:
                    item_pod = QStandardItem(sub_item)
                    item.appendRow(item_pod)
                model.appendRow(item)

        self.parent.ui.centerMenuPages.setCurrentIndex(5)
        self.parent.ui.pcTree.setModel(model)
        self.parent.ui.pcTree.expandAll()
        self.parent.ui.pcTree.clicked.connect(self.on_tree_item_clicked)

    def on_tree_item_clicked(self, index):
        print("Clicked item index:", index)
        item = self.parent.ui.pcTree.model().itemFromIndex(index)
        if item is not None:
            item_name = item.text()
            print("Clicked item name:", item_name)
            if item_name == "Historia przegladarek":
                self.parent.ui.customQStackedWidget.setCurrentIndex(8)
                self.db_menager.get_history_browser_from_all_browser(self.db_menager.get_history_browser_list(),self.parent.history_browser_filters,self.parent.history_browser_marge_filters,100000000,0)
            elif item_name == "Wiinformacje o Systemie":
                self.parent.ui.customQStackedWidget.setCurrentIndex(4)
                self.load_device_info()
    
    def set_item_combo_box(self, list_values,combo_box):
        combo_box.clear()
        combo_box.addItem("Wszystkie",0)
        if list_values:
            for value in list_values:
                combo_box.addItem(value[1],value[0])
    
    def generate_sercher_history_browser_combo_box(self):
        browser_list = self.db_menager.get_detected_browsers()
        broweser_combo_box_list = []
        for i in range(len(browser_list)):
            broweser_combo_box_list.append((browser_list[i][0],browser_list[i][1]))

        user_list = self.db_menager.get_all_os_users()
        user_combo_box_list = []
        for i in range(len(user_list)):
                if user_list[i][2] != "" and user_list[i][2] is not None:
                    user_combo_box_list.append((user_list[i][0],user_list[i][2]))
                elif user_list[i][1] != "" and user_list[i][1] is not None:
                        user_combo_box_list.append((user_list[i][0],user_list[i][1]))
                
        profile_list = self.db_menager.get_detected_browsers()
        profile_combo_box_list = []
        seen = set()
        for i in range(len(profile_list)):
            if profile_list[i][2] not in seen :
                seen.add(profile_list[i][2]) 
                profile_combo_box_list.append((profile_list[i][0],profile_list[i][2]))
        
        self.set_item_combo_box(profile_combo_box_list,self.parent.ui.profileComboBox)
        self.set_item_combo_box(broweser_combo_box_list,self.parent.ui.browserComboBox)
        self.set_item_combo_box(user_combo_box_list,self.parent.ui.userComboBox)
        
        print(user_list)



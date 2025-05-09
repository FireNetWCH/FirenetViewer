import src.db_function.pc_db as pc_db
from PySide6.QtWidgets import QTableWidgetItem,QTableWidget, QHeaderView
from PySide6.QtCore import Qt,QTimer
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
    
    def load_borowser_download_history(self):
        rows = self.db_menager.get_download_history_browser_from_all_browser(self.db_menager.get_browser_table_type_list("_downloads"),self.parent.history_download_browser_filters,self.parent.history_browser_marge_filters,100000000,0)

        self.parent.ui.networkBrowserTable.setRowCount(0)
        self.parent.ui.networkBrowserTable.setColumnCount(0)
        self.parent.ui.networkBrowserTable.setColumnCount(7)
        self.parent.ui.networkBrowserTable.setHorizontalHeaderLabels(["id","Domena", "Nazwa pliku","Data","Profil","Urzytkownik","Przeglądarka"])
        if rows:
            for row in rows:
                row_position = self.parent.ui.networkBrowserTable.rowCount()
                self.parent.ui.networkBrowserTable.insertRow(row_position)
                for i, value in enumerate(row):
                    
                    if i == 1:
                        if value is not None:
                            sufix = tldextract.extract(value).suffix
                            #subdomain = tldextract.extract(value).subdomain
                            domein = tldextract.extract(value).domain
                            item = QTableWidgetItem(str(f"{domein}.{sufix}"))
                            self.parent.ui.networkBrowserTable.setItem(row_position, i, item)
                    elif i ==2 :
                        if value is not None:
                            file_name = value.split("\\")[-1]
                            item = QTableWidgetItem(str(file_name))
                            self.parent.ui.networkBrowserTable.setItem(row_position, i, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.networkBrowserTable.setItem(row_position, i, item)
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Interactive)                   
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Interactive)
        self.parent.ui.networkBrowserTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.parent.ui.networkBrowserTable.cellClicked.connect(self.load_download_deteils)
        self.parent.ui.networkBrowserTable.verticalHeader().setVisible(False)

    def load_download_deteils(self, row, column):
        id = self.parent.ui.networkBrowserTable.item(row, 0).text()
        browser_name = self.parent.ui.networkBrowserTable.item(row,6).text()
        browser_name = browser_name.lower()
        browser_name = browser_name.replace(" ","_")
        rows = self.db_menager.get_download_deteils(browser_name+"_downloads",id)
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
        rows = self.db_menager.get_history_browser_from_all_browser(self.db_menager.get_browser_table_type_list("_history"),self.parent.history_browser_filters,self.parent.history_browser_marge_filters,100000000,0)

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
                        stripped_value = value.removeprefix(f"{parsed.scheme}://")
                        item = QTableWidgetItem(str(stripped_value))
                        self.parent.ui.historyBrowserTablet.setItem(row_position, i, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.historyBrowserTablet.setItem(row_position, i, item)
        self.parent.ui.historyBrowserTablet.cellClicked.connect(self.load_history_deteils)
        self.parent.ui.historyBrowserTablet.verticalHeader().setVisible(False)                
        for i in range(self.parent.ui.historyBrowserTablet.columnCount()):
            if i != 1:
                self.parent.ui.historyBrowserTablet.resizeColumnToContents(i)
        self.parent.ui.historyBrowserTablet.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.parent.ui.historyBrowserTablet.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        def enable_column_resize():
            self.parent.ui.historyBrowserTablet.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        QTimer.singleShot(0, enable_column_resize)

        

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
                self.parent.ui.historyWebEngineView.load(str(rows[0][1]))
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

        hisotry_browser_liset = self.db_menager.get_browser_table_type_list("_history")
        download_history_list = self.db_menager.get_browser_table_type_list("_downloads")
        save_login = self.db_menager.get_browser_table_type_list("_logins")
        sercher_list = self.db_menager.get_browser_table_type_list("_searchhistory")
        autofill_list = self.db_menager.get_browser_table_type_list("_autofill")
        browser_branch = []

        if hisotry_browser_liset:
            browser_branch.append("Historia przegladarek")
        if download_history_list:
            browser_branch.append("Historia pobierania")
        if save_login:
            browser_branch.append("Zapisane loginy w przeglądarkach")
        if sercher_list:
            browser_branch.append("Historia wyszukiwania")
        if autofill_list:
            browser_branch.append("Zapisane dane autouzupełniania")
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
                self.db_menager.get_history_browser_from_all_browser(self.db_menager.get_browser_table_type_list("_history"),self.parent.history_browser_filters,self.parent.history_browser_marge_filters,100000000,0)
            elif item_name == "Wiinformacje o Systemie":
                self.parent.ui.customQStackedWidget.setCurrentIndex(4)
                self.load_device_info()
            elif item_name == "Historia pobierania":
                self.parent.ui.customQStackedWidget.setCurrentIndex(5)
                self.db_menager.get_download_history_browser_from_all_browser(self.db_menager.get_browser_table_type_list("_downloads"),self.parent.history_download_browser_filters,self.parent.history_browser_marge_filters,100000000,0)
            elif item_name == "Zapisane loginy w przeglądarkach":
                self.parent.ui.customQStackedWidget.setCurrentIndex(9)
                self.load_save_login()
            elif item_name == "Historia wyszukiwania":
                self.parent.ui.customQStackedWidget.setCurrentIndex(10)
                self.load_sercher()
            elif item_name == "Zapisane dane autouzupełniania":
                self.parent.ui.customQStackedWidget.setCurrentIndex(11)
                self.load_autofill()
    
    def set_item_combo_box(self, list_values,combo_box):
        combo_box.clear()
        combo_box.addItem("Wszystkie",0)
        if list_values:
            for value in list_values:
                combo_box.addItem(value[1],value[0])
    
    def generate_sercher_history_browser_combo_box(self,profil_box, browser_box, user_box):
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
        
        self.set_item_combo_box(profile_combo_box_list,profil_box)
        self.set_item_combo_box(broweser_combo_box_list,browser_box)
        self.set_item_combo_box(user_combo_box_list,user_box)

    def load_save_login(self):
        rows = self.db_menager.get_all_save_logins(self.db_menager.get_browser_table_type_list("_logins"),self.parent.save_login_filters,self.parent.history_browser_marge_filters,100000000,0)

        self.parent.ui.saveLoginTableWidget.setRowCount(0)
        self.parent.ui.saveLoginTableWidget.setColumnCount(0)
        self.parent.ui.saveLoginTableWidget.setColumnCount(7)
        self.parent.ui.saveLoginTableWidget.setHorizontalHeaderLabels(["id","Domena", "Login","Data","Profil","Urzytkownik","Przeglądarka"])
        if rows:
            for row in rows:
                row_position = self.parent.ui.saveLoginTableWidget.rowCount()
                self.parent.ui.saveLoginTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    
                    if i == 1:
                        if value is not None:
                            sufix = tldextract.extract(value).suffix
                            #subdomain = tldextract.extract(value).subdomain
                            domein = tldextract.extract(value).domain
                            item = QTableWidgetItem(str(f"{domein}.{sufix}"))
                            self.parent.ui.saveLoginTableWidget.setItem(row_position, i, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.saveLoginTableWidget.setItem(row_position, i, item)
        self.parent.ui.saveLoginTableWidget.cellClicked.connect(self.load_logins_deteils)
        self.parent.ui.saveLoginTableWidget.verticalHeader().setVisible(False)
        self.parent.ui.saveLoginTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        for i in range(self.parent.ui.saveLoginTableWidget.columnCount()):
            if i != 1 or i != 2:
                self.parent.ui.saveLoginTableWidget.resizeColumnToContents(i)
        self.parent.ui.saveLoginTableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.parent.ui.saveLoginTableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
    def load_logins_deteils(self, row, column):
        id = self.parent.ui.saveLoginTableWidget.item(row, 0).text()
        browser_name = self.parent.ui.saveLoginTableWidget.item(row,6).text()
        browser_name = browser_name.lower()
        browser_name = browser_name.replace(" ","_")
        rows = self.db_menager.get_logins_deteils(browser_name+"_logins",id)
        if rows:
            print(rows)
            if rows[0][1] is not None:
                self.parent.ui.saveLoginUrlLabel.setText(str(rows[0][1]))
            else:
                self.parent.ui.saveLoginUrlLabel.setText("Brak adresu URL")
            if rows[0][2] is not None:
                self.parent.ui.loginLabel.setText(str(rows[0][2]))
            else:
                self.parent.ui.loginLabel.setText("Brak zapisanego loginu")
            if rows[0][3] is not None:
                self.parent.ui.lastDateUseLabel.setText(str(rows[0][3]))
            else:
                self.parent.ui.lastDateUseLabel.setText("Brak ostatniej dayty wizyty")

    def load_sercher(self):
        rows = self.db_menager.get_all_seracher(self.db_menager.get_browser_table_type_list("_searchhistory"),self.parent.sercher_list_filters,self.parent.history_browser_marge_filters,100000000,0)

        self.parent.ui.sercherTableWidget.setRowCount(0)
        self.parent.ui.sercherTableWidget.setColumnCount(0)
        self.parent.ui.sercherTableWidget.setColumnCount(7)
        self.parent.ui.sercherTableWidget.setHorizontalHeaderLabels(["id","Fraza", "Domena","Data","Profil","Urzytkownik","Przeglądarka"])
        if rows:
            for row in rows:
                row_position = self.parent.ui.sercherTableWidget.rowCount()
                self.parent.ui.sercherTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                    
                    if i == 2:
                        if value is not None:
                            sufix = tldextract.extract(value).suffix
                            #subdomain = tldextract.extract(value).subdomain
                            domein = tldextract.extract(value).domain
                            item = QTableWidgetItem(str(f"{domein}.{sufix}"))
                            self.parent.ui.sercherTableWidget.setItem(row_position, i, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.sercherTableWidget.setItem(row_position, i, item)
        self.parent.ui.sercherTableWidget.cellClicked.connect(self.load_sercher_deteils)
        self.parent.ui.sercherTableWidget.verticalHeader().setVisible(False)
        for i in range(self.parent.ui.sercherTableWidget.columnCount()):
            if i != 1 and i != 2:
                self.parent.ui.sercherTableWidget.resizeColumnToContents(i)
        self.parent.ui.sercherTableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.parent.ui.sercherTableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        def enable_column_resize():
            self.parent.ui.sercherTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        QTimer.singleShot(0, enable_column_resize)

    def load_sercher_deteils(self, row, column):
        id = self.parent.ui.sercherTableWidget.item(row, 0).text()
        browser_name = self.parent.ui.sercherTableWidget.item(row,6).text()
        browser_name = browser_name.lower()
        browser_name = browser_name.replace(" ","_")
        rows = self.db_menager.get_sercher_deteils(browser_name+"_searchhistory",id)
        if rows:
            print(rows)
            if rows[0][1] is not None:
                self.parent.ui.sercherUrlLabel.setText(str(rows[0][1]))
                self.parent.ui.sercherWebEngineView.load(str(rows[0][1]))
            else:
                self.parent.ui.sercherUrlLabel.setText("Brak adresu URL")
            if rows[0][2] is not None:
                self.parent.ui.termLabel.setText(str(rows[0][2]))
            else:
                self.parent.ui.termLabel.setText("Brak zapisanego Frazy")
            if rows[0][3] is not None:
                self.parent.ui.sercherDateLabel.setText(str(rows[0][3]))
            else:
                self.parent.ui.sercherDateLabel.setText("Brak ostatniej dayty wizyty")

    def load_autofill(self):
        rows = self.db_menager.get_all_autofill(self.db_menager.get_browser_table_type_list("_autofill"),self.parent.autofill_filters,self.parent.history_browser_marge_filters,100000000,0)

        self.parent.ui.autofillTableWidget.setRowCount(0)
        self.parent.ui.autofillTableWidget.setColumnCount(0)
        self.parent.ui.autofillTableWidget.setColumnCount(7)
        self.parent.ui.autofillTableWidget.setHorizontalHeaderLabels(["id","Etykieta", "Wartość","Data ostaniego urzycia","Profil","Urzytkownik","Przeglądarka"])
        if rows:
            for row in rows:
                row_position = self.parent.ui.autofillTableWidget.rowCount()
                self.parent.ui.autofillTableWidget.insertRow(row_position)
                for i, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.parent.ui.autofillTableWidget.setItem(row_position, i, item)
        self.parent.ui.autofillTableWidget.cellClicked.connect(self.load_autofill_deteils)
        self.parent.ui.autofillTableWidget.verticalHeader().setVisible(False)

        for i in range(self.parent.ui.autofillTableWidget.columnCount()):
            if i != 1 and i != 2:
                self.parent.ui.autofillTableWidget.resizeColumnToContents(i)
        self.parent.ui.autofillTableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.parent.ui.autofillTableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        def enable_column_resize():
            self.parent.ui.autofillTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        QTimer.singleShot(0, enable_column_resize)


    def load_autofill_deteils(self, row, column):
        id = self.parent.ui.autofillTableWidget.item(row, 0).text()
        browser_name = self.parent.ui.autofillTableWidget.item(row,6).text()
        browser_name = browser_name.lower()
        browser_name = browser_name.replace(" ","_")
        rows = self.db_menager.get_autofill_deteils(browser_name+"_autofill",id)
        if rows:
            print(rows)
            if rows[0][1] is not None:
                self.parent.ui.autofillNameLabel.setText(str(rows[0][1]))
            else:
                self.parent.ui.autofillNameLabel.setText("Brak etykiety")
            if rows[0][2] is not None:
                self.parent.ui.autofillValueLabel.setText(str(rows[0][2]))
            else:
                self.parent.ui.autofillValueLabel.setText("Brak zapisanej wartości")
            if rows[0][3] is not None:
                self.parent.ui.autofillCountUseLabel.setText(str(rows[0][3]))
            else:
                self.parent.ui.autofillCountUseLabel.setText("Brak ilości urzyć")
            if rows[0][4] is not None:
                self.parent.ui.autofillCreateDateLabel.setText(str(rows[0][4]))
            else:
                self.parent.ui.autofillCreateDateLabel.setText("Brak daty utworzenia")
            if rows[0][5] is not None:
                self.parent.ui.autofillLastUseDateLabel.setText(str(rows[0][5]))
            else:
                self.parent.ui.autofillLastUseDateLabel.setText("Brak daty ostaniego urzycia")

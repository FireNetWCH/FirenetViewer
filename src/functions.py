import os
import sqlite3
import logging
from typing import Any, List, Dict, Optional
import pandas as pd
from PySide6.QtCore import Qt, QSettings, QDir, QPoint,QEasingCurve,QRect
from PySide6.QtGui import QFont, QFontDatabase, QAction,QStandardItem, QPixmap, QImage, QPainter
from PySide6.QtWidgets import (
    QCheckBox, QPushButton, QGraphicsScene, QTableWidgetItem, QTabBar,QMenu, QFileSystemModel,QSizePolicy,QSplitter,QFrame,QApplication,QTableWidget,QDialog,QCalendarWidget,
    QTreeView, QVBoxLayout, QFileDialog, QGraphicsView, QTreeWidgetItem,QListWidgetItem, QTreeWidget, QMainWindow,QListWidget,QHeaderView,QAbstractItemView
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.pagesizes import letter

from PySide6.QtCore import QPropertyAnimation as QAnimation
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

from src.email_page.multi_tag_dialog import MultiTagInputDialog
from src.email_page.multi_tag_selector import MultiTagSelector
from src.gui_function import display_file_content
from src.email_page.key_press_filter import KeyPressFilter
from src.calendar_dialog_widget import get_selected_date
from src.atachment_list_widget import FileListItem
from src.email_page.selector_tag_sercher import SekectorTag
from src.message_box.date_warning import left_date_wornig, rights_date_wornig
from src.db_function.exports import generate_pdf,remove_multi_new_line,export_to_pdf,export_to_excel
from src.email_page.export_options import ExportSelector
from src.db_function.db_email_folders_tree import load_folders_data_into_tree
from src.email_page.main_emeil_table import load_data_from_database
#from src.label_context_menu import show_context_menu
import src.db_function.db_email_function as db_email_function
import math
import json
import shutil 
import openpyxl
from openpyxl.styles import Alignment
from openpyxl.worksheet.page import PageMargins

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GUIFunctions:
    """ Klasa zawierająca funkcje obsługujące interfejs graficzny i logikę aplikacji. """
    def __init__(self, main_window: QMainWindow) -> None:
        self.main = main_window
        self.ui = main_window.ui
        self.db_connection: Optional[sqlite3.Connection] = None
        self.active_filters: Dict[str, str] = {'sender_name': "", "cc": "", "subject": "", "date_fr": "", 'date_to':"","folder_id" : "1","body":"","flag":"False","tag":""}
        self.columns_hidden: List[bool] = [False] * 7
        self.filtering_active: bool = False
        self.current_sort_order: Dict[int, Any] = {}

        #Parametry do obsługi emeil
        #kolumna w tabeli emaili gdzie znajdzuje się checbox
        self.column_check_box= 5
        file_config = open(".\\config.json")
        config = json.load(file_config)
        base_path = config['path']
        self.path = base_path
        self.sql_name = ""
        self.id_selected_email = 0
        self.is_expanded_serch_frame = True

        self.max_page = 0
        self.all_emails_count = 0
        self.current_page = 0
        self.emails_per_page = 500
        self._setup_ui(self.path)
        self._tymczaspwe_ukrycie_()
    def _setup_ui(self,path_database) -> None:
        """Inicjalizacja interfejsu – ustawienia czcionki, motywu oraz połączenia sygnałów."""
        self.enable_column_rearrangement()
        self.load_product_sans_font()
        self.initialize_app_theme()
        self.display_database(path_database)
        self.display_folders_in_help_page()
        self._connect_signals()
        
        # Konfiguracja widoku drzewa katalogów
        self.ui.select_directory.clicked.connect(self.select_directory)
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath('')
        self.tree_view = QTreeView(self.main)
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setVisible(False)
        layout = QVBoxLayout(self.main)
        layout.addWidget(self.tree_view)

        # Ustawie parametrów Ramki Wysukiwania Email i jej animacji
        frame = self.ui.dataAnalysisPage.findChild(QLabel,"label_7")
        self.animation = QAnimation(frame, b'maximumHeight')
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        #self.is_expanded_serch_frame = True

        # Konfiguracja widokui Email
        header = self.ui.tableWidget.horizontalHeader()
        for col in range(self.ui.tableWidget.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)
        splitter = QSplitter(Qt.Horizontal)
        dada_layout = self.ui.dataAnalysisPage.layout()
        splitter.addWidget(self.ui.tableWidget)
        splitter.addWidget(self.ui.EmailtabWidget)
        dada_layout.addWidget(splitter)
        self.ui.EmailtabWidget.tabCloseRequested.connect(lambda index: self.ui.EmailtabWidget.removeTab(index))
        tab_bar = self.ui.EmailtabWidget.tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)
        
        #ukrycie okna naglowkow email
        self.ui.emailHederDockWidget.hide()

        
        label = self.ui.homePage.findChild(QLabel, "label_7")
        print(label)
        pixmap = QPixmap("logo.jpg")
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(100, 100)
        
        
    def _connect_signals(self) -> None:
        """Łączy sygnały z odpowiednimi metodami."""
        # Menu (centralne i boczne)
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())
        #rozciąganie szerokości paska bocznego przy splitter
        self.ui.closeCenterMenuBtn.clicked.connect(lambda : self.ui.splitter.setSizes([0, 1]))
        self.ui.fileBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.settingsBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.infoBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.helpBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))


        # Obsługa wyszukiwania i filtrów
        self.ui.searchBtn.clicked.connect(self.show_search_results)
        self.ui.filter_table_btn.clicked.connect(self.join_search)
        self.ui.seachSurname.returnPressed.connect(self.join_search)
        self.ui.seachName.returnPressed.connect(self.join_search)
        self.ui.searchBody.returnPressed.connect(self.join_search)
        self.ui.searchDate.returnPressed.connect(self.join_search)
        self.ui.show_table_btn.clicked.connect(self.show_all_columns)
        self.ui.show_flags_btn.clicked.connect(self.toggle_filter_flags)
        self.ui.export_pdf.clicked.connect(self.open_dialog_export_selector_to_pdf)
        self.ui.exportExelBtn.clicked.connect(self.open_dialog_export_selector_to_exel)
        self.ui.pst_files_btn.clicked.connect(self.upload_pst_file)
        #self.ui.checkBoxData.checkStateChanged.connect(self.date_state_box)

        self.ui.tagPuschBtn.clicked.connect(lambda: self.open_dialog_tag_selector(self.active_filters))

        self.ui.startDataLabel.selectionChanged.connect(self.serch_by_date_start)
        self.ui.endDataLabel.selectionChanged.connect(self.serch_by_date_end)
        self.ui.startDataBtn.clicked.connect(self.serch_by_date_start)
        self.ui.endDataBtn.clicked.connect(self.serch_by_date_end)
        self.ui.startDataLabel.textChanged.connect(self.join_search)
        self.ui.endDataLabel.textChanged.connect(self.join_search)


        # Obsługa Event Tabeli Email
        self.ui.tableWidget.cellClicked.connect(self.load_clicked_email)
        self.ui.tableWidget.cellActivated.connect(self._get_id_flags_item_email)
        self.key_filter = KeyPressFilter(self.ui.tableWidget, self._get_id_flags_item_email,self.load_clicked_email,self.multi_flag_selected)
        self.ui.tableWidget.installEventFilter(self.key_filter)
        self.ui.prevEmailTableBtn.clicked.connect(self.previous_page)
        self.ui.nextEmailTableBtn.clicked.connect(self.next_page)
        self.ui.showSearchPanelBtn.clicked.connect(self.toggle_frame)
        # Obłsuga kliknięcia w drzewo katalogów Email
        tw = self.ui.helpPage.findChild(QTreeWidget,"folders_tree")
        tw.itemClicked.connect(self.tree_email_dir_clicked)

        # Obsługa Wyboru Bazy Emaili
        db_list = self.ui.helpPage.findChild(QListWidget, "db_list")
        db_list.itemClicked.connect(self.selec_sqlit_db)

        # Obsługa wyświetlania mutlimediów z załącznków email
        la = self.ui.EmailtabWidget.findChild(QListWidget,"listAttachments")
        la.itemClicked.connect(self.email_copy_attachments)

        # Obsługa pokazywania i ukrywania okna nagłówków email
        heder_btn = self.ui.EmailtabWidget.findChild(QPushButton,"hederEmailBtn")
        heder_btn.clicked.connect(self.show_heder_winodw)

        test = self.ui.emailHederDockWidget.findChild(QLabel,"headerEmailLabel")
        window_clode_btn = self.ui.emailHederDockWidget.findChild(QPushButton,"hiddenHederWindowBtn")
        print(window_clode_btn)
        window_clode_btn.clicked.connect(self.ui.emailHederDockWidget.hide)
    

        # konfiguracja menu rozwijanego dla Labelki zawierającej treść Emaila 
        bodylabel = self.ui.EmailtabWidget.findChild(QLabel, "body")
        bodylabel.setContextMenuPolicy(Qt.CustomContextMenu)
        bodylabel.customContextMenuRequested.connect(self.show_context_menu)

        

        # Konfiguracja menu nagłówka tabeli
        header = self.ui.tableWidget.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_column_menu)

    def _tymczaspwe_ukrycie_(self):
        #wyszukiwarka 
        self.ui.frame_2.hide()
        self.ui.searchBtn.hide()
        self.ui.searchinp.hide()
        self.ui.label_9.hide()
        self.ui.serachinpCont.hide()
        #przycisk
        self.ui.reportsBtn.hide()
        self.ui.infoBtn.hide()
        self.ui.fileBtn.hide()
        self.ui.detailsBtn.hide()
        print()



    def show_context_menu(self, pos):
        context_menu = self.ui.EmailtabWidget.findChild(QLabel, "body")
        all_labels =  db_email_function.get_all_labels_name(self.db_connection)
        labelContextMenu = QMenu(self.main)

        submenu = QMenu("Etykiety", labelContextMenu)
        selected_text = context_menu.selectedText()
        print(selected_text)
        for row in all_labels:
            action = QAction(str(row[1]), self.main)
            action.triggered.connect(lambda checked, value=row[0]: self.add_lebels_to_db(value,selected_text))
            submenu.addAction(action)
        labelContextMenu.addMenu(submenu)
        labelContextMenu.exec(context_menu.mapToGlobal(pos))

    def add_lebels_to_db(self,id_labels_name,selected_text):

        db_email_function.add_label(self.db_connection,id_labels_name,self.id_selected_email,selected_text)
        

    def show_heder_winodw(self):
        if self.ui.emailHederDockWidget.isHidden():
            self.ui.emailHederDockWidget.show()
        else:
            self.ui.emailHederDockWidget.hide()



    def serch_by_date_start(self):
        date = get_selected_date(self)
        
        if date is not None:
            if self.active_filters['date_to'] != "":
                if date.toString("yyyy-MM-dd") > self.active_filters['date_to']:
                    rights_date_wornig()
                    self.ui.startDataLabel.setText(date.toString(""))
                else:
                    self.ui.startDataLabel.setText(date.toString("yyyy-MM-dd"))
            else:
                self.ui.startDataLabel.setText(date.toString("yyyy-MM-dd"))
        else:
            self.ui.startDataLabel.setText("")

    def serch_by_date_end(self):
        date = get_selected_date(self)

        if date is not None:
            if self.active_filters['date_fr'] != "":
                if date.toString("yyyy-MM-dd") < self.active_filters['date_fr']:
                    left_date_wornig()
                    self.ui.endDataLabel.setText(date.toString(""))
                else:
                    self.ui.endDataLabel.setText(date.toString("yyyy-MM-dd"))
            else:
                self.ui.endDataLabel.setText(date.toString("yyyy-MM-dd"))
        else:
            self.ui.endDataLabel.setText("")
            
    def toggle_frame(self):
        frame = self.ui.dataAnalysisPage.findChild(QFrame,"serchEmailFrame")
        self.animation.setTargetObject(frame)
        if self.is_expanded_serch_frame:
            self.animation.setStartValue(self.ui.dataAnalysisPage.findChild(QFrame,"serchEmailFrame").height())
            self.animation.setEndValue(0)
        else:
            self.animation.setStartValue(self.ui.dataAnalysisPage.findChild(QFrame,"serchEmailFrame").height())
            self.animation.setEndValue(100) 
        self.animation.start()

        self.is_expanded_serch_frame = not self.is_expanded_serch_frame

    def next_page(self):
        if self.current_page < self.max_page-1:
            self.current_page += 1
        load_data_from_database(self)

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        load_data_from_database(self)

    def _get_id_flags_item_email(self,row):
        id = self.ui.tableWidget.item(row,0).text()
        check_box = self.ui.tableWidget.cellWidget(row,self.column_check_box)
        flags = int(check_box.isChecked())
        if flags == 1:
            flags = 0
            check_box.setChecked(False)
        else:
            flags = 1
            check_box.setChecked(True)
        db_email_function.update_flag(self.db_connection,id,flags)
    
    def multi_flag_selected(self,rows):
        all_is_one_state = True
        id_list =[]
        first_state = self.ui.tableWidget.cellWidget(rows[0],self.column_check_box).isChecked()
        for row in rows:
            if first_state != self.ui.tableWidget.cellWidget(row,self.column_check_box).isChecked():
                all_is_one_state = False
                id_list.append(self.ui.tableWidget.item(row,0).text())
        if all_is_one_state == True:
            db_email_function.update_multi_flags(self.db_connection,id_list,not first_state)
            for row in rows:
                self.ui.tableWidget.cellWidget(row,self.column_check_box).setChecked(not first_state)
        else:
            db_email_function.update_multi_flags(self.db_connection,id_list,True)
            for row in rows:
                self.ui.tableWidget.cellWidget(row,self.column_check_box).setChecked(True)

    def date_state_box(self):
        pom = self.ui.checkBoxData.isChecked()
        self.ui.seachOd.setEnabled(pom)
        self.ui.seachDo.setEnabled(pom)


    def selec_sqlit_db(self,item):
        print(os.path.join(self.path,item.text().split('.')[0],item.text()))
        if not self.db_connection is None: 
            self.db_connection.close()
            print("zamknięto polaczenie")
        
        db_path = os.path.join(self.path,item.text().removesuffix('.sqlite'),item.text())
        print(db_path)
        db_email_function.connect_to_database(self,db_path)
        sql_name = db_path.split('\\')[-1]
        sql_name = sql_name.removesuffix('.sqlite')
        self.sql_name = sql_name
        self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(sql_name)
        
        load_data_from_database(self)
        self.display_folders_in_help_page()
        tw = self.ui.helpPage.findChild(QTreeWidget,"folders_tree")
        tw.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tw.itemClicked.connect(self.tree_email_dir_clicked)
        self.clear_filtr()
    
    def open_dialog_tag_selector(self, user_id: int) -> None:
        """Otwiera okno dialogowe do edycji tagów użytkownika."""
        dialog = SekectorTag(self.db_connection, self.active_filters,self.main)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika {user_id}")
            self.ui.selectedTagLabel.setText(f"Wybrane Tagi: {self.active_filters['tag'].removeprefix("(").removesuffix(")")}")
            load_data_from_database(self)

    def open_dialog_export_selector_to_pdf(self):
        dialog = ExportSelector()
        if dialog.exec_() == QDialog.Accepted:
            selected_option = dialog.get_selected_option()
            is_checkBox_checked = dialog.get_checkBox_state()
            export_to_pdf(self,self.db_connection,self.path,self.sql_name,self.active_filters,selected_option,is_checkBox_checked)
            
    def open_dialog_export_selector_to_exel(self):
        dialog = ExportSelector()
        if dialog.exec_() == QDialog.Accepted:
            selected_option = dialog.get_selected_option()
            is_checkBox_checked = dialog.get_checkBox_state()
            export_to_excel(self,self.db_connection,self.path,self.sql_name,self.active_filters,selected_option,is_checkBox_checked)

    def load_clicked_email(self,row,column):
        id = self.ui.tableWidget.item(row,0).text()
        print(self.active_filters)
        self.id_selected_email = id
        query =f'''
        SELECT * from emails WHERE id = {id}
        '''
        for x in range(self.ui.EmailtabWidget.count() - 1, 0, -1):
            self.ui.EmailtabWidget.removeTab(x)
        body_label = self.ui.EmailtabWidget.findChild(QLabel, "body")
        subject_label = self.ui.EmailtabWidget.findChild(QLabel, "subject")
        sender_label = self.ui.EmailtabWidget.findChild(QLabel, "sender")
        date_label = self.ui.EmailtabWidget.findChild(QLabel, "date")
        cc_label = self.ui.EmailtabWidget.findChild(QLabel, "cc")
        header_email_label = self.ui.emailHederDockWidget.findChild(QLabel,"headerEmailLabel")
        
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        emai_value = cursor.fetchall()

        query_attachments = f'''SELECT * FROM attachments WHERE email_id ={emai_value[0][0]}'''
        cursor.execute(query_attachments)
        attachments_value = cursor.fetchall()
        listAttachments = self.ui.EmailtabWidget.findChild(QListWidget, "listAttachments")
        listAttachments.clear()
        for _, file_name, extra_value in attachments_value:
            file_path = os.path.join(self.path,self.sql_name,"Attachments",str(self.id_selected_email),file_name)
            widget = FileListItem(f"{file_name}",file_path,self.ui.EmailtabWidget)  
            item = QListWidgetItem(listAttachments)
            item.setSizeHint(widget.sizeHint())  
            listAttachments.addItem(item)  
            listAttachments.setItemWidget(item, widget)
        listAttachments.setFixedHeight(60)
        search_term = self.active_filters['body']
        pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        
        if isinstance(emai_value[0][8],str):
            tekst = emai_value[0][8]
        else:
            tekst = emai_value[0][8].decode("utf-8")

            tekst_html = tekst.replace('\n', '<br>')
            if(search_term ==""):
                body_label.setText(tekst_html)
            else:
                highlighted_content = pattern.sub(lambda match: f"<span style='background-color: yellow;'>{match.group()}</span>",tekst_html)
                body_label.setTextFormat(Qt.TextFormat.RichText)    
                body_label.setText(highlighted_content)

        subject_label.setText(emai_value[0][7])
        sender_label.setText(emai_value[0][3])
        date_label.setText(emai_value[0][1])
        cc_label.setText(emai_value[0][5])
        header_email_label.setText(emai_value[0][11])
  
    def clear_filtr(self):
        self.ui.seachName.setText("")
        self.ui.seachSurname.setText("")
        self.ui.searchDate.setText("")
        self.ui.searchBody.setText("")
        self.active_filters["sender_name"] = ""
        self.active_filters["cc"] = ""
        self.active_filters["subject"] = ""
        self.active_filters["body"] = ""
        self.active_filters["tag"] = ""
        
    def tree_email_dir_clicked(self,item ,column):
        self.active_filters["folder_id"] = item.data(0,1)
        self.clear_filtr()
        

        load_data_from_database(self)
        self.current_page = 0
            
    def email_copy_attachments(self,item):
        source_path = os.path.join(self.path,self.sql_name,"Attachments",str(self.id_selected_email),item.text())
        destination_path, _ = QFileDialog.getSaveFileName(None, "Zapisz plik jako",item.text(), item.text().split('.')[-1])
        try:
         if destination_path:  
            shutil.copy(source_path, destination_path)
            print(f"Plik został skopiowany do: {destination_path}")
            logger.info(f"Plik został skopiowany do: {destination_path}")
        except Exception as e:
            print(f"Błąd podczas kopiowania pliku: {e}")
            logger.error(f"Błąd podczas kopiowania pliku: {e}")


    def open_tag_selector(self, email_id: int) -> None:
        """Otwiera okno dialogowe do edycji tagów użytkownika."""
        dialog = MultiTagSelector(email_id, self.db_connection, self.main)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika {email_id}")
            load_data_from_database(self)

    def show_search_results(self) -> None:
        """Wyświetla wyszukane wyniki (przykładowo – pokazuje tooltip)."""
        search_phrase = self.ui.searchinp.text()
        if not search_phrase:
            return
        try:
            self.searchToolTip.show()
        except AttributeError:
            self.create_search_tip_overlay()
            self.searchToolTip.show()
        self.searchToolTip.setDescription("Wyszukuję informację dla... " + search_phrase)

    def initialize_app_theme(self) -> None:
        """Inicjalizuje motyw aplikacji na podstawie ustawień."""
        settings = QSettings()
        current_theme = settings.value("THEME")
        self.populate_theme_list(current_theme)
        self.ui.themeList.currentTextChanged.connect(self.change_app_theme)

    def populate_theme_list(self, current_theme: str) -> None:
        """Wypełnia listę dostępnych motywów."""
        for theme in self.ui.themes:
            if (theme.name == "LightBlue") or (theme.name == "DarkYellow"):
                self.ui.themeList.addItem(theme.name, theme.name)
                if theme.defaultTheme or theme.name == current_theme:
                    index = self.ui.themeList.findData(theme.name)
                    self.ui.themeList.setCurrentIndex(index)

    def change_app_theme(self) -> None:
        """Zmienia motyw aplikacji."""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")
        if current_theme != selected_theme:
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    def load_product_sans_font(self) -> None:
        """Ładuje czcionkę Product Sans i ustawia ją dla aplikacji."""
        font_id = QFontDatabase.addApplicationFont("./fonts/...")
        if font_id == -1:
            logger.error("Failed to load Product Sans font")
            return 
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        product_sans = QFont(font_families[0] if font_families else 'Sans Serif')
        self.main.setFont(product_sans)

    def load_filtr_dict(self) -> None:
        self.active_filters["sender_name"] = self.ui.seachName.text().lower()
        self.active_filters["cc"] = self.ui.seachSurname.text().lower()
        self.active_filters["subject"] = self.ui.searchDate.text().lower()
        self.active_filters["date_fr"] = self.ui.startDataLabel.text().lower()
        self.active_filters["date_to"] = self.ui.endDataLabel.text().lower()
        self.active_filters["body"] = self.ui.searchBody.text().lower()
        # fitr pod flaga w innym miejscu (toggle_filter_flags)
    def join_search(self):
        self.load_filtr_dict()
        load_data_from_database(self)    

    def show_column_menu(self, position: QPoint) -> None:
        """Wyświetla menu kontekstowe dla nagłówka kolumny."""
        header = self.ui.tableWidget.horizontalHeader()
        column = header.logicalIndexAt(position)
        menu = QMenu(self.main)
        sort_asc_action = QAction("Sortuj rosnąco", self.main)
        sort_desc_action = QAction("Sortuj malejąco", self.main)
        hide_column_action = QAction("Ukryj kolumnę", self.main)

        if column == 6:
            add_tag_action = QAction("Dodaj tag", self.main)
            add_tag_action.triggered.connect(self.open_add_tag_dialog)
            menu.addAction(add_tag_action)

        sort_asc_action.triggered.connect(lambda: self.sort_column(column, Qt.AscendingOrder))
        sort_desc_action.triggered.connect(lambda: self.sort_column(column, Qt.DescendingOrder))
        hide_column_action.triggered.connect(lambda: self.hide_columns(column))

        menu.addAction(sort_asc_action)
        menu.addAction(sort_desc_action)
        menu.addSeparator()
        menu.addAction(hide_column_action)
        menu.exec(header.mapToGlobal(position))

    def set_data(line_edit,text):
        line_edit.setText(text)

    def sort_column(self, column_index: int, order: Any) -> None:
        """Sortuje tabelę według wybranej kolumny."""
        self.ui.tableWidget.sortItems(column_index, order)

    def hide_columns(self, column_index: int) -> None:
        """Przełącza widoczność wskazanej kolumny."""
        self.columns_hidden[column_index] = not self.columns_hidden[column_index]
        self.ui.tableWidget.setColumnHidden(column_index, self.columns_hidden[column_index])

    def show_all_columns(self) -> None:
        """Przywraca widoczność wszystkich kolumn."""
        for i in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnHidden(i, False)
        self.columns_hidden = [False] * self.ui.tableWidget.columnCount()

    def enable_column_rearrangement(self) -> None:
        """Umożliwia przeciąganie i zmienianie kolejności kolumn w tabeli."""
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionsMovable(True)
        header.setDragEnabled(True)

    def plot_data(self, ages: List[int]) -> None:
        """Tworzy histogram wieku użytkowników i wyświetla go na widżecie."""
        scene = QGraphicsScene()
        fig, ax = plt.subplots(figsize=(5, 4))
        if ages:
            bins = range(min(ages), max(ages) + 2)
            ax.hist(ages, bins=bins, alpha=0.7, color='blue')
        ax.set_title("Wiek ludzi z danych z tabeli")
        ax.set_xlabel("Wiek")
        ax.set_ylabel("Częstotliwość")
        canvas = FigureCanvas(fig)
        canvas.draw()
        scene.addWidget(canvas)
        self.ui.graphicsView.setScene(scene)

    def open_add_tag_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        dialog = MultiTagInputDialog(self.db_connection, self.main)
        if dialog.exec():
            logger.info("Nowy tag został dodany.")
            load_data_from_database(self)

    def toggle_filter_flags(self) -> None:
        """Przełącza tryb filtrowania według zaznaczonych flag."""
        if self.active_filters["flag"] == "True":
            self.active_filters["flag"] = "False"
        else:
            self.active_filters["flag"] = "True"
        self.join_search()
    
    def select_directory(self) -> None:
        """Pozwala wybrać katalog, a następnie wyświetla jego zawartość."""
        directory = QFileDialog.getExistingDirectory(self.main, "Wybierz katalog", "", options=QFileDialog.Options())
        if directory:
            self.replace_label_with_treeview(directory)
            self.switch_to_file_reader()

    def switch_to_file_reader(self) -> None:
        """Przełącza widok na czytnik plików."""
        self.ui.fileBtn.click()

    def replace_label_with_treeview(self, directory: str) -> None:
        """Zamienia etykietę na widok drzewa katalogów."""
        self.file_system_model.setRootPath(directory)
        self.file_system_model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.tree_view.setRootIndex(self.file_system_model.index(directory))
        for col in [1, 2, 3]:
            self.tree_view.setColumnHidden(col, True)
        layout = self.ui.fileReader.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.fileReader)
            self.ui.fileReader.setLayout(layout)
        # Usunięcie starych widżetów
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)
        layout.addWidget(self.tree_view)
        self.tree_view.setVisible(True)
        self.tree_view.selectionModel().selectionChanged.connect(self.on_file_selection_changed)

    def on_file_selection_changed(self) -> None:
        """Wywoływana po zmianie zaznaczenia – wyświetla zawartość wybranego pliku."""
        selected_indexes = self.tree_view.selectedIndexes()
        if selected_indexes:
            selected_file_path = self.file_system_model.filePath(selected_indexes[0])
            display_file_content(self,selected_file_path)

    def display_image_message(self, message: str) -> None:
        """Wyświetla komunikat (np. informujący o niedostępnej funkcjonalności)."""
        self.ui.label_11.setText(message)

    def upload_pst_file(self) -> None:
        """Pozwala wybrać plik PST i wywołuje funkcję jego przetwarzania."""
        pst_file, _ = QFileDialog.getOpenFileName(self.main, "Wybierz plik .pst", "", "PST Files (*.pst)")
        if pst_file:
            self.process_pst_file(pst_file)

    def process_pst_file(self, pst_file: str) -> None:
        """Przetwarza plik PST (implementację uzupełnij według potrzeb)."""
        logger.info(f"Przetwarzanie pliku PST: {pst_file}")

    def display_folders_in_help_page(self):
        self.folders_tree = QTreeWidget()
        self.folders_tree.setHeaderLabel("Struktura folderów (z bazy)")
        self.folders_tree.setObjectName("folders_tree")
        self.folders_tree.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout = self.ui.helpPage.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.helpPage)
            self.ui.helpPage.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                #print(w.objectName)
                if (w) and not (isinstance(w ,QListWidget)):
                    w.setParent(None)
        column_count = self.folders_tree.columnCount()


        for i in range(column_count):
            self.folders_tree.resizeColumnToContents(i)
            row_count = self.folders_tree.topLevelItemCount()

        for i in range(row_count):
            self.folders_tree.resizeRowToContents(i)

        layout.addWidget(self.folders_tree)
        load_folders_data_into_tree(self,self.db_connection,self.folders_tree)

    def display_database(self,path_to_dir):
        self.list_widget = QListWidget()
        self.list_widget.setObjectName("db_list")
        self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sql_list_file = []
        dir_content =  os.scandir(path_to_dir)
        for file in dir_content:
            if os.path.isdir(os.path.join(path_to_dir,file)):
                list_file = os.scandir(os.path.join(path_to_dir,file))
                for sq_file in list_file:
                    if os.path.isfile(os.path.join(path_to_dir,file,sq_file)) :
                        _, ext = os.path.splitext(sq_file.name.lower())
                        if ext == '.sqlite':
                            sql_list_file.append(sq_file.name)


        if self.db_connection is None and len(sql_list_file) > 0 :
            try:
                db_email_function.connect_to_database(self,path_to_dir+"\\"+sql_list_file[0].split('.')[-2]+"\\"+sql_list_file[0])
                load_data_from_database(self)
                self.sql_name =sql_list_file[0].split('.')[-2]
                self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(self.sql_name)
                logger.info(f"Połączono z pierwszą odnalezioną bazą SQLite: {self.sql_name}")
            except Exception as e:
                logger.error(f"Bład przy pierwszym łaczeniu do SQLite: {e}")
        print(sql_list_file)
        self.list_widget.addItems(sql_list_file)    
        layout = self.ui.helpPage.layout()
        layout.addWidget(self.list_widget)
        

    
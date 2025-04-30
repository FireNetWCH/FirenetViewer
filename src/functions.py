import os
import sqlite3
import logging
from typing import Any, List, Dict, Optional
    
from PySide6.QtCore import Qt, QSettings, QDir, QPoint,QEasingCurve,QDate,QUrl,Slot,QObject
from PySide6.QtGui import QFont, QFontDatabase, QAction, QPixmap,QIcon,QDesktopServices,QImage
from PySide6.QtWidgets import (QLineEdit,QApplication,
    QPushButton, QGraphicsScene, QTabBar,QMenu, QFileSystemModel,QSizePolicy,QSplitter,QFrame,QDialog,QMessageBox,
    QTreeView, QVBoxLayout, QFileDialog,QListWidgetItem, QTreeWidget, QMainWindow,QListWidget,QHeaderView,QSizeGrip
)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.pagesizes import letter

from PySide6.QtCore import QPropertyAnimation as QAnimation
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

from src.email_page.multi_tag_dialog import MultiTagInputDialog
from src.email_page.multi_tag_selector import MultiTagSelector
from PySide6.QtGui import QDesktopServices
from src.gui_function import display_file_content
from src.email_page.key_press_filter import KeyPressFilter
from src.calendar_dialog_widget import DateRangeDialog
from src.atachment_list_widget import FileListItem
from src.email_page.selector_tag_sercher import SekectorTag
from src.email_page.tag_dialog import TagCrud
from src.email_page.label_dialog import LabelsCrud
from src.db_function.exports import export_to_pdf,export_to_excel
from src.email_page.export_options import ExportSelector
from src.label_page.main_label_page import load_all_labels,load_clicked_email_on_labels
from src.db_function.db_email_folders_tree import load_folders_data_into_tree
from src.email_page.main_emeil_table import load_data_from_database,load_color_dictionery,ClickableLabel
from src.email_page.context_menu import LabelContextMenu,EditLabelContextMenu,TableContextMenu
from src.message_box.scaletLabel import ScalableLabel
#from src.label_context_menu import show_context_menu
import src.db_function.db_email_function as db_email_function
from src.graphs_page.mein_graps_page import load_stat 
from src.message_box.date_warning import add_labels_worning
import shutil 
import sys
import hashlib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_resource_path(relative_path):
    """Zwraca poprawną ścieżkę do zasobów, obsługując tryb onefile"""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS  
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GUIFunctions(QObject):
    """ Klasa zawierająca funkcje obsługujące interfejs graficzny i logikę aplikacji. """
    def __init__(self, main_window: QMainWindow) -> None:
        super().__init__() 
        self.main = main_window
        self.ui = main_window.ui
        self.db_connection: Optional[sqlite3.Connection] = None
        self.active_filters: Dict[str, str] = {'sender_email': "", "recipients": "", "subject": "", "date_fr": "", 'date_to':"","folder_id" : "1","body":"","flag":"False","tag":""}
        self.columns_hidden: List[bool] = [False] * 7
        self.filtering_active: bool = False
        self.current_sort_order: Dict[int, Any] = {}

        self.url_www = "https://www.firenet.com.pl/"
        self.url_linkedin = "https://www.linkedin.com/in/firenet-informatyka-%C5%9Bledcza-71197a357/"
        self.url_fb = "https://www.facebook.com/profile.php?id=61574549756781&locale=pl_PL"
       
        #Parametry do obsługi emeil
        #kolumna w tabeli emaili gdzie znajdzuje się checbox
        self.column_check_box= 5
        # config_path = get_resource_path("config.json")
        #print(os.getcwd())
        # config_path = os.getcwd()+"\\SQL"
        self.pom = True
        # config = json.load(config_path)
        # base_path = config['path']
        self.path = os.getcwd()+"\\SQL"
        self.sql_name = ""
        self.id_selected_email = 0
        self.is_expanded_serch_frame = True
        self.id_selected_label = 0
        self.max_page = 0
        self.all_emails_count = 0
        self.last_clicket_row = 0
        self.current_page = 0
        self.emails_per_page = 100
        self.tag_color : Dict[str, str] = {}
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

        # splitter2 = QSplitter(Qt.Horizontal)
        # #dada_layout = self.ui.dataAnalysisPage.layout()
        # splitter2.addWidget(self.ui.widget_45)
        # splitter2.addWidget(self.ui.widget_48)
        #dada_layout.addWidget(self.ui.widget_46) 
        dada_layout.addWidget(self.ui.widget_46)
        
        
        #ukrycie okna naglowkow email
        self.ui.emailHederDockWidget.hide()

        
        old_label = self.ui.homePage.findChild(QLabel, "label_7")
        new_label = ScalableLabel(parent=old_label.parent())
        new_label.setObjectName("label_7")
        new_label.setGeometry(old_label.geometry())

        layout = old_label.parentWidget().layout()
        if layout:
            index = layout.indexOf(old_label)
            layout.removeWidget(old_label)
            old_label.deleteLater()
            layout.insertWidget(index, new_label)
        else:
            old_label.deleteLater()
            new_label.show()

        # Ustaw pixmapę
        image = QImage(get_resource_path("logo.png"))
        # Ustawienie obrazu w ScalableLabel
        new_label.setPixmap(QPixmap.fromImage(image))
          
        # print(label)
        # pixmap = QPixmap("logo.png")
        # scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # label.setPixmap(scaled_pixmap)
        
        
        
        # Konfiguracja widokui Email w sekcji etykiet
        self.ui.EmailtabWidget_2.tabCloseRequested.connect(lambda index: self.ui.EmailtabWidget_2.removeTab(index))
        tab_bar = self.ui.EmailtabWidget_2.tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)
    def debuging(self):
        self.main.showMinimized()
        
        
        
    def _connect_signals(self) -> None:
        """Łączy sygnały z odpowiednimi metodami."""
        # Menu (centralne i boczne)
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        #self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.meilBoxBtn.clicked.connect(self.clicket_hamburger )
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())
        
        
        self.ui.minimalizeBtn.clicked.connect(self.debuging)
        self.ui.restoreBtn.clicked.connect(self.toggle_window_state)
        self.ui.graphsBtn.clicked.connect(lambda :load_stat(self,self.db_connection))
        
       
       
        #rozciąganie szerokości paska bocznego przy splitter
        self.ui.closeCenterMenuBtn.clicked.connect(lambda : self.ui.splitter.setSizes([0, 1]))
        self.ui.fileBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.settingsBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.infoBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        #self.ui.helpBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))
        self.ui.meilBoxBtn.clicked.connect(lambda : self.ui.splitter.setSizes([1, 2]))

        # Obsługa wyszukiwania i filtrów
        self.ui.searchBtn.clicked.connect(self.show_search_results)
        #self.ui.filter_table_btn.clicked.connect(self.join_search)
        self.ui.seachSurname.returnPressed.connect(self.join_search)
        self.ui.seachName.returnPressed.connect(self.join_search)
        self.ui.searchBody.returnPressed.connect(self.join_search)
        self.ui.searchDate.returnPressed.connect(self.join_search)
        self.ui.show_table_btn.clicked.connect(self.show_all_columns)
        self.ui.show_flags_btn.clicked.connect(self.toggle_filter_flags)
        self.ui.export_pdf.clicked.connect(self.open_dialog_export_selector_to_pdf)
        self.ui.clearBtn.clicked.connect(self.clear_filtr)
       
        self.ui.exportExelBtn.clicked.connect(self.open_dialog_export_selector_to_exel)
        self.ui.tagiBtn.clicked.connect(self.show_tag_crud)


        self.ui.labelNameCrudBtn.clicked.connect(lambda :self.show_label_crud(self.path))
        self.ui.lableBtn.clicked.connect(self.open_label_page)
        self.ui.LabelTableWidget.cellClicked.connect(lambda row : load_clicked_email_on_labels(self,row))
        self.ui.contactBtn.clicked.connect(self.show_email_client)
        self.ui.wwwBtn.clicked.connect(self.open_www_in_browser)
        
        self.ui.linkedinBtn.clicked.connect(self.open_linkedin_in_browser)
        
        self.ui.fbBtn.clicked.connect(self.open_facebook_in_browser)
        
        #self.ui.checkBoxData.checkStateChanged.connect(self.date_state_box)

        self.ui.tagPuschBtn.clicked.connect(lambda: self.open_dialog_tag_selector(self.active_filters))

        self.ui.startDataLabel.selectionChanged.connect(self.serch_by_date_start)
        self.ui.endDataLabel.selectionChanged.connect(self.serch_by_date_start)
        #self.ui.endDataLabel.selectionChanged.connect(self.serch_by_date_end)
        self.ui.startDataBtn.clicked.connect(self.serch_by_date_start)
        #self.ui.endDataBtn.clicked.connect(self.serch_by_date_start)
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
        self.ui.dataAnalysisPage.findChild(QLineEdit,"jumpToPagelineEdit").returnPressed.connect(self.jump_to_page)

        # Dodanie menu kontekstowego do Tabeli Emaili
        self.context_menu_email_table = TableContextMenu(main=self, db_connection=self.db_connection, parent=self.ui.tableWidget)
        
        # Obłsuga kliknięcia w drzewo katalogów Email
        tw = self.ui.helpPage.findChild(QTreeWidget,"folders_tree")
        tw.itemClicked.connect(self.tree_email_dir_clicked)

        # Obsługa Wyboru Bazy Emaili
        db_list = self.ui.helpPage.findChild(QListWidget, "db_list")
        db_list.itemClicked.connect(self.selec_sqlit_db)

        # Obsługa wyświetlania mutlimediów z załącznków email
        # la = self.ui.EmailtabWidget.findChild(QListWidget,"listAttachments")
        # print(la)
        # la.itemClicked.connect(FileListItem)

        # Obsługa pokazywania i ukrywania okna nagłówków email
        heder_btn = self.ui.EmailtabWidget.findChild(QPushButton,"hederEmailBtn")
        heder_btn.clicked.connect(self.show_heder_winodw)

        # test = self.ui.emailHederDockWidget.findChild(QLabel,"headerEmailLabel")
        # window_clode_btn = self.ui.emailHederDockWidget.findChild(QPushButton,"hiddenHederWindowBtn")
        # print(window_clode_btn)
        # window_clode_btn.clicked.connect(self.ui.emailHederDockWidget.hide)
    

        # konfiguracja menu rozwijanego dla Labelki zawierającej treść Emaila 
        bodylabel = self.ui.EmailtabWidget.findChild(QLabel, "body")
        bodylabel.setContextMenuPolicy(Qt.CustomContextMenu)
        bodylabel.customContextMenuRequested.connect(self.show_context_menu)

        # konfiguracja menu rozwijanego dla Labelki zawierającej treść Emaila w sekcji Etykiet
        bodylabel = self.ui.page.findChild(QLabel, "body_2")
        bodylabel.setContextMenuPolicy(Qt.CustomContextMenu)
        bodylabel.customContextMenuRequested.connect(self.show_context_menu_email_body)


        # Konfiguracja menu nagłówka tabeli
        header = self.ui.tableWidget.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_column_menu)

        # ustawienia size gripa i możliwości ruszania oknem przez trzymanie zewnetrtznej ramki 
        self.resize_grip_frame = self.ui.sizeGrip
        self.resize_grip = QSizeGrip(self.resize_grip_frame)
        self.resize_grip.resize(200, 200)
        self.resize_grip.move(self.main.width() - 20, self.main.height() - 20)

        pixmap = QPixmap(get_resource_path("miniLogo.png"))
        scaled_pixmap = pixmap.scaled(40, 40, Qt.KeepAspectRatio)
        self.ui.label_23.setPixmap(scaled_pixmap)
        self.ui.ofertaBtn.setIcon(QIcon(scaled_pixmap))
        # self.resize_grip.setIcon(QIcon(get_resource_path("Qss\\icons\\FFFFFF\\feather\\home.png")))

        #ustawienie odpowiednich ikon i kolorów tła
    
       
        self.ui.export_pdf.setIcon(QIcon(":feather/icons/feather/pdf.png"))
        
        self.ui.exportExelBtn.setIcon(QIcon(":feather/icons/feather/xls.png"))
        
        self.ui.clearBtn.setIcon(QIcon(":material_design/icons/material_design/hide_source.png"))
        self.ui.show_table_btn.setIcon(QIcon(":feather/icons/feather/rotate-cw.png"))
        self.ui.leftMenu.setStyleSheet("background-color: #102339; border: 3px solid #102339;")

        self.ui.homeBtn.setIcon(QIcon(":feather/FFFFFF/feather/home.png"))
        self.ui.infoBtn.setIcon(QIcon(":feather/FFFFFF/feather/activity.png"))
        self.ui.dataBtn.setIcon(QIcon(":feather/FFFFFF/feather/mail.png"))
        self.ui.restoreBtn.setIcon(QIcon(":feather/FFFFFF/feather/copy.png"))
        self.ui.closeBtn.setIcon(QIcon(":feather/FFFFFF/feather/x.png"))
        self.ui.linkedinBtn.setIcon(QIcon(":feather/FFFFFF/feather/linkedin.png"))
        self.ui.fbBtn.setIcon(QIcon(":feather/FFFFFF/feather/facebook.png"))

        self.ui.graphsBtn.setIcon(QIcon(":font_awesome/FFFFFF/font_awesome/solid/chart-pie.png"))
        self.ui.meilBoxBtn.setIcon(QIcon(":material_design/FFFFFF/material_design/format_align_justify.png"))
        
        self.ui.closeCenterMenuBtn.setIcon(QIcon(":font_awesome/icons/font_awesome/solid/circle-xmark.png"))
        self.ui.startDataBtn.setIcon(QIcon(":font_awesome/icons/font_awesome/regular/calendar.png"))

        self.ui.minimalizeBtn.setIcon(QIcon(":feather/FFFFFF/feather/minus.png"))
        self.ui.prevEmailTableBtn.setIcon(QIcon(":feather/icons/feather/arrow_left.png"))
        self.ui.nextEmailTableBtn.setIcon(QIcon(":feather/icons/feather/arrow_right.png"))
        
        self.ui.fbBtn.setIcon(QIcon(":feather/FFFFFF/feather/facebook.png"))
        self.ui.wwwBtn.setIcon(QIcon(":feather/FFFFFF/font_awesome/solid/rss.png"))
        
        # file = QFile(":feather/FFFFFF/feather/activity.png")

        # if file.exists():
        #     print("Zasób został poprawnie załadowany!")
        # else:
        #     print("Zasób NIE został znaleziony.")

        self.ui.widget_42.hide()
        self.ui.progressBar.hide()
    
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
        self.ui.settingsBtn.hide()
        self.ui.detailsBtn.hide()
        self.ui.menuBtn.hide()
        self.ui.helpBtn.hide()
    
    def toggle_window_state(self):
        self.ui.restoreBtn.setIcon(QIcon(get_resource_path("Qss\\icons\\FFFFFF\\feather\\copy.png")))
        #print(self.main.windowState())
        state = self.main.windowState()
        if self.pom:
            self.main.showNormal()
            self.pom=False
        else:
            self.main.showMaximized()
            self.pom=True
            
    def show_email_client(self):
        adres_email = "biuro@firenet.com.pl"
        subject = "FireNet Viewer: "
        body = ""

        mailto_link = f"mailto:{adres_email}?subject={QUrl.toPercentEncoding(subject).data().decode()}&body={QUrl.toPercentEncoding(body).data().decode()}"
        QDesktopServices.openUrl(QUrl(mailto_link))

    def show_tag_crud(self):
        dialog = TagCrud(self.db_connection,self.sql_name,path = self.path)
        load_color_dictionery(self)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika")
            #self.ui.selectedTagLabel.setText(f"Wybrane Tagi: {self.active_filters['tag'].removeprefix("(").removesuffix(")")}")
            
    
    def show_label_crud(self,path):
        dialog = LabelsCrud(self.db_connection,path = path)
        if dialog.exec():
            logger.info(f"Zaktualizowano labelki")
            load_all_labels(self)
            #self.ui.selectedTagLabel.setText(f"Wybrane Tagi: {self.active_filters['tag'].removeprefix("(").removesuffix(")")}")

    def open_www_in_browser(self):
        QDesktopServices.openUrl(QUrl(self.url_www))

    def open_linkedin_in_browser(self):
        QDesktopServices.openUrl(QUrl(self.url_linkedin))

    def open_facebook_in_browser(self):
        QDesktopServices.openUrl(QUrl(self.url_fb))
    
    def set_tag(self,tag):
        values = []
        query_parts = []
        scroll_pos = self.ui.tableWidget.verticalScrollBar().value()
        id = db_email_function.get_it_tags(tag,self.db_connection)
        widgets_ = []
        query_list = ""
        # print(id)
        pom = True
        for idx in self.ui.tableWidget.selectionModel().selectedRows():
            row = idx.row()
            widget = self.ui.tableWidget.cellWidget(row, 6)

            widgets_.append(widget)
            item = self.ui.tableWidget.item(row, 0) 
            if item:
                values.append(item.text())
                query_list +=f"({id[0][0]},{item.text()})"
                query_parts.append(f"({id[0][0]}, {item.text()})") 
                
        if query_parts:
            query_list = ", ".join(query_parts)
        for items in widgets_:
            layout = items.layout()
            in_widget = False
            if layout is not None:
                for i in range(layout.count()):
                    child = layout.itemAt(i).widget()
                    if child.text() == tag:
                        in_widget = True
                        # print("ZMIANA")
                        break
                    #print(f"child:{child.text()}")
            pom = in_widget
            if pom == False:
                break
        #print(pom)
        last_row = self.ui.tableWidget.selectionModel().selectedRows()
        if pom:
            db_email_function.delate_multi_tags(self.db_connection,query_list)
        else:
            db_email_function.multi_insert_tag(query_list,self.db_connection)
        load_data_from_database(self)
        # print(last_row)
        self.ui.tableWidget.selectRow(last_row[-1].row())
        self.ui.tableWidget.verticalScrollBar().setValue(scroll_pos)
        
        self.load_clicked_email(last_row[-1].row(),0)


    def clicket_hamburger(self):
        self.ui.centerMenu.expandMenu()
        self.ui.meilBoxBtn.setCheckable(True)
    def open_label_page(self):
        load_all_labels(self)
        self.ui.mainPages.setCurrentIndex(0)
    
    def jump_to_page(self):
        nr_page = self.ui.jumpToPagelineEdit.text().lower()
        if  isinstance(int(nr_page),int):
            if int(nr_page) < 0:
                self.current_page = 0 
            elif int(nr_page) >= 1 and int(nr_page) < self.max_page :
                self.current_page = (int(nr_page) - 1)
            elif int(nr_page) > 1 and  int(nr_page) > self.max_page:
                self.current_page = self.max_page - 1
        else:
            self.current_page = 0 
        load_data_from_database(self)

    @Slot(str,name="test")
    def date_wornig(self, text):
        '''Funkca wyświetla okno dialogowe z komuniektem:
        "Zakończenia exportu" '''
     
        #self.ui.sqlEmailDbName.setText(text)
        
        # print(self.main)
        msgBox = QMessageBox(parent=self.main)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
    
        #msgBox.exec()
    @Slot(int,int)
    def export_progrs(self,all_count_export,count_export):
        ''''''
        self.ui.exportCountLabel.setText(f"Eksport:{count_export} / {all_count_export}")
        self.ui.progressBar.setValue(count_export)
       
    
    def show_context_menu(self, pos):
        context_widget = self.ui.EmailtabWidget.findChild(QLabel, "body")
        context_menu = LabelContextMenu(self.main, self.db_connection,self,path=self.path)
        context_menu.show(pos, context_widget)

    def show_context_menu_email_body(self,pos):
        context_widget = self.ui.page.findChild(QLabel, "body_2")
        context_menu = EditLabelContextMenu(self.main, self.db_connection,self,path= self.path)
        context_menu.show(pos, context_widget)

    def add_lebels_to_db(self,id_labels_name,selected_text):
        db_email_function.add_label(self.db_connection,id_labels_name,self.id_selected_email,selected_text)
        add_labels_worning()
        self.load_clicked_email(self.ui.tableWidget.currentRow(),0)
    def set_labels(self,id_labels):
        # print(self.ui.body.selectedText())
        if self.ui.body.selectedText() is not None and self.ui.body.selectedText()!="":
            db_email_function.add_label(self.db_connection,id_labels,self.id_selected_email,self.ui.body.selectedText())
            add_labels_worning()
        
            self.load_clicked_email(self.ui.tableWidget.currentRow(),0)
    def show_heder_winodw(self):
        if self.ui.emailHederDockWidget.isHidden():
            self.ui.emailHederDockWidget.setFloating(True)
            self.ui.emailHederDockWidget.show()
            screen_geometry = QApplication.primaryScreen().availableGeometry()
            # print(self.main)
            window_geometry = self.main.frameGeometry()
            center_point = screen_geometry.center()
            window_geometry.moveCenter(center_point)
            self.ui.emailHederDockWidget.move(window_geometry.center())
        else:
            self.ui.emailHederDockWidget.hide()



    def serch_by_date_start(self):
        dialog_calendar = DateRangeDialog()
        
        date = dialog_calendar.get_selected_dates()
        # print(date)
        # print(date[0])
        if date[0] != "":
            # print(date[0])
            start_date = QDate.fromString(date[0], "yyyy-MM-dd")
            if self.active_filters['date_to'] !="":
                filter_end_date = QDate.fromString(self.active_filters['date_to'], "yyyy-MM-dd")
                if start_date > filter_end_date:
                    self.ui.startDataLabel.setText("")
                    self.ui.endDataLabel.setText("")
                else:
                    self.ui.startDataLabel.setText(date[0])
            else:
                self.ui.startDataLabel.setText(date[0])
        else:
            self.ui.startDataLabel.setText("")

        if date[1] != "":
            # print(date[1])
            end_date = QDate.fromString(date[1], "yyyy-MM-dd")
            if self.active_filters['date_fr'] !="":
                filter_start_date = QDate.fromString(self.active_filters['date_fr'], "yyyy-MM-dd")
                if end_date < filter_start_date:
                    self.ui.endDataLabel.setText("")
                    self.ui.startDataLabel.setText("")
                else:
                    self.ui.endDataLabel.setText(date[1])
            else:
                self.ui.endDataLabel.setText(date[1])
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
        self.ui.mainPages.setCurrentIndex(1)
        #print(os.path.join(self.path,item.text().split('.')[0],item.text()))
        logger.info(f"")
        if not self.db_connection is None: 
            self.db_connection.close()
            print("zamknięto polaczenie")
        self.current_page = 0
        # print(self.path)
        db_path = os.path.join(self.path,item.text().removesuffix('.sqlite'),item.text())
        print(db_path)
        
        db_email_function.connect_to_database(self,db_path+".sqlite")
        
        sql_name = db_path.split('\\')[-1]
        sql_name = sql_name.removesuffix('.sqlite')
        self.sql_name = sql_name
        self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(sql_name)
        load_color_dictionery(self)
 

        # print(self.tag_color)
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
            selected_list = self.active_filters['tag']
            selected_list = selected_list.replace("#_empty_#","BRAK KATEGORI")
            self.ui.selectedTagLabel.setText(f"Wybrane kategorie: {self.active_filters['tag'].removeprefix("(").removesuffix(")")}")
            self.current_page = 0
            load_data_from_database(self)
    
       
    def open_dialog_export_selector_to_pdf(self):
        '''Funkcja wyswietlajaca okno dialogowe opcji exportu plikow do PDF'''
        dialog = ExportSelector()
        if dialog.exec_() == QDialog.Accepted:
            selected_option = dialog.get_selected_option()
            is_checkBox_checked = dialog.get_checkBox_state()
            export_to_pdf(self,self.db_connection,self.path,self.sql_name,self.active_filters,selected_option,is_checkBox_checked)
            
    def open_dialog_export_selector_to_exel(self):
        '''Funkcja wyswietlajaca okno dialogowe opcji exportu plikow do exele'''
        dialog = ExportSelector()
        if dialog.exec_() == QDialog.Accepted:
            selected_option = dialog.get_selected_option()
            is_checkBox_checked = dialog.get_checkBox_state()
            export_to_excel(self,self.db_connection,self.path,self.sql_name,self.active_filters,selected_option,is_checkBox_checked)
    
    def set_color_label(self,color,border):
        '''Funkcja do stylowanie labelek(przycikow) w dolnej czesci widoku gluwnego GUI'''
        if border:
            return f"""background-color: {color}; color: black;border-radius: 6px;padding: 2px 6px;font-size: 11px;border: 1px solid black;"""
        else:
            return f"""background-color: {color}; color: black;border-radius: 6px;padding: 2px 6px;font-size: 11px;border:none;"""            

    def load_clicked_email(self,row,column):
        '''Funkcja wyświetla kliknienty emeil z tabeli glownej w ramce w prawej czesci GUI'''
        id = self.ui.tableWidget.item(row,0).text()
        tag_list_widget = self.ui.tableWidget.cellWidget(row,6)
        tag_list_layout = tag_list_widget.layout()
        tag_list = []
        if tag_list_layout is not None: 
            if tag_list_layout.count() > 0:
                for i in range(tag_list_layout.count()):
                    widget = tag_list_layout.itemAt(i).widget()
                    tag_list.append(widget.text())

        down_tag_widget =  self.ui.downTagWidget
        layout_tag_widget = down_tag_widget.layout()
        if layout_tag_widget is not None:
            if layout_tag_widget.count() > 0:
                for i in range(layout_tag_widget.count()):
                    if tag_list:
                        if layout_tag_widget.itemAt(i).widget().text() in tag_list:
                            tag_widget = layout_tag_widget.itemAt(i).widget()
                            tag = layout_tag_widget.itemAt(i).widget().text()
                            color = self.tag_color[tag]
                            if not color:
                                hash_object = hashlib.md5(tag.encode())
                                hex_color = '#' + hash_object.hexdigest()[:6]
                                color = hex_color
                                self.tag_color[tag] = color
                            tag_widget.setStyleSheet(self.set_color_label(color,False))
                        else:
                            tag_widget = layout_tag_widget.itemAt(i).widget()
                            tag_widget.setStyleSheet(self.set_color_label("#FFFFFF",True))
                    else:
                        tag_widget = layout_tag_widget.itemAt(i).widget()
                        tag_widget.setStyleSheet(self.set_color_label("#FFFFFF",True))
        down_label_widget =  self.ui.downLabelWidget
        layout_label_widget = down_label_widget.layout()

        label_list = db_email_function.get_unique_email_label_name(self.db_connection,id,self.sql_name)
        label_list = [item[0] for item in label_list]
        #print(label_list)
        if layout_label_widget is not None:
            if layout_label_widget.count() > 0:
                for i in range(layout_label_widget.count()):
                    if label_list:
                        #print(layout_label_widget.itemAt(i).widget().text())
                        if layout_label_widget.itemAt(i).widget().text() in label_list:
                            layout_widget = layout_label_widget.itemAt(i).widget()
                            hash_object = hashlib.md5(layout_label_widget.itemAt(i).widget().text().encode())
                            hex_color = '#' + hash_object.hexdigest()[:6]
                            layout_widget.setStyleSheet(self.set_color_label(hex_color,False))
                        else:
                            layout_widget = layout_label_widget.itemAt(i).widget()
                            layout_widget.setStyleSheet(self.set_color_label("#FFFFFF",True))
                    else:
                        for i in range(layout_label_widget.count()):
                            layout_widget = layout_label_widget.itemAt(i).widget()
                            layout_widget.setStyleSheet(self.set_color_label("#FFFFFF",True))
        #print(self.active_filters)
        self.id_selected_email = id
        # print(id)
        query =f'''
        SELECT * from emails WHERE id = {id}
        '''
        for x in range(self.ui.EmailtabWidget.count() - 1, 0, -1):
            self.ui.EmailtabWidget.removeTab(x)
        body_label = self.ui.EmailtabWidget.findChild(QLabel, "body")
        subject_label = self.ui.EmailtabWidget.findChild(QLabel, "subject")
        sender_label = self.ui.EmailtabWidget.findChild(QLabel, "sender")
        date_label = self.ui.EmailtabWidget.findChild(QLabel, "date")
        recipients_label = self.ui.EmailtabWidget.findChild(QLabel, "recipientsLabel")

        cc_widget = self.ui.EmailtabWidget.findChild(QWidget, "ccWidget")
        cc_label = self.ui.EmailtabWidget.findChild(QLabel, "ccLabel")
        bcc_label = self.ui.EmailtabWidget.findChild(QLabel, "bccLabel")
        bcc_widget = self.ui.EmailtabWidget.findChild(QWidget, "bccWidget")

        header_email_label = self.ui.emailHederDockWidget.findChild(QLabel,"headerEmailLabel")
        header_email_id_label = self.ui.emailHederDockWidget.findChild(QLabel,"idEmailHeaderLabel")
        header_email_id_label.setText(str(id))
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania emaeila o id:{id} z bazą danych:{self.sql_name} {e}")
            print(f"Błąd podczas pobierania emaeila o id:{id} z bazą danych:{self.sql_name} {e}")

        emai_value = cursor.fetchall()
        try:
            query_attachments = f'''SELECT * FROM attachments WHERE email_id ={emai_value[0][0]}'''
            cursor.execute(query_attachments)
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania zalacznikow z bazą danych:{self.sql_name} {e}")
            print(f"Błąd podczas pobierania zalacznikow z bazą danych:{self.sql_name} {e}")

        attachments_value = cursor.fetchall()
        if len(attachments_value) > 0:
            listAttachments = self.ui.EmailtabWidget.findChild(QListWidget, "listAttachments")
            listAttachments.clear()
            listAttachments.show()
            def on_item_clicked(item):
                widget = listAttachments.itemWidget(item)
                if widget:
                    widget.preview_file()
            for _, file_name, extra_value in attachments_value:
                file_path = os.path.join(self.path,self.sql_name,"Attachments",str(self.id_selected_email),file_name)
                # print(file_path)
                widget = FileListItem(f"{file_name}",file_path,self.ui.EmailtabWidget)  
                item = QListWidgetItem(listAttachments)
                item.setSizeHint(widget.sizeHint())  
                listAttachments.addItem(item)  
                listAttachments.setItemWidget(item, widget)
            listAttachments.itemClicked.disconnect()
            listAttachments.itemClicked.connect(lambda item: on_item_clicked(item))
            listAttachments.setFixedHeight(60)
        else:
            self.ui.EmailtabWidget.findChild(QListWidget, "listAttachments").hide()
        search_term = self.active_filters['body']
        search_term = db_email_function.word_to_highline(search_term)

        if isinstance(search_term, list):
            escaped_terms = [re.escape(term) for term in search_term if term] 
            pattern = re.compile('|'.join(escaped_terms), re.IGNOREfCASE)
        else:
            pattern = re.compile(re.escape(search_term), re.IGNORECASE)

        try:
            tekst = emai_value[0][8]
            body_label.setTextFormat(Qt.TextFormat.RichText)
            #print(emai_value[0][8])
            if emai_value[0][8] is not None:
                if isinstance(emai_value[0][8],str):
                    tekst = emai_value[0][8]
                else:
                    tekst = emai_value[0][8].decode("utf-8")
                

                tekst_html = tekst.replace('\n', '<br>')
                if(search_term ==""):
                    body_label.setText(tekst_html)
                    
                else:
                    tekst_html = tekst.replace('\n', '<br>')
                    highlighted_content = pattern.sub(lambda match: f"<span style='background-color: yellow;'>{match.group()}</span>",tekst_html)
                    body_label.setTextFormat(Qt.TextFormat.RichText)    
                    body_label.setText(highlighted_content)
            else:
                #emai_value[0][8]=""
                tekst = ""
                body_label.setText("")
        except:
            logger.error(f"Błąd podczas parsowania body wiadomości email id:{id} {e}")
            print(f"Błąd podczas parsowania body wiadomości email id:{id} {e}")
        try:
            subject_label.setText(emai_value[0][7])
            sender_label.setText(emai_value[0][3])
            date_label.setText(emai_value[0][1])
            recipients_label.setText(emai_value[0][4])
            header_email_label.setText(emai_value[0][11])
            if emai_value[0][6] is None:
                bcc_widget.hide()
            else:
                bcc_widget.show()
                bcc_label.setText(emai_value[0][6])
            if emai_value[0][5] is None:
                cc_widget.hide()
            else:
                cc_widget.show()
                cc_label.setText(emai_value[0][5])
        except:
            logger.error(f"Błąd podczas parsowania usawiania wartosci meta_danych email id:{id} {e}")
            print(f"Błąd podczas parsowania usawiania wartosci meta_danych email id:{id} {e}")

    def clear_filtr(self):
        self.ui.seachName.setText("")
        self.ui.seachSurname.setText("")
        self.ui.searchDate.setText("")
        self.ui.searchBody.setText("")
        self.ui.startDataLabel.setText("")
        self.ui.endDataLabel.setText("")
        self.ui.selectedTagLabel.setText("")
        self.ui.dirNameLabel.setText("")
        self.ui.show_flags_btn.setChecked(False)
        #selected_tag_label = self.ui.emailHederDockWidget.findChild(QLabel,"selected_tag_label")
        self.ui.selectedTagLabel.setText("")
        self.active_filters["sender_email"] = ""
        self.active_filters["recipients"] = ""
        self.active_filters["subject"] = ""
        self.active_filters["body"] = ""
        self.active_filters["tag"] = ""
        self.active_filters["folder_id"] = "1"
        self.active_filters["date_fr"] = ""
        self.active_filters["date_to"] = ""
        self.active_filters["flag"] = "False"

        load_data_from_database(self)

    def tree_email_dir_clicked(self,item ,column):
        self.clear_filtr()
        self.active_filters["folder_id"] = item.data(0,1)
        if item.data(0,1) != "1":
            dir_path = db_email_function.get_folder_path(self.db_connection, item.data(0,1))
            self.ui.dirNameLabel.setText(str(dir_path[0][0]))
        self.ui.mainPages.setCurrentIndex(1)
        self.current_page = 0
        #print(self.current_page)
        load_data_from_database(self)
            
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
        load_color_dictionery(self)
        dialog = MultiTagSelector(email_id,self.sql_name, self.db_connection, self.main, self.path)
        dialog.load_tags()
        if dialog.exec():
            logger.info(f"Zaktualizowano kategorie dla użytkownika {email_id}")
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
        self.active_filters["sender_email"] = self.ui.seachName.text().lower()
        self.active_filters["recipients"] = self.ui.seachSurname.text().lower()
        self.active_filters["subject"] = self.ui.searchDate.text().lower()
        self.active_filters["date_fr"] = self.ui.startDataLabel.text().lower()
        self.active_filters["date_to"] = self.ui.endDataLabel.text().lower()
        self.active_filters["body"] = self.ui.searchBody.text().lower()
        # fitr pod flaga w innym miejscu (toggle_filter_flags)
    def join_search(self):
        self.load_filtr_dict()
        self.current_page = 0 
        load_data_from_database(self)
        if( self.ui.tableWidget.rowCount() > 0):
            self.load_clicked_email(0,0)
            self.ui.tableWidget.selectRow(0)      

    def show_column_menu(self, position: QPoint) -> None:
        """Wyświetla menu kontekstowe dla nagłówka kolumny."""
        header = self.ui.tableWidget.horizontalHeader()
        column = header.logicalIndexAt(position)
        menu = QMenu(self.main)
        sort_asc_action = QAction("Sortuj rosnąco", self.main)
        sort_desc_action = QAction("Sortuj malejąco", self.main)
        hide_column_action = QAction("Ukryj kolumnę", self.main)

        if column == 6:
            add_tag_action = QAction("Dodaj kategorie", self.main)
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

    def open_add_tag_dialog(self) -> None:
        """Otwiera okno dialogowe umożliwiające dodanie nowego tagu."""
        dialog = MultiTagInputDialog(self.db_connection, self.main)
        if dialog.exec():
            logger.info("Nowa kategoria została dodana.")
            #load_data_from_database(self)

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
                            sql_list_file.append(sq_file.name.removesuffix('.sqlite'))


        if self.db_connection is None and len(sql_list_file) > 0 :
            try:
                #db_path = os.path.join(self.path,item.text().removesuffix('.sqlite'),item.text())
                # print(f"sql_list[0]: {sql_list_file[0]}")
                db_email_function.connect_to_database(self,path_to_dir+"\\"+sql_list_file[0].removesuffix('.sqlite')+"\\"+sql_list_file[0]+".sqlite")
                load_color_dictionery(self)
                load_data_from_database(self)
                
                self.sql_name =sql_list_file[0].removesuffix('.sqlite')
                
                self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(self.sql_name)
                
                logger.info(f"Połączono z pierwszą odnalezioną bazą SQLite: {self.sql_name}")
            except Exception as e:
                logger.error(f"Bład przy pierwszym łaczeniu do SQLite: {e}")
        # print(sql_list_file)
        self.list_widget.addItems(sql_list_file)    
        layout = self.ui.helpPage.layout()
        layout.addWidget(self.list_widget)
        
    
    
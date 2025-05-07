import sqlite3
import logging
from typing import Any, List, Dict, Optional
import pandas as pd
from PySide6.QtCore import Qt, QSettings, QDir, QPoint,QDate
from PySide6.QtGui import QFont, QFontDatabase, QAction,QIcon
from PySide6.QtWidgets import (
    QCheckBox, QPushButton, QGraphicsScene, QTableWidgetItem, QMenu, QFileSystemModel,
    QTreeView, QVBoxLayout, QFileDialog, QMainWindow,QTabBar
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.pc_browser.pc_browser import pc_browser
from src.multi_tag_dialog import MultiTagInputDialog
from src.multi_tag_selector import MultiTagSelector
from src.viewers.display_chenger import display_file_content
from src.viewers.explorer_function import prev_item,histor_stack
from src.viewers.dir_viewers import DirViewers
from src.disc_image_reader.disc_viewer import DiscViewers
from src.style_app import style_app
from src.db_function.pc_db import database_pc_manager
from src.firenet_viewer_widget.calendar_dialog_widget import DateRangeDialog
import sys,os
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_resource_path(relative_path):
    """Zwraca poprawną ścieżkę do zasobów, obsługując tryb onefile"""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS  
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GUIFunctions:
    """ Klasa zawierająca funkcje obsługujące interfejs graficzny i logikę aplikacji. """
    def __init__(self, main_window: QMainWindow) -> None:
        self.main = main_window
        self.ui = main_window.ui
        self.db_connection: Optional[sqlite3.Connection] = None
        self.db_menager = None
        self.pc_browser = None
        self.download_history_filters: Dict[str, str] = {"url": "", "path": "", "start_date": "", "end_date": ""}
        self.history_browser_filters: Dict[str, str] = {"url": "","title": "", "visit_count": "0","start_date": "", "end_date": ""}
        self.history_browser_marge_filters: Dict[str, str] = {"name": "", "profile_name": "","u.id": ""}
        self.columns_hidden: List[bool] = [False] * 6
        self.filtering_active: bool = False
        self.current_sort_order: Dict[int, Any] = {}
        self.histor = histor_stack()
        self.back_hisotry = histor_stack()
        self.active_path =""
        self.img_path = ""
        self.statusWindowMaxymalize = True
        self._setup_ui()
        self.load_data_from_database()
        self.load_data_and_plot()
        self.organizationName = "FireNet"

    def _setup_ui(self) -> None:
        """Inicjalizacja interfejsu – ustawienia czcionki, motywu oraz połączenia sygnałów."""
        self.enable_column_rearrangement()
        self.load_product_sans_font()
        self.initialize_app_theme()
        self._connect_signals()
        self.inicialize_pc_browser()
        # Konfiguracja widoku drzewa katalogów
        self.ui.select_directory.clicked.connect(self.select_directory)
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath('')
        self.tree_view = QTreeView(self.main)
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setVisible(False)
        layout = QVBoxLayout(self.main)
        layout.addWidget(self.tree_view)

        #Dodanie pierwszej strony do eksploratora plikow
        self.explorer = DirViewers(parent=self)
        self.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget").addTab(self.explorer,"last_patch_part")
        tab_bar = self.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget").tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)

        self.disc_imgae_explorer = DiscViewers(parent=self)
        self.ui.tabWidget_2.addTab(self.disc_imgae_explorer,"DISC_IMG")
        tab_bar = self.ui.tabWidget_2.tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)  
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
        self.ui.restoreBtn.clicked.connect(self.toggle_window_state)
        self.ui.minimalizeBtn.clicked.connect(self.minimalize)
        #ładowanie mofelu obrazu dysku
        #self.ui.select_img_disc_btn.clicked.connect(lambda)
        #Left Menu 
        #print(self.ui.mainPages)
        
        self.ui.eksploratorImgBtn.clicked.connect(lambda: self.ui.customQStackedWidget.setCurrentIndex(4))

        # Obsługa wyszukiwania i filtrów
        # self.ui.searchBtn.clicked.connect(self.show_search_results)
        # self.ui.seachName.returnPressed.connect(self.search_by_first_name)
        # self.ui.seachSurname.returnPressed.connect(self.search_by_last_name)
        # self.ui.searchDate.returnPressed.connect(self.search_by_birth_date)
        # self.ui.serachOld.returnPressed.connect(self.search_by_age)
        # self.ui.filter_table_btn.clicked.connect(self.apply_filters)
        # self.ui.show_table_btn.clicked.connect(self.show_all_columns)
        # self.ui.show_flags_btn.clicked.connect(self.toggle_filter_flags)
        # self.ui.export_pdf.clicked.connect(self.export_to_pdf)
        # self.ui.export_excel.clicked.connect(self.export_to_excel)
        # self.ui.pst_files_btn.clicked.connect(self.upload_pst_file)
        
        #główne przyciski
        self.ui.up_btn.clicked.connect(lambda :display_file_content(self,prev_item(self,self.ui.pathLabel.text())))
        
        self.ui.up_btn_2.clicked.connect(lambda : self.disc_imgae_explorer.prevItem(self))
        #Podłączenie zamknięcia karty exploratora 
        self.ui.tabWidget.tabCloseRequested.connect(lambda index: self.ui.tabWidget.removeTab(index))
        self.ui.tabWidget_2.tabCloseRequested.connect(lambda index: self.ui.tabWidget_2.removeTab(index))
        #Przyciski do obsługi histoiri przeglądania
        # self.ui.left_btn.clicked.connect()
        # self.ui.rigth_btn.clicked.connect()
        self.ui.left_btn.hide()
        self.ui.rigth_btn.hide()        
        # Konfiguracja menu nagłówka tabeli
        header = self.ui.tableWidget.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_column_menu)
        style =  style_app(self)
        style.set_style()
        
        self._tymczasowe_ukrycie()

    def _tymczasowe_ukrycie(self):
        #self.ui.dataBtn.hide()
        pass
    
    def inicialize_pc_browser(self):
        first_path = "C:\\Users\\firenet\\FirenetViewer\\pc_storage\\sqlite\\os_extraction.db"

        self.db_menager = database_pc_manager(first_path)
        self.db_menager.connect_to_db(first_path)

        self.ui.customQStackedWidget.setCurrentIndex(5)
        self.pc_browser = pc_browser(first_path,self,self.db_menager)
        self.pc_browser.load_device_info()
        self.pc_browser.load_software_info()
        self.pc_browser.load_network_config()
        self.pc_browser.load_installed_software()
        self.pc_browser.load_borowser_download_history('google_chrome_dowsnloads')
        self.pc_browser.load_history_browser()
        self.pc_browser.generate_pc_tree()
        self.pc_browser.generate_sercher_history_browser_combo_box()

        self.ui.domenaLineEdit.editingFinished.connect(self.update_domena_filter)
        self.ui.titleLineEdit.editingFinished.connect(self.update_title_filter)
        self.ui.visitCountLineEdit.editingFinished.connect(self.update_visit_count_filter)
        self.ui.browserComboBox.currentTextChanged.connect(self.update_browser_name_filter)
        self.ui.profileComboBox.currentTextChanged.connect(self.update_profile_name_filter)
        self.ui.userComboBox.currentTextChanged.connect(self.update_user_name_id_filter)
        self.ui.calendarBtn.clicked.connect(self.serch_by_date_start)
        self.ui.startDateLineEdit.textChanged.connect(self.update_data_filter)
        self.ui.endDatelineEdit.textChanged.connect(self.update_data_filter)

    def update_data_filter(self):
        self.history_browser_filters["start_date"] = self.ui.startDateLineEdit.text()
        self.history_browser_filters["end_date"] = self.ui.endDatelineEdit.text()
        self.pc_browser.load_history_browser()
    def update_domena_filter(self):
        self.history_browser_filters["url"] = self.ui.domenaLineEdit.text()
        self.pc_browser.load_history_browser()

    def update_title_filter(self):
        self.history_browser_filters["title"] = self.ui.titleLineEdit.text()
        self.pc_browser.load_history_browser()

    def update_visit_count_filter(self):
        count = self.ui.visitCountLineEdit.text()
        if count == "":
            self.history_browser_filters["visit_count"] = "0"
            self.pc_browser.load_history_browser()
        else:
            try:
                count = int(count)
                self.history_browser_filters["visit_count"] = count
                self.pc_browser.load_history_browser()
            except ValueError:
                logger.error("Invalid visit count value")
                self.ui.visitCountLineEdit.setText("0")

    def update_profile_name_filter(self):
        if self.ui.profileComboBox.currentText() == "Wszystkie":
            self.history_browser_marge_filters["profile_name"] = ""
            self.pc_browser.load_history_browser()
        else:
            self.history_browser_marge_filters["profile_name"] = self.ui.profileComboBox.currentText()
        self.pc_browser.load_history_browser()

    def update_browser_name_filter(self):
        if self.ui.browserComboBox.currentText() == "Wszystkie":
            self.history_browser_marge_filters["name"] = ""
            self.pc_browser.load_history_browser()
        else:
            self.history_browser_marge_filters["name"] = self.ui.browserComboBox.currentText()
        self.pc_browser.load_history_browser()
        #self.history_browser_filters["visit_count"] = self.ui.visitCountLineEdit.text()

    def update_user_name_id_filter(self):
        if self.ui.userComboBox.currentText() == "Wszystkie":
            self.history_browser_marge_filters["u.id"] = ""
            self.pc_browser.load_history_browser()
        else:
            self.history_browser_marge_filters["u.id"] = self.ui.userComboBox.currentData()
            print(self.history_browser_marge_filters["u.id"])
        self.pc_browser.load_history_browser()
    def toggle_window_state(self):
        self.ui.restoreBtn.setIcon(QIcon(":feather/FFFFFF/feather/copy.png"))
        #print(self.main.windowState())
        state = self.main.windowState()
        if self.statusWindowMaxymalize:
            self.main.showNormal()
            self.statusWindowMaxymalize=False
        else:
            self.main.showMaximized()
            self.statusWindowMaxymalize=True
    def minimalize(self):
        self.main.showMinimized()

    def load_data_from_database(self) -> None:
        """
        Wczytuje dane z bazy SQLite i wypełnia tabelę widżetem.
        Używa zapytania SQL z lewym łączeniem, aby zebrać informacje o użytkownikach oraz ich tagach.
        """
        if not self.db_connection:
            logger.error("Brak połączenia z bazą danych.")
            return

        query = '''
            SELECT u.id, u.first_name, u.second_name, u.date_of_birth, u.age, u.flag,
                   GROUP_CONCAT(t.tag_name) AS tags 
            FROM users u
            LEFT JOIN user_tags ut ON u.id = ut.user_id
            LEFT JOIN tags t ON ut.tag_id = t.id
            GROUP BY u.id
        '''
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(6)

            for row_idx, row_data in enumerate(data):
                user_id = row_data[0]
                for col_idx, cell_data in enumerate(row_data[1:]):
                    if col_idx == 4:
                        checkbox = QCheckBox()
                        checkbox.setChecked(bool(cell_data))
                        checkbox.stateChanged.connect(
                            lambda state, uid=user_id: self.update_flag(uid, state)
                        )
                        self.ui.tableWidget.setCellWidget(row_idx, col_idx, checkbox)
                    elif col_idx == 5:
                        btn = QPushButton("Pokaż tagi")
                        btn.clicked.connect(lambda _, uid=user_id: self.open_tag_selector(uid))
                        self.ui.tableWidget.setCellWidget(row_idx, col_idx, btn)
                    else:
                        item = QTableWidgetItem(str(cell_data) if cell_data else "")
                        self.ui.tableWidget.setItem(row_idx, col_idx, item)
            logger.info("Dane zostały załadowane do tabeli.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas wykonywania zapytania: {e}")

    def serch_by_date_start(self):
        dialog_calendar = DateRangeDialog()
        
        date = dialog_calendar.get_selected_dates()
        # print(date)
        # print(date[0])
        if date[0] != "":
            # print(date[0])
            start_date = QDate.fromString(date[0], "yyyy-MM-dd")
            if self.history_browser_filters['start_date'] !="":
                filter_end_date = QDate.fromString(self.history_browser_filters['start_date'], "yyyy-MM-dd")
                if start_date > filter_end_date:
                    self.ui.startDateLineEdit.setText("")
                    self.ui.endDatelineEdit.setText("")
                else:
                    self.ui.startDateLineEdit.setText(date[0])
            else:
                self.ui.startDateLineEdit.setText(date[0])
        else:
            self.ui.startDateLineEdit.setText("")

        if date[1] != "":
            # print(date[1])
            end_date = QDate.fromString(date[1], "yyyy-MM-dd")
            if self.history_browser_filters['end_date'] !="":
                filter_start_date = QDate.fromString(self.history_browser_filters['end_date'], "yyyy-MM-dd")
                if end_date < filter_start_date:
                    self.ui.endDatelineEdit.setText("")
                    self.ui.startDataLabel.setText("")
                else:
                    self.ui.endDatelineEdit.setText(date[1])
            else:
                self.ui.endDatelineEdit.setText(date[1])
        else:
            self.ui.endDatelineEdit.setText("")

    def open_tag_selector(self, user_id: int) -> None:
        """Otwiera okno dialogowe do edycji tagów użytkownika."""
        dialog = MultiTagSelector(user_id, self.db_connection, self.main)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika {user_id}")
            self.load_data_from_database()

    def update_flag(self, user_id: int, state: int) -> None:
        """Aktualizuje flagę użytkownika w bazie danych."""
        flag_value = 1 if state else 0
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE users SET flag = ? WHERE id = ?", (flag_value, user_id))
            self.db_connection.commit()
            logger.info(f"Updated flag for user ID {user_id} to {flag_value}.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizacji flagi: {e}")

    def update_tag(self, user_id: int, tag_name: str) -> None:
        """Aktualizuje tag przypisany do użytkownika."""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id FROM tags WHERE tag_name = ?", (tag_name,))
            tag_id = cursor.fetchone()
            if tag_id:
                cursor.execute("UPDATE users SET tag_id = ? WHERE id = ?", (tag_id[0], user_id))
                self.db_connection.commit()
                logger.info(f"Updated tag for user ID {user_id} to {tag_name}.")
            else:
                logger.warning(f"Tag name '{tag_name}' not found.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizacji tagu: {e}")

    def close_database_connection(self) -> None:
        if self.db_connection:
            self.db_connection.close()

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


    def apply_filters(self) -> None:
        """
        Przechodzi przez wszystkie wiersze tabeli i ukrywa te,
        które nie spełniają kryteriów aktywnych filtrów.
        """
        for row in range(self.ui.tableWidget.rowCount()):
            row_matches = True
            for column, query in self.active_filters.items():
                if query:
                    item = self.ui.tableWidget.item(row, column)
                    if not (item and query in item.text().lower()):
                        row_matches = False
                        break
            self.ui.tableWidget.setRowHidden(row, not row_matches)

    def show_column_menu(self, position: QPoint) -> None:
        """Wyświetla menu kontekstowe dla nagłówka kolumny."""
        header = self.ui.tableWidget.horizontalHeader()
        column = header.logicalIndexAt(position)
        menu = QMenu(self.main)
        sort_asc_action = QAction("Sortuj rosnąco", self.main)
        sort_desc_action = QAction("Sortuj malejąco", self.main)
        hide_column_action = QAction("Ukryj kolumnę", self.main)

        if column == 5:
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

    def load_data_and_plot(self) -> None:
        """Wczytuje dane (wiek użytkowników) i tworzy wykres."""
        if not self.db_connection:
            return
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT age FROM users")
            ages = [row[0] for row in cursor.fetchall()]
            self.plot_data(ages)
        except sqlite3.Error as e:
            logger.error(f"Error fetching data: {e}")

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
            self.load_data_from_database()

    def toggle_filter_flags(self) -> None:
        """Przełącza tryb filtrowania według zaznaczonych flag."""
        if self.filtering_active:
            self.reset_filters()
        else:
            self.filter_checked_flags()
        self.filtering_active = not self.filtering_active

    def filter_checked_flags(self) -> None:
        """Ukrywa wiersze, w których flaga nie jest zaznaczona."""
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox = self.ui.tableWidget.cellWidget(row, 4)
            if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                self.ui.tableWidget.showRow(row)
            else:
                self.ui.tableWidget.hideRow(row)

    def reset_filters(self) -> None:
        """Przywraca widoczność wszystkich wierszy tabeli."""
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.showRow(row)

    def export_to_pdf(self) -> None:
        """Eksportuje widoczne dane tabeli do pliku PDF."""
        file_path, _ = QFileDialog.getSaveFileName(
            self.main, "Zapisz plik PDF", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if not file_path:
            return
        if not file_path.endswith(".pdf"):
            file_path += ".pdf"
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 30, "Przefiltrowane dane z tabeli")
        c.setFont("Helvetica", 12)
        row_height = 20
        start_y = height - 60

        for row in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.isRowHidden(row):
                continue
            row_data = []
            for column in range(self.ui.tableWidget.columnCount()):
                if column == 4:
                    widget = self.ui.tableWidget.cellWidget(row, column)
                    row_data.append("Tak" if isinstance(widget, QCheckBox) and widget.isChecked() else "Nie")
                else:
                    item = self.ui.tableWidget.item(row, column)
                    row_data.append(item.text() if item else "")
            c.drawString(30, start_y - row * row_height, ", ".join(row_data))
        c.save()
        logger.info(f"Plik PDF zapisany jako: {file_path}")

    def export_to_excel(self) -> None:
        """Eksportuje widoczne dane tabeli do pliku Excel."""
        file_path, _ = QFileDialog.getSaveFileName(
            self.main, "Zapisz plik Excel", "", "Excel Files (*.xlsx);;All Files (*)"
        )
        if not file_path:
            return
        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"
        data = []
        for row in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.isRowHidden(row):
                continue
            row_data = []
            for column in range(self.ui.tableWidget.columnCount()):
                if column == 4:
                    widget = self.ui.tableWidget.cellWidget(row, column)
                    row_data.append("Tak" if isinstance(widget, QCheckBox) and widget.isChecked() else "Nie")
                else:
                    item = self.ui.tableWidget.item(row, column)
                    row_data.append(item.text() if item else "")
            data.append(row_data)
        df = pd.DataFrame(data, columns=["Imię", "Nazwisko", "Data urodzenia", "Wiek", "Flagi", "Tagi"])
        df.to_excel(file_path, index=False)
        logger.info(f"Plik Excel zapisany jako: {file_path}")

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
        self.ui.pathLabel.setText(directory)
        display_file_content(self,directory)
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
            self.ui.pathLabel.setText(selected_file_path)

    def display_image_message(self, message: str) -> None:
        """Wyświetla komunikat (np. informujący o niedostępnej funkcjonalności)."""
        self.ui.pathLabel.setText(message)

    def upload_pst_file(self) -> None:
        """Pozwala wybrać plik PST i wywołuje funkcję jego przetwarzania."""
        pst_file, _ = QFileDialog.getOpenFileName(self.main, "Wybierz plik .pst", "", "PST Files (*.pst)")
        if pst_file:
            self.process_pst_file(pst_file)

    def process_pst_file(self, pst_file: str) -> None:
        """Przetwarza plik PST (implementację uzupełnij według potrzeb)."""
        logger.info(f"Przetwarzanie pliku PST: {pst_file}")

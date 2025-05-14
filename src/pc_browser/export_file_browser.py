import src.db_function.pc_db as pc_db
from PySide6.QtWidgets import QTableWidgetItem,QTableWidget, QHeaderView,QVBoxLayout,QLayout
from PySide6.QtCore import Qt,QTimer
import pandas as pd
import fitz
import os
import shutil
import logging
import sys 
import io

from typing import Any, List, Dict, Optional
from urllib.parse import urlparse
from datetime import datetime
from PySide6.QtGui import QStandardItemModel, QStandardItem,QPixmap
from src.db_function.export_file_db import database_file_export_menager
from src.pc_browser.key_press_filter import KeyPressFilterTableBrowsers
from src.firenet_viewer_widget.calendar_dialog_widget import DateRangeDialog
from src.viewers.wiget_generator import generator_wiget
from PySide6.QtCore import QDate
class export_file_browser:
    def __init__(self,parent ,db_menager : database_file_export_menager):
        self.db_menager = db_menager
        self.parent = parent
        self.focus_file_type = None
        self.export_file_gui_done = False
        self.file_storage = "D:\\DaneDoTestow\\Wyeksportowane pliki\\Pliki użytkowników"
        self.table_dict : Dict[str, str] = {}
        self.export_file_filters : Dict[str,str] = {"file_name":"", "file_size": "", "start_date":"", "end_date":""}
        #self.export_init_gui()

    def get_branch_tree_list(self):
        table_list = self.db_menager.get_all_table_list()
        branch_list = []
        other_file = False
        for table_name in table_list:
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
        if not self.export_file_gui_done:
            self.export_init_gui()
            self.export_file_gui_done = True
        rows = self.db_menager.get_contents_from_table(self.table_dict[self.focus_file_type],self.export_file_filters)
        self.parent.ui.exportFileTableWidget.setRowCount(0)
        self.parent.ui.exportFileTableWidget.setColumnCount(0)
        self.parent.ui.exportFileTableWidget.setColumnCount(4)
        self.parent.ui.exportFileTableWidget.setHorizontalHeaderLabels(["Id","Nazwa Pliku","Rozmiar","Data utworzenia"])
       
        for row in rows:
            row_position = self.parent.ui.exportFileTableWidget.rowCount()
            self.parent.ui.exportFileTableWidget.insertRow(row_position)
            for i, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.parent.ui.exportFileTableWidget.setItem(row_position, i, item)
        self.parent.ui.exportFileTableWidget.verticalHeader().setVisible(False)                
        self.parent.ui.exportFileTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_deteils_export_file(self,row,col):    
        id = self.parent.ui.exportFileTableWidget.item(row, 0).text()
        if self.focus_file_type != "Pozostałe":
            row = self.db_menager.get_full_deteils_export_file(id,self.table_dict[self.focus_file_type])
        else:
            row = self.db_menager.get_deteils_export_file(id,self.table_dict[self.focus_file_type])
        print(row)

        layout = self.parent.ui.fileExportWidget.findChild(QLayout, "contentLayout")
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)
            #self.parent.ui.fileExportWidget.setLayout(None)
        else:
            layout = QVBoxLayout()
            layout.setObjectName("contentLayout")
            self.parent.ui.fileExportWidget.setLayout(layout)

        ext = row[0][1].split(".")[-1]
        path = os.path.join(self.file_storage, row[0][1])
        if ext == "pdf":
            pdf_document = fitz.open(path)
            widget = generator_wiget(pdf_document,ext,widget = self.parent.ui.fileExportWidget)
        elif ext in ['jpg','jpeg','png','gif','bmp','ppm']:
            pix_map = QPixmap(path)
            widget = generator_wiget(pix_map,ext,widget = self.parent.ui.fileExportWidget)
        elif ext in['csv','xlsx','xls','odf','ods','xlsm','xlsb']:
            if ext == "csv":
                file = pd.read_csv(path)
            elif ext in['xlsx','xlsm','xlsb',]:
                file = pd.read_excel(path)
            elif ext in ['odf','ods']:
                file = pd.read_excel(path,engine="odf")
            elif ext in ['xls']:
                file = pd.read_excel(path,engine="xlrd")
            widget = generator_wiget(file,"csv")
        elif ext == "docx":
            widget = generator_wiget(path,"docx")
        elif ext in ['mp3','wav','ogg','flac','aac','m4a','mp4','avi','mkv','webm','mov','MP4']:
            widget = generator_wiget(path,"mp4")
        else:
            with open(path, "rb") as f:
                byte_stream = io.BytesIO(f.read())
            widget = generator_wiget(byte_stream,"."+ext,name = row[0][2])

        layout.addWidget(widget)

        self.parent.ui.fieleExportNameLabel.setText(row[0][2])
        self.parent.ui.fileExportPathLabel.setText(row[0][3])
        self.parent.ui.fileExportSizeLabel.setText(row[0][4])
        self.parent.ui.fileExportCreateDateLabel.setText(row[0][5])
        self.parent.ui.fileExportDateModyficatinLabel.setText(row[0][6])
        self.parent.ui.fileExportDateAccessLabel.setText(row[0][7])
        if self.focus_file_type != "Pozostałe":
            self.parent.ui.fileExportMetadataLabel.setText(row[0][8])
        else: 
            self.parent.ui.fileExportMetadataLabel.setText("Brak metadanych")

    def export_init_gui(self):
        self.parent.ui.exportFileTableWidget.cellClicked.connect(self.load_deteils_export_file)
        self.parent.ui.exportFileNameLineEdit.editingFinished.connect(lambda : self.update_filter(self.export_file_filters,"file_name",self.load_exported_file,self.parent.ui.exportFileNameLineEdit))
        # (lambda : self.update_filter(self.history_download_browser_filters,"download_path",self.load_borowser_download_history,self.parent.ui.fileNameLineEdit))
        self.key_filter_browser_history = KeyPressFilterTableBrowsers(self.parent.ui.exportFileTableWidget, self.load_deteils_export_file,self.load_deteils_export_file)
        self.parent.ui.exportFileTableWidget.installEventFilter(self.key_filter_browser_history)
        
        self.parent.ui.exportFileCalendarBtn.clicked.connect(lambda : self.serch_by_date_start(self.parent.ui.exportFileStartDateLineEdit,self.parent.ui.exportFileEndDateLineEdit,self.export_file_filters,"start_date","end_date"))
        self.parent.ui.exportFileStartDateLineEdit.textChanged.connect(lambda :self.update_data_filter(self.export_file_filters,"start_date","end_date",self.load_exported_file,self.parent.ui.exportFileStartDateLineEdit,self.parent.ui.exportFileEndDateLineEdit))
        self.parent.ui.exportFileEndDateLineEdit.textChanged.connect(lambda:self.update_data_filter(self.export_file_filters,"start_date","end_date",self.load_exported_file,self.parent.ui.exportFileStartDateLineEdit,self.parent.ui.exportFileEndDateLineEdit))
    
    def update_filter(self,filter_list,filter_key,load_function,line_edit):
        filter_list[filter_key] = line_edit.text()
        load_function()
    
    def update_data_filter(self,list_filter,stert_key,end_key,load_function,start_line_edit,end_line_edit):
        list_filter[stert_key] = start_line_edit.text()
        list_filter[end_key] = end_line_edit.text()
        load_function()

    def serch_by_date_start(self,start_data_lineEdit,end_data_lineEdit,list_filter,start_key,end_key):
        """Otwiera okno dialogowe do wyboru zakresu dat."""
        dialog_calendar = DateRangeDialog()
        
        date = dialog_calendar.get_selected_dates()
        # print(date)
        # print(date[0])
        if date[0] != "":
            # print(date[0])
            start_date = QDate.fromString(date[0], "yyyy-MM-dd")
            if list_filter[start_key] !="":
                filter_end_date = QDate.fromString(list_filter[start_key], "yyyy-MM-dd")
                if start_date > filter_end_date:
                    start_data_lineEdit.setText("")
                    end_data_lineEdit.setText("")
                else:
                    start_data_lineEdit.setText(date[0])
            else:
                start_data_lineEdit.setText(date[0])
        else:
            start_data_lineEdit.setText("")

        if date[1] != "":
            # print(date[1])
            end_date = QDate.fromString(date[1], "yyyy-MM-dd")
            if list_filter[end_key] !="":
                filter_start_date = QDate.fromString(list_filter[end_key], "yyyy-MM-dd")
                if end_date < filter_start_date:
                    end_data_lineEdit.setText("")
                    start_data_lineEdit.setText("")
                else:
                    end_data_lineEdit.setText(date[1])
            else:
                end_data_lineEdit.setText(date[1])
        else:
            end_data_lineEdit.setText("")

    
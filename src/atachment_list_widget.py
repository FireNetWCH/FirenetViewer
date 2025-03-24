from PySide6.QtWidgets import QApplication, QListWidget, QWidget, QPushButton, QHBoxLayout, QLabel, QListWidgetItem,QFileDialog,QFrame,QSizePolicy
from PySide6.QtGui import QPixmap,QIcon
from src.viewers.wiget_generator import generator_wiget
import pandas as pd
import fitz
import os
import shutil
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class FileListItem(QWidget):
    def __init__(self, filename,file_path, parent=None):
        super().__init__(parent)
        self.tab = parent
        self.file_name = filename
        self.file_path = file_path
        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)  
        layout.setSpacing(1)
        self.frame =QWidget(self)
        frame_layout = QHBoxLayout(self.frame)
        frame_layout.setContentsMargins(1, 1, 1, 1)
        frame_layout.setSpacing(1)
        self.label = QLabel(filename)
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.preview_button = QPushButton(QIcon("./Qss/icons/black/feather/link.png"), "")
        self.preview_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.preview_button.clicked.connect(self.preview_file)
        frame_layout.addWidget(self.label)
        frame_layout.addWidget(self.preview_button)
        frame_layout.addStretch()
        layout.addWidget(self.frame)
        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def preview_file(self):
        ext = self.file_name.split(".")[-1]
        print(ext)
        if ext in ['jpg','jpeg','png','gif','bmp','ppm']:
            file = QPixmap(self.file_path)
            tab_wiget = generator_wiget(file,".jpg")
            page_layout = tab_wiget.layout()
            page_layout.addWidget(self.download_pusch_btn())
            self.tab.addTab(tab_wiget,self.file_name)
            self.tab.setCurrentWidget(tab_wiget)
        elif ext in['csv','xlsx','xls','odf','ods','xlsm','xlsb']:
            if ext == "csv":
                file = pd.read_csv(self.file_path)
            elif ext in['xlsx','xlsm','xlsb',]:
                file = pd.read_excel(self.file_path)
            elif ext in ['odf','ods']:
                file = pd.read_excel(self.file_path,engine="odf")
            elif ext in ['xls']:
                file = pd.read_excel(self.file_path,engine="xlrd")
            tab_wiget = generator_wiget(file,".csv")
            page_layout = tab_wiget.layout()
            page_layout.addWidget(self.download_pusch_btn())
            self.tab.addTab(tab_wiget,self.file_name)
            self.tab.setCurrentWidget(tab_wiget)
        elif ext == 'pdf':
            pdf_document = fitz.open(self.file_path)
            tab_wiget = generator_wiget(pdf_document,".pdf")
            page_layout = tab_wiget.layout()
            page_layout.addWidget(self.download_pusch_btn())
            self.tab.addTab(tab_wiget,self.file_name)
            self.tab.setCurrentWidget(tab_wiget)
        elif ext in ['.txt', '.py', '.log']:  
            with open(self.file_path, "r", encoding="utf-8") as file:
                        txt = file.read()
            tab_wiget = generator_wiget(txt,".txt")
            page_layout = tab_wiget.layout()
            page_layout.addWidget(self.download_pusch_btn())
            self.tab.addTab(tab_wiget,self.file_name)
            self.tab.setCurrentWidget(tab_wiget)
        else:
            tab_wiget = generator_wiget(self.file_path,"")
            page_layout = tab_wiget.layout()
            page_layout.addWidget(self.download_pusch_btn())
            self.tab.addTab(tab_wiget,self.file_name)
            self.tab.setCurrentWidget(tab_wiget)
        


    def download_pusch_btn(self):
        downloadBtn = QPushButton(f"POBIERZ\n{self.file_name}")
        downloadBtn.setObjectName("standard")
        downloadBtn.setStyleSheet("QPushButton{font-weight: bold; border-radius: 5px;border: 2px solid #A0C8FF} QPushButton::hover{background-color:#A0C8FF}")
        print(downloadBtn)
        downloadBtn.clicked.connect(lambda : self.copy_file(self.file_path))
        return downloadBtn
    def copy_file(self,path):

        destination_path, _ = QFileDialog.getSaveFileName(None, "Zapisz plik jako",self.file_name, self.file_name.split('.')[-1])
        try:
         if destination_path:  
            shutil.copy(path, destination_path)
            print(f"Plik został skopiowany do: {destination_path}")
            logger.info(f"Plik został skopiowany do: {destination_path}")
        except Exception as e:
            print(f"Błąd podczas kopiowania pliku: {e}")
            logger.error(f"Błąd podczas kopiowania pliku: {e}")
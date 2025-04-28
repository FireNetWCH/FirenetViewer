from src.viewers.pdf_viewer import display_pdf_content
from src.viewers.img_viewer import display_img_content
from src.viewers.video_viewer import display_vidoe_content
from src.viewers.dir_viewers import display_dir_content
from src.viewers.docx_viewers import display_docx_content
from src.viewers.table_viewers import display_table_content
from src.viewers.txt_viewers import display_txt_content
from src.viewers.not_support_file import NotSupportFileView
from src.firenet_viewer_widget.downloadButtona import downloadButton
from src.disc_image_reader.download_menager import download_manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
import pytsk3
import os
import io
import pandas as pd
def display_file_content(self, file_path,history_flag = 1,file_system = None) -> None:
        """W zależności od rozszerzenia, wyświetla zawartość pliku lub komunikat o braku wsparcia.
          Jeśli flaga ustawiona jest na 0 nie dodaje przekazanej ścieżki do wyszukiwania"""
        #history_flag -> oznacza czy sciężka ma zostać dodana do histori szukania, czy ścieżka pochodzi z akcji cofnięcia w przód/tył

        if isinstance(file_path, str):
            try:
                print(file_path)
                _, ext = os.path.splitext(file_path.lower())
                if ext in ['.txt', '.py', '.log','.doc']:
                    self.ui.pathLabel.setText(file_path)
                    q_tab = self.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget")
                    with open(file_path, "r", encoding="utf-8") as file:
                        txt = file.read()
                    tab_content = display_txt_content(self,txt)
                    q_tab.addTab(tab_content,"TXT")
                    q_tab.setCurrentWidget(tab_content)
                    # if history_flag == 1:
                    #     self.history.append_history(file_path)
                elif ext in['.docx','.odt']:
                    display_docx_content(self,file_path)
                    self.ui.pathLabel.setText(file_path)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                elif ext in['.csv','.xlsx','.xls','.odf','.ods','.xlsm','.xlsb']:
                    self.ui.pathLabel.setText(file_path)
                    if ext == ".csv":
                        df = pd.read_csv(file_path)
                    elif ext in['.xlsx','.xlsm','.xlsb',]:
                        df = pd.read_excel(file_path)
                    elif ext in ['.odf','.ods','.odt']:
                        df = pd.read_excel(file_path,engine="odf")
                    elif ext in ['.xls']:
                        df = pd.read_excel(file_path,engine="xlrd")
                                    
                    tab_content = display_table_content(self, df,ext)
                    q_tab = self.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget")
                    q_tab.addTab(tab_content,"Image")
                    q_tab.setCurrentWidget(tab_content)

                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)      
                elif ext == '.pdf':
                    display_pdf_content(self,0,1, file_path)
                    self.ui.pathLabel.setText(file_path)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                elif ext in ['.jpg','.jpeg','.png','.gif','.bmp','.ppm']:
                    pixmap = QPixmap(file_path)
                    self.ui.pathLabel.setText(file_path)
                    q_tab = self.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget")
                    tab_content = display_img_content(self,pixmap)
                    q_tab.addTab(tab_content,"Exel")
                    q_tab.setCurrentWidget(tab_content)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                elif ext == '.pst':
                    self.display_image_message("PST files are in progress.")
                    self.ui.pathLabel.setText(file_path)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                elif ext in ['.mp3','.mp4','.avi','.mkv','.mov','.wmv','.flv','.ogv']:
                    display_vidoe_content(self,file_path)
                    self.ui.pathLabel.setText(file_path)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                elif os.path.isdir(file_path):
                    self.explorer.set_directory(file_path)
                    self.ui.pathLabel.setText(file_path)
                    # if history_flag == 1:
                    #     self.histor.append_history(file_path)
                else:
                    self.ui.pathLabel.setText(file_path)
            except Exception as e:
                self.ui.pathLabel.setText(f"Could not read file: {e}")
        
        else:
            try:
                _, ext = os.path.splitext(file_path.info.name.name.decode().lower())
                if ext in ['.jpg','.jpeg','.png','.gif','.bmp','.ppm']:
                    file_hoke = file_system.open_meta(file_path.info.name.meta_addr)
                    file_data = file_hoke.read_random(0,file_hoke.info.meta.size)
                    pixmap = QPixmap()
                    pixmap.loadFromData(file_data)
                    display_img_content(self,pixmap)
                    q_tab = self.ui.tabWidget_2
                    tab_content = display_img_content(self,pixmap)
                    dm = download_manager(file_path)
                    download_buttona = downloadButton(file_path.info.name.name.decode().lower(),lambda: dm.download_file_img())
                    q_tab = self.ui.tabWidget_2
                    tab_content.layout().addWidget(download_buttona, alignment=Qt.AlignCenter)
                    q_tab.addTab(tab_content,"IMG")
                    q_tab.setCurrentWidget(tab_content)

                elif ext in ['.txt', '.py', '.log']:
                    file_hoke = file_system.open_meta(file_path.info.name.meta_addr)
                    if file_hoke.info.meta.size > 0: 
                        file_data = file_hoke.read_random(0,file_hoke.info.meta.size)
                        txt = file_data.decode("utf-8")     
                        q_tab = self.ui.tabWidget_2
                        tab_content = display_txt_content(self,txt)
                        dm = download_manager(file_path)
                        download_buttona = downloadButton(file_path.info.name.name.decode().lower(),lambda: dm.download_file_img())
                        q_tab = self.ui.tabWidget_2
                        tab_content.layout().addWidget(download_buttona, alignment=Qt.AlignCenter)
                        q_tab.addTab(tab_content,"TXT")
                        q_tab.setCurrentWidget(tab_content)
                    else:
                        print("Plik jest pósty - 'dodać widget i logi '")
                elif ext in['.csv','.xlsx','.xls','.odf','.ods','.xlsm','.xlsb']:
                    file_hoke = file_system.open_meta(file_path.info.name.meta_addr)
                    file_data = file_hoke.read_random(0,file_hoke.info.meta.size)
                    if file_data is None:
                        return None

                    file_stream = io.BytesIO(file_data) 

                    if ext == ".csv":
                        df = pd.read_csv(file_stream)
                    elif ext in ['.xlsx', '.xlsm', '.xlsb']:
                        df = pd.read_excel(file_stream)
                    elif ext in ['.odf', '.ods', '.odt']:
                        df = pd.read_excel(file_stream, engine="odf")
                    elif ext == '.xls':
                        df = pd.read_excel(file_stream, engine="xlrd")
                    else:
                        print(f"Nieobsługiwane rozszerzenie: {ext}")
                        return None
                    tab_content = display_table_content(self, df,ext)
                    dm = download_manager(file_path)
                    download_buttona = downloadButton(file_path.info.name.name.decode().lower(),lambda: dm.download_file_img())
                    q_tab = self.ui.tabWidget_2
                    tab_content.layout().addWidget(download_buttona, alignment=Qt.AlignCenter)
                    q_tab.addTab(tab_content,"EXEL")
                    q_tab.setCurrentWidget(tab_content)
                else:
                    tab_content = NotSupportFileView()
                    dm = download_manager(file_path)
                    download_buttona = downloadButton(file_path.info.name.name.decode().lower(),lambda: dm.download_file_img())
                    q_tab = self.ui.tabWidget_2
                    tab_content.layout().addWidget(download_buttona, alignment=Qt.AlignCenter)
                    q_tab.addTab(tab_content,"Not Suport Fiel")
                    q_tab.setCurrentWidget(tab_content)

            except Exception as e:
                print(f"Bład w PyTSK3 w display_chebger.py : {e}")
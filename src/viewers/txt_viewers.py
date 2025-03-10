from PySide6.QtWidgets import QTextEdit,QWidget,QTreeView,QAbstractItemView
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget,QVBoxLayout
from src.disc_inage_reader.ewf_info import EWFImgInfo
from src.disc_inage_reader.image_file_model import TSKFileSystemModel
import pytsk3
import pyewf
import os
import traceback

#import olefile
import re
import string
class TxtViewers (QWidget):
    def __init__(self,parent = None):
        super().__init__()
        try:
            filename = os.listdir("D:\\Laptop HP\\dysk_twardy_hgst_w51k obraz")
            for i in range(len(filename)):
                filename[i] = os.path.join("D:\\Laptop HP\\dysk_twardy_hgst_w51k obraz", filename[i])
            ewf_handle = pyewf.handle()
            ewf_handle.open(filename)
            img = EWFImgInfo(ewf_handle)
            volume = pytsk3.Volume_Info(img)
            partitions = list(volume)
            first_partition = partitions[7]
            print(first_partition)
            fs = pytsk3.FS_Info(img, offset=first_partition.start * 512)
            
            self.model = TSKFileSystemModel(fs)
            self.tree = QTreeView()
            
            self.tree.setModel(self.model)
            #self.tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            self.tree.setExpandsOnDoubleClick(True)
            layout = QVBoxLayout()
            layout.addWidget(self.tree)
            self.setLayout(layout)
            
        except Exception as e:
            print(f"ERROR IMAGE VIEW: {e}")
            print(traceback.format_exc())
def display_txt_content(context,txt_path,ext):
    try:
        txt_viewers = TxtViewers()
        layout = context.ui.reportsPage.layout()
        if layout is None:
            raise ValueError("Brak layoutu w reportsPage!")
        meta_data_system_file = MetaDataTableWiget(txt_path)
        view_cleaer(layout,context)
        q_tab = context.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget")
        tab_content = QWidget()
        tab_layout = QVBoxLayout(tab_content)


        layoutRP = context.ui.rightMenu.layout()
        layoutRP.addWidget(meta_data_system_file)

        q_tab.addTab(tab_content,"Text")
        q_tab.setCurrentWidget(txt_viewers)
        

        tab_layout.addWidget(txt_viewers)
    except Exception as e:
        print(f"ERROR IMAGE VIEW: {e}")
        print(traceback.format_exc())
from PySide6.QtWidgets import QWidget,QFileSystemModel,QVBoxLayout,QTreeView,QListView,QSizePolicy,QPushButton
from PySide6.QtCore import QSize
from src.viewers.explorer_function import view_cleaer,MetaDataTableWiget
from src.disc_image_reader.ewf_info import EWFImgInfo
from src.disc_image_reader.image_file_tree_model import TSKFileSystemTreeModel
from src.disc_image_reader.image_file_list_model import TSKFileSystemListModel
import pytsk3
import pyewf
import os
import traceback
import json
class DiscViewersTree(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.parent = parent
        file_config = open(".\\config.json")
        config = json.load(file_config)
        base_path = config['path']
        nr_partycji = config['numer_partycji']
        filename = os.listdir(base_path)
        for i in range(len(filename)):
            filename[i] = os.path.join(base_path, filename[i])
        ewf_handle = pyewf.handle()
        ewf_handle.open(filename)
        img = EWFImgInfo(ewf_handle)
        volume = pytsk3.Volume_Info(self.parent.disc_img)
        partitions = list(volume)
        first_partition = partitions[nr_partycji]
        #print(first_partition)
        self.fs = pytsk3.FS_Info(img, offset=first_partition.start * 512)
        self.model = TSKFileSystemTreeModel(fs = self.parent.fs)


        volume = pytsk3.Volume_Info(img)
        #volume = pytsk3.tsk_vs_open(img)
        partitions = list(volume)
        basic_partitions = []
        for partition in volume:
            # print(f"volume: {partition.addr}, Rozmiar: {partition.len}, Nazwa: {partition.desc}")
            if partition.desc == b"Basic data partition":
                basic_partitions.append(partition)

        # print(basic_partitions)
        

        
        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.model)
        self.tree_view.setAnimated(True)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tree_view.doubleClicked.connect(lambda index: self.itemDoubleClicked(index, parent))
        self.tree_view.clicked.connect(self.itemOneClicked)
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree_view)
        self.setLayout(layout)
       

    def itemOneClicked(self,index):
        item = index.internalPointer()
        print(item)
        if item[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            self.parent.disc_imgae_explorer.model.folder_path = item[0]
            self.parent.disc_imgae_explorer.model.load_entreis()
            self.parent.disc_imgae_explorer.model.layoutChanged.emit()
            self.parent.ui.pathImageLabel.setText(item[0])
            if  self.parent.ui.customQStackedWidget.currentIndex() != 6 :
                self.parent.ui.customQStackedWidget.setCurrentIndex(6)
        else:
            import src.viewers.display_chenger as g
            g.display_file_content(self.parent, item, 1, self.fs)
        # self.parent.img_path = self.model.folder_path
        # self.parent.ui.pathImageLabel.setText(self.parent.img_path)
        
def display_dir_content(context,dir_viewers,dir_path):
    
    prev_btn = QPushButton("<-")
    next_btn = QPushButton("->")

    # dir_viewers.list_view.doubleClicked.connect(lambda index: dir_viewers.itemDoubleClicked(index, context))
    # dir_viewers.list_view.clicked.connect(lambda index: dir_viewers.itemOneClicked(index,context))
    layout = context.ui.reportsPage.layout()
    view_cleaer(layout,context)
    context.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget").addTab(dir_viewers,"last_patch_part")
    # layoutRP = context.ui.rightMenu.layout()
    # layoutRP.addWidget(meta_data_system_file)
    layout.addWidget(prev_btn)
    layout.addWidget(next_btn)
    
   

    
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
class DiscViewersExplorator(QWidget):
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
        self.model = TSKFileSystemListModel(file_system = self.parent.fs)


        volume = pytsk3.Volume_Info(img)
        #volume = pytsk3.tsk_vs_open(img)
        partitions = list(volume)
        basic_partitions = []
        for partition in volume:
            # print(f"volume: {partition.addr}, Rozmiar: {partition.len}, Nazwa: {partition.desc}")
            if partition.desc == b"Basic data partition":
                basic_partitions.append(partition)

        self.list_view = QListView(self)
        self.list_view.setModel(self.model)
        self.list_view.setViewMode(QListView.IconMode) 
        self.list_view.setIconSize(QSize(64, 64)) 
        self.list_view.setResizeMode(QListView.Adjust) 
        self.list_view.setGridSize(QSize(100, 100))
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.list_view.doubleClicked.connect(lambda index: self.itemDoubleClicked(index, parent))
        #self.list_view.clicked.connect(lambda index: self.itemOneClicked(index,parent))
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_view)
        self.setLayout(layout)

    

    # def set_directory(self, dir_path):
    #     self.file_system_model.setRootPath(dir_path)
    #     self.list_view.setRootIndex(self.file_system_model.index(dir_path))

    def prevItem(self, parent):
    # Przejdź do katalogu wyżej
        if "/" in self.model.folder_path.strip("/"):
            self.model.folder_path = self.model.folder_path.rsplit("/", 1)[0]
            if self.model.folder_path == "":
                self.model.folder_path = "/"
        else:
            self.model.folder_path = "/"
        self.model.load_entreis()
        self.model.layoutChanged.emit()
        parent.img_path = self.model.folder_path
        parent.ui.pathImageLabel.setText(parent.img_path)

    def prevItemTree(self,parent):
        parent.img_path = parent.img_path.rsplit("/", 1)[0]
        parent.ui.pathImageLabel.setText(parent.img_path)
        self.tree_view.setRootIndex(self.model.parent(self.tree_view.rootIndex()))

    def itemDoubleClicked(self, index, parent):
        row = index.row()
        if 0 <= row < len(self.model.entries):
            item = self.model.entries[row]
            print(item)
            if item[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
                self.model.folder_path = item[0]
                self.model.load_entreis()
                self.model.layoutChanged.emit()
                parent.img_path = item[0]
                parent.ui.pathImageLabel.setText(parent.img_path)
            else:
                import src.viewers.display_chenger as g
                g.display_file_content(parent, item, 1, self.fs)

    def itemDoubleClickedTree(self,index,parent):
        """Obsługuje kliknięcie elementu – jeśli katalog, przechodzi do niego."""
        item = index.internalPointer()
        print(item)
        if item[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            self.tree_view.setRootIndex(index)
            #print(item[1].info.name.name.decode())
            parent.img_path = f"{parent.img_path}/{item[1].info.name.name.decode()}"
            parent.ui.pathImageLabel.setText(parent.img_path)
            
        else:
            import src.viewers.display_chenger as g
            item = index.internalPointer()
            g.display_file_content(parent,item,1,self.fs)
            
            

    def print_entries(self, index):
        # Wypisuje słownik entries z modelu do konsoli
        for key, val_list in self.model.entries.items():
            #print(f"Ścieżka: {key}")
            for val in val_list:
                try:
                    name = val[1].info.name.name.decode() if val[1].info.name.name else "<brak nazwy>"
                    addr = val[1].info.name.meta_addr
                    # print(f"  - {name} fullpath{val[0]}")
                    #print(f"  - {name} (addr: {addr}) fullpath{val[0]}")
                except Exception as e:
                    print(f"  - Błąd odczytu: {e}")
        import pprint
        pprint.pprint(self.model.entries)

    def itemOneClicked(self,index,parent):
        file_path = self.file_system_model.filePath(index)
        #meta_data_table_wiget = MetaDataTableWiget(file_path)
        # self.setMetadataRightWidget(parent,meta_data_table_wiget)
        
    def init_partition_tree():
        file_config = open(".\\config.json")
        config = json.load(file_config)
        base_path = config['path']
        basic_partitions = []
        for partition in volume:
            print(f"volume: {partition.addr}, Rozmiar: {partition.len}, Nazwa: {partition.desc}")
            if partition.desc == b"Basic data partition":
                basic_partitions.append(partition)
    # def setMetadataRightWidget(self,context,wiget):
    #     layout_rm = context.ui.rightMenu.layout()
    #     if layout_rm is None:
    #         layout_rm = QVBoxLayout(context.ui.rightMenu)
    #         context.ui.rightMenu.setLayout(layout_rm)
    #     for i in reversed(range(layout_rm.count())):
    #         widget_to_remove = layout_rm.itemAt(i).widget()
    #         widget_to_remove.deleteLater() 
    #     layout_rm.addWidget(wiget)
        
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
    
   

    
from PySide6.QtWidgets import QWidget,QFileSystemModel,QVBoxLayout,QListView,QSizePolicy,QPushButton
from PySide6.QtCore import QSize
from src.viewers.explorer_function import view_cleaer,MetaDataTableWiget
class DirViewers(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath("")
        self.list_view = QListView(self)
        self.list_view.setModel(self.file_system_model)
        self.list_view.setViewMode(QListView.IconMode) 
        self.list_view.setIconSize(QSize(64, 64)) 
        self.list_view.setResizeMode(QListView.Adjust) 
        self.list_view.setGridSize(QSize(100, 100))
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.list_view.doubleClicked.connect(lambda index: self.itemDoubleClicked(index, parent))
        self.list_view.clicked.connect(lambda index: self.itemOneClicked(index,parent))
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_view)
        self.setLayout(layout)

    def set_directory(self, dir_path):
        self.file_system_model.setRootPath(dir_path)
        self.list_view.setRootIndex(self.file_system_model.index(dir_path))

    def itemDoubleClicked(self,index,parent):
        """Obsługuje kliknięcie elementu – jeśli katalog, przechodzi do niego."""
        file_path = self.file_system_model.filePath(index)
        if self.file_system_model.isDir(index):  
            self.set_directory(file_path)
            parent.ui.pathLabel.setText(file_path)
        else:
            import src.viewers.display_chenger as g
            meta_data_system_file = MetaDataTableWiget(file_path)
            layout_rm = parent.ui.rightMenu.layout()
            if layout_rm is None:
                layout_rm = QVBoxLayout(parent.ui.rightMenu)
                parent.ui.rightMenu.setLayout(layout_rm)
            for i in reversed(range(layout_rm.count())):
                widget_to_remove = layout_rm.itemAt(i).widget()
                widget_to_remove.deleteLater() 
            layout_rm.addWidget(meta_data_system_file)
            g.display_file_content(parent,file_path)

    def itemOneClicked(self,index,parent):
        file_path = self.file_system_model.filePath(index)
        meta_data_table_wiget = MetaDataTableWiget(file_path)
        self.setMetadataRightWidget(parent,meta_data_table_wiget)
        

    def setMetadataRightWidget(self,context,wiget):
        layout_rm = context.ui.rightMenu.layout()
        if layout_rm is None:
            layout_rm = QVBoxLayout(context.ui.rightMenu)
            context.ui.rightMenu.setLayout(layout_rm)
        for i in reversed(range(layout_rm.count())):
            widget_to_remove = layout_rm.itemAt(i).widget()
            widget_to_remove.deleteLater() 
        layout_rm.addWidget(wiget)
        
def display_dir_content(context,dir_viewers,dir_path):
    dir_viewers.file_system_model.setRootPath(dir_path)
    dir_viewers.set_directory(dir_path)
    meta_data_system_file = MetaDataTableWiget(dir_path)
    
    prev_btn = QPushButton("<-")
    next_btn = QPushButton("->")

    dir_viewers.list_view.doubleClicked.connect(lambda index: dir_viewers.itemDoubleClicked(index, context))
    dir_viewers.list_view.clicked.connect(lambda index: dir_viewers.itemOneClicked(index,context))
    layout = context.ui.reportsPage.layout()
    view_cleaer(layout,context)
    context.ui.reportsPage.findChild(QWidget,"function_bar").findChild(QWidget,"tabWidget").addTab(dir_viewers,"last_patch_part")
    layoutRP = context.ui.rightMenu.layout()
    layoutRP.addWidget(meta_data_system_file)
    layout.addWidget(prev_btn)
    layout.addWidget(next_btn)
    
   

    
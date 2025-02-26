from PySide6.QtWidgets import QWidget,QFileSystemModel,QVBoxLayout,QTableView,QListView,QSizePolicy,QPushButton
from PySide6.QtCore import QSize
from src.viewers.explorer_function import view_cleaer
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
        self.uper_path = ""

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_view)
        self.setLayout(layout)

    def set_directory(self, dir_path):
        self.file_system_model.setRootPath(dir_path)
        self.list_view.setRootIndex(self.file_system_model.index(dir_path))

    def itme_list_clicked(self,index,parent):
        """Obsługuje kliknięcie elementu – jeśli katalog, przechodzi do niego."""
        file_path = self.file_system_model.filePath(index)
        
        if self.file_system_model.isDir(index):  
            self.set_directory(file_path)
            parent.ui.label_11.setText(file_path)
        else:
            import src.viewers.display_chenger as g
            g.display_file_content(self,file_path)
        
def display_dir_content(context,dir_path):
    dir_viewers = DirViewers()
    dir_viewers.file_system_model.setRootPath(dir_path)
    dir_viewers.set_directory(dir_path)
    
    prev_btn = QPushButton("<-")
    next_btn = QPushButton("->")

    dir_viewers.list_view.clicked.connect(lambda index: dir_viewers.itme_list_clicked(index, context))
    
    layout = context.ui.reportsPage.layout()
    view_cleaer(layout,context)
    # if layout is None:
    #     layout = QVBoxLayout(context.ui.reportsPage)
    #     context.ui.reportsPage.setLayout(layout)
    # for i in reversed(range(layout.count())):
    #     widget_to_remove = layout.itemAt(i).widget()
    #     print(widget_to_remove.objectName())
    #     if widget_to_remove:
    #         widget_to_remove.setParent(None)

    #context.verticalLayout_13.addWidget(prev_btn)
    
    layout.addWidget(dir_viewers,stretch=1)
    layout.addWidget(prev_btn)
    layout.addWidget(next_btn)
    
   

    
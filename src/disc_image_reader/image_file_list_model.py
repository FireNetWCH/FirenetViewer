from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt,QAbstractListModel
from PySide6.QtWidgets import QFileIconProvider
import os
import pytsk3
class TSKFileSystemListModel(QAbstractListModel):
    def __init__(self,file_system, parent = None):
        super().__init__(parent)
        #self.entries = entris
        self.root_path = "/"
        self.folder_path = self.root_path
        self.icon_provider = QFileIconProvider()
        self.entries = []
        self.fs = file_system
        self.load_entreis()

    def load_entreis(self):
        print("laduje encje")
        print(self.folder_path)
        self.entries = []
        for entry in self.fs.open_dir(path = self.folder_path):
            name = entry.info.name.name.decode()
            if name not in [".",".."]:
                if self.folder_path != '/':
                    self.entries.append(((self.folder_path+"/"+name),entry))
                else: 
                    self.entries.append(((self.folder_path+name),entry))
        print(self.entries)

    def rowCount(self,parent):
        return len(self.entries)
    
    def data(self,index,role):
        if not index.isValid():
            return None
        
        item = self.entries[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
           
            return item[1].info.name.name.decode() if item[1].info.name.name else "Brak nazwy"

        elif role == Qt.ItemDataRole.DecorationRole:
            
            if not item[1].info.meta or not hasattr(item[1].info.name, 'type') or item[1].info.name.type is None:
                
                return self.icon_provider.icon(QFileIconProvider.IconType.File)
            elif item[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
                return self.icon_provider.icon(QFileIconProvider.IconType.Folder)
            else:
                return self.icon_provider.icon(QFileIconProvider.IconType.File)


import sys
import pyewf
import pytsk3
from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel, QMainWindow,QFileIconProvider, QAbstractItemView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt,QAbstractListModel
import os
class TSKFileSystemTreeModel(QAbstractItemModel):
    def __init__(self, fs, parent=None):
        super().__init__(parent)
        self.fs = fs
        self.root_path = "/"
        self.icon_provider = QFileIconProvider()
        
        self.entries = {}   
        self.build_entries(self.root_path)
    
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 1

    def rowCount(self, parent):
        if not parent.isValid():
            return len(self.entries.get(self.root_path, []))
        node = parent.internalPointer()
        parent_key = node[0]
        if node[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            if parent_key not in self.entries:
                self.build_entries(parent_key)

            if len(self.entries[parent_key]) == 0:
                return 1 
            else:
                
                return len(self.entries[parent_key])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        
        item = index.internalPointer()
       
        if role == Qt.ItemDataRole.DisplayRole:
           
            return item[1].info.name.name.decode() if item[1].info.name.name else "Brak nazwy"

        elif role == Qt.ItemDataRole.DecorationRole:
            
            if not item[1].info.meta or not hasattr(item[1].info.name, 'type') or item[1].info.name.type is None:
                
                return self.icon_provider.icon(QFileIconProvider.IconType.File)
            elif item[1].info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
                return self.icon_provider.icon(QFileIconProvider.IconType.Folder)
            else:
                return self.icon_provider.icon(QFileIconProvider.IconType.File)

        else:
            return None

    def index(self, row, column, parent):
        if not parent.isValid():
            key = self.root_path
        else:
            parent_entry = parent.internalPointer()
            key = parent_entry[0]
        
        if key in self.entries and row < len(self.entries[key]):
            file_entry = self.entries[key][row]
            return self.createIndex(row, 0, file_entry)
        else:
            return QModelIndex()


    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        
        entry = index.internalPointer()
       
        entry_key = os.path.dirname(entry[0])   
        parent_dir = os.path.dirname(entry_key)

        
        if parent_dir not in self.entries:
            self.build_entries(parent_dir)
        if parent_dir not in self.entries:
            self.build_entries(parent_dir)
        w = self.entries[parent_dir]
        for row ,item in enumerate(w):
            if item[0] == entry_key:
                return self.createIndex(row,0,item) 
        return QModelIndex()
        

    def hasChildren(self, parent=QModelIndex()):
        has_children = self.rowCount(parent) > 0
        return has_children 

    def fetchMore(self, parent):
        return 0 
        
    def build_entries(self, parent_path):
        key = parent_path
        if key not in self.entries:
            self.entries[key] = []
        for item in self.fs.open_dir(path=key):
            name = item.info.name.name.decode()
            if name not in [".", ".."]:
                full_path = key + "/" + name if key != "/" else "/" + name
                self.entries[key].append((full_path, item))

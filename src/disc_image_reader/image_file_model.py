import sys
import pyewf
import pytsk3
from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel, QMainWindow,QFileIconProvider, QAbstractItemView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt,QAbstractListModel
class TSKFileSystemModel(QAbstractItemModel):
    def __init__(self, fs, parent=None):
        super().__init__(parent)
        self.fs = fs
        self.root_path = "/"
        self.icon_provider = QFileIconProvider()
        self.entries = {self.root_path : list(fs.open_dir(path="/"))}   
        for item in self.entries[self.root_path]: 
            if (item.info.name.name.decode() == "."):
                self.entries[self.root_path].remove(item)
            if (item.info.name.name.decode() == ".."):
                self.entries[self.root_path].remove(item) 
        
    
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 1

    def rowCount(self, parent):
        if not parent.isValid():
            return len(self.entries.get(self.root_path, []))
        node = parent.internalPointer()


        parent_key = self._generate_key(self.get_key(node.info.name.meta_addr), parent.internalPointer().info.name.name.decode() if parent.isValid() else self.root_path)
        if node.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            if parent_key not in self.entries:
                self.entries[parent_key] = list(self.fs.open_dir(path=parent_key))
                
                self.entries[parent_key] = [
                    item for item in self.entries[parent_key]
                    if item.info.name.name.decode() not in [".", ".."]
                    ] 

            if len(self.entries[parent_key]) == 0:
                return 1 
            else:
                return len(self.entries[parent_key])
        return 0

    def data(self, index, role):
            if not index.isValid():
                return None

            if role == Qt.ItemDataRole.DisplayRole:
                item = index.internalPointer()
                return item.info.name.name.decode()
            elif role ==Qt.ItemDataRole.DecorationRole: 
                item = index.internalPointer()
                if item.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
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
            key = self._generate_key(self.get_key(parent_entry.info.name.meta_addr), parent_entry.info.name.name.decode())

        if key in self.entries and row < len(self.entries[key]):
            file_entry = self.entries[key][row]
            return self.createIndex(row, column, file_entry)
        else:
            return QModelIndex()


    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        
        entry = index.internalPointer()
        entry_key = self.get_key(entry.info.name.meta_addr)

        if(entry_key == '/'):
            return QModelIndex()

        key_list=entry_key.split("/")
        if len(key_list) == 1:
            entry_key = "/"
            value = key_list[0]
        else: 
            value = key_list[-1]
            key_list = key_list[:-1]
            entry_key = "/".join(key_list)        
        w = self.entries[entry_key]
        for row ,item in enumerate(w):
            if item.info.name.name.decode() == value:
                return self.createIndex(row,0,item) 

        

    def hasChildren(self, parent=QModelIndex()):
        has_children = self.rowCount(parent) > 0
        return has_children 

    def fetchMore(self, parent):
        return 0 

    def _generate_key(self,  parent_key,entry,):
        if parent_key == "/":
            return entry
        else:
            return parent_key + "/" + entry        
        

    def get_key(self, value):                    
        for key, val_list in self.entries.items():
            for val in val_list:
                if val.info.name.meta_addr == value:
                    return key
                        
        return None
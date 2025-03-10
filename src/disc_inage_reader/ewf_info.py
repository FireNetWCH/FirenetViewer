import sys
import os
import pytsk3
import pyewf
from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel, QMainWindow, QAbstractItemView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt

class EWFImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self.ewf_handle = ewf_handle
        super().__init__()

    def read(self, offset, size):
        self.ewf_handle.seek(offset)
        return self.ewf_handle.read(size)

    def get_size(self):
        return self.ewf_handle.get_media_size()



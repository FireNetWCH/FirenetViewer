import pyewf
import pytsk3
import os
from PySide6.QtWidgets import QFileDialog

class download_manager():
    def __init__(self,file):
        self.file = file

    def select_output_path(self):
        dir_path = QFileDialog.getExistingDirectory(None, "Wybierz folder do zapisu PDF")
        return dir_path
    
    def download_file_img(self):
        
        output_path = os.path.join(self.select_output_path(),self.file.info.name.name.decode().lower())
        print(output_path)
        with open(output_path, "wb") as output_file:
            offset = 0
            size = 1024 * 1024  #
            while offset < self.file.info.meta.size:
                available_to_read = min(size, self.file.info.meta.size - offset)
                data = self.file.read_random(offset, available_to_read)
                if not data:
                    break
                output_file.write(data)
                offset += len(data)
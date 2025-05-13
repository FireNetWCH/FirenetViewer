from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout,QPushButton,QFileDialog,QMessageBox
from PySide6.QtCore import Qt
import io
class NotSupportFileView(QWidget):
    def __init__(self,byte_stream,name,ext,parent=None):
        super().__init__(parent)

        self.label = QLabel("Ten format pliku nie jest obsługiwany.")
        self.label.setAlignment(Qt.AlignCenter) 
        self.btn = QPushButton("Pobierz")
        self.btn.clicked.connect(lambda : self.copy_file(parent,byte_stream,name,ext))
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.setContentsMargins(20, 20, 20, 20) 
        self.setLayout(layout)

    def copy_file(self,parent,byte_stream,name,ext):
       
        suggested_file_name = f"{name}"
        file_path, _ = QFileDialog.getSaveFileName( parent, "Zapisz plik jako...", suggested_file_name, f"Pliki {ext} (*{ext})")
        if not file_path:
            return  

        try:            
            if isinstance(byte_stream, io.BytesIO):
                data = byte_stream.getvalue()
            else:
                data = byte_stream

            with open(file_path, 'wb') as f:
                f.write(data)

            QMessageBox.information(parent, "Sukces", f"Plik zapisany pomyślnie:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(parent, "Błąd", f"Nie udało się zapisać pliku:\n{str(e)}")
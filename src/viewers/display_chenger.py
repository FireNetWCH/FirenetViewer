from src.viewers.pdf_viewer import display_pdf_content
from src.viewers.img_viewer import display_img_content
from src.viewers.video_viewer import display_vidoe_content
from src.viewers.dir_viewers import display_dir_content
import os

def display_file_content(self, file_path: str,history_flag = 1) -> None:
        """W zależności od rozszerzenia, wyświetla zawartość pliku lub komunikat o braku wsparcia.
          Jeśli flaga ustawiona jest na 0 nie dodaje przekazanej ścieżki do wyszukiwania"""
        #history_flag -> oznacza czy sciężka ma zostać dodana do histori szukania, czy ścieżka pochodzi z akcji cofnięcia w przód/tył

        try:
            print(file_path)
            _, ext = os.path.splitext(file_path.lower())
            if ext in ['.txt', '.csv', '.py', '.log']:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if isinstance(content, list):
                        content = "\n".join(content)
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.history.append_history(file_path)
            elif ext == '.pdf':
                display_pdf_content(self,0,1, file_path)
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.histor.append_history(file_path)
            elif ext in ['.jpg','.jpeg','.png','.gif','.bmp','.ppm']:
                display_img_content(self,file_path)
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.histor.append_history(file_path)
            elif ext == '.pst':
                self.display_image_message("PST files are in progress.")
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.histor.append_history(file_path)
            elif ext in ['.mp4','.avi','.mkv','.mov','.wmv','.flv','.ogv']:
                display_vidoe_content(self,file_path)
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.histor.append_history(file_path)
            elif os.path.isdir(file_path):
                display_dir_content(self,file_path)
                self.ui.label_11.setText(file_path)
                if history_flag == 1:
                    self.histor.append_history(file_path)
            else:
                self.ui.label_11.setText("Selected file type is not supported.")
        except Exception as e:
            self.ui.label_11.setText(f"Could not read file: {e}")
            
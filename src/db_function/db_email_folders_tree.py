import sqlite3
from PySide6.QtWidgets import QTreeWidgetItem,QTreeWidget
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def load_folders_data_into_tree(self,db_connection,folders_tree):
        if not db_connection:
            return
        try:
            cursor = db_connection.cursor()
            cursor.execute("SELECT path, id,item_count FROM folders")
            rows = cursor.fetchall()
            tree_dict = {}
            for row in rows:
                full_path = row[0]
                dir_id = row[1]
                item_count = row[2]
                parts = full_path.split("\\")
                current_level = tree_dict

                for part in parts:
                    if part not in current_level:
                        current_level[part] = {"id": dir_id,"item_count": item_count, "subfolders": {}}
                    current_level = current_level[part]["subfolders"]
            folders_tree.clear()
            add_items_to_tree(self,folders_tree,tree_dict)
            
        except sqlite3.Error as e:
            print(f"Błąd zapytania do bazy: {e}")

def add_items_to_tree(self, parent, tree_level: dict):
        for folder_name, folder_data in tree_level.items():
            if folder_name =="":
                folder_name = "HOME"
            item = QTreeWidgetItem([f"{folder_name} ({folder_data['item_count']})"])
            item.setData(0, 1, folder_data["id"])
            if isinstance(parent, QTreeWidget):
                parent.addTopLevelItem(item)
            else:
                parent.addChild(item)
            if folder_data["subfolders"]:
                add_items_to_tree(self,item, folder_data["subfolders"])
# def display_database(self,path_to_dir,sql_name,db_connection,folders_tree):
#         from src.functions import load_data_from_database
#         self.list_widget = QListWidget()
#         self.list_widget.setObjectName("db_list")
#         self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         sql_list_file = []
#         dir_content =  os.scandir(path_to_dir)
#         for file in dir_content:
#             if os.path.isdir(os.path.join(path_to_dir,file)):
#                 list_file = os.scandir(os.path.join(path_to_dir,file))
#                 for sq_file in list_file:
#                     if os.path.isfile(os.path.join(path_to_dir,file,sq_file)) :
#                         _, ext = os.path.splitext(sq_file.name.lower())
#                         if ext == '.sqlite':
#                             sql_list_file.append(sq_file.name)


#         if self.db_connection is None and len(sql_list_file) > 0 :
#             try:
#                 db_email.connect_to_database(self,path_to_dir+"\\"+sql_list_file[0].split('.')[-2]+"\\"+sql_list_file[0])
#                 load_data_from_database(self,db_connection,folders_tree)
#                 sql_name =sql_list_file[0].split('.')[-2]
#                 self.ui.dataAnalysisPage.findChild(QLabel,"sqlEmailDbName").setText(sql_name)
#                 logger.info(f"Połączono z pierwszą odnalezioną bazą SQLite: {sql_name}")
#             except Exception as e:
#                 logger.error(f"Bład przy pierwszym łaczeniu do SQLite: {e}")
#         #print(sql_list_file)
#         self.list_widget.addItems(sql_list_file)    
#         layout = self.ui.helpPage.layout()
#         layout.addWidget(self.list_widget)
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
import src.db_function.db_email_function as db_email
from src.label_page.main_label_page import load_all_labels,load_clicked_email_on_labels
from src.email_page.label_dialog import LabelsCrud
import logging
from src.email_page.main_emeil_table import load_data_from_database
from src.email_page.multi_tag_selector import MultiTagSelectorMultiEmail
from src.email_page.main_emeil_table import load_data_from_database
from src.message_box.date_warning import add_labels_worning
from PySide6.QtCore import QCoreApplication
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ContextMenu:
    def __init__(self, main, db_connection):
        self.main = main
        self.db_connection = db_connection

    def show(self, pos, context_widget):
        raise NotImplementedError("Metoda 'show' musi być zaimplementowana w klasie pochodnej")

class LabelContextMenu(ContextMenu):
    def __init__(self, main, db_connection,parent,path):
        super().__init__(main, db_connection)
        self.parent= parent
        self.path = path

    def add_lebels_to_db(self,id_labels_name,selected_text,parent):
        db_email.add_label(parent.db_connection,id_labels_name,parent.id_selected_email,selected_text)
        add_labels_worning()

    def show(self, pos, context_widget):
        all_labels = db_email.get_all_labels_name(self.db_connection)
        labelContextMenu = QMenu(self.main)
        submenu = QMenu(QCoreApplication.translate("context_meny","Nadaj Etykiete"), labelContextMenu)

        selected_text = context_widget.selectedText()
        #print(selected_text)

        for row in all_labels:
            action = QAction(str(row[1]), self.main)
            action.triggered.connect(lambda checked, value=row[0]: self.add_lebels_to_db(value, selected_text,self.parent))
            submenu.addAction(action)
        
        add_new_label_action = QAction(QCoreApplication.translate("context_meny","+ Dodaj nową"), self.main)
        add_new_label_action.triggered.connect(lambda : self.super_add_label(context_widget))
        labelContextMenu.addMenu(submenu)
        submenu.addAction(add_new_label_action)
        labelContextMenu.exec(context_widget.mapToGlobal(pos))

    def show_label_crud(self):
        dialog = LabelsCrud(self.db_connection,self.path)
        if dialog.exec():
            logger.info(f"Zaktualizowano tagi dla użytkownika")
            load_data_from_database(self.parent)

    def super_add_label(self,context_widget):
        self.show_label_crud()
        selected_text = context_widget.selectedText()
        if selected_text != "":
            all_labels = db_email.get_all_labels_name(self.db_connection)
            #print(all_labels)
            self.add_lebels_to_db(all_labels[-1][0], selected_text,self.parent)
            

class EditLabelContextMenu(LabelContextMenu):
    def __init__(self, main, db_connection,parent,path):
        super().__init__(main, db_connection,parent,path)
        self.parent = parent
        self.path = path
    def add_lebels_to_db(self,id_labels_name,selected_text,parent):
        super().add_lebels_to_db(id_labels_name,selected_text,parent)
        load_all_labels(parent)

    def show_label_crud(self,parent):
        super().show_label_crud()
        load_all_labels(parent)

    def edit_label(self,current_text,parent):
        db_email.updata_label(self.db_connection,parent.id_selected_label,current_text)
        load_all_labels(parent)
        load_clicked_email_on_labels(parent,parent.last_clicket_row)

    def show(self, pos, context_widget):
        all_labels = db_email.get_all_labels_name(self.db_connection)
        labelContextMenu = QMenu(self.main)

        submenu = QMenu(QCoreApplication.translate("context_meny","Dodaj etykiete"), labelContextMenu)

        selected_text = context_widget.selectedText()

        for row in all_labels:
            action = QAction(str(row[1]), self.main)
            action.triggered.connect(lambda checked, value=row[0]: self.add_lebels_to_db(value, selected_text,self.parent))
            submenu.addAction(action)

        add_new_label_action = QAction(QCoreApplication.translate("context_meny","+ Dodaj nową"), self.main)
        add_new_label_action.triggered.connect(lambda: self.show_label_crud(self.parent))
        labelContextMenu.addMenu(submenu)
        submenu.addAction(add_new_label_action)
        labelContextMenu.addMenu(submenu)
        

        action_edit = QAction(QCoreApplication.translate("context_meny","Edytuj etykietę"), self.main)
        action_edit.triggered.connect(lambda: self.edit_label(selected_text,self.parent))
        labelContextMenu.addAction(action_edit)

        labelContextMenu.exec(context_widget.mapToGlobal(pos)) 


class TableContextMenu(ContextMenu):
    def __init__(self, main, db_connection, parent):
        super().__init__(main, db_connection)
        self.parent = parent
        self.main = main
        self.table = parent
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(lambda pos: self.show(pos, context_widget=parent))

    def show(self, pos, context_widget):
        labelContextMenu = QMenu(self.parent)
        set_multi_tag_action = labelContextMenu.addAction(QCoreApplication.translate("context_meny","Nadaj kategorie"))
        set_multi_tag_action.triggered.connect(lambda : self.set_multi_tag(self.main.db_connection,context_widget))
        labelContextMenu.exec(context_widget.mapToGlobal(pos))


    def set_multi_tag(self, db_connection, context_widget):
        dialog = MultiTagSelectorMultiEmail(None, connection=db_connection, parent=context_widget)
        query = 'INSERT or IGNORE INTO email_tags (email_id, tag_id) VALUES (?, ?);'
        dialog.load_tags()
        cursor = db_connection.cursor()
        if dialog.exec():
            selected_rows = {item.row() for item in context_widget.selectedItems()}
            for row in selected_rows:  
                id_email = context_widget.item(row,0) 
                for i in range(len(dialog.tags)):
                        cursor.execute(query, (id_email.text(),dialog.tags[i]))
            
        db_connection.commit()
        load_data_from_database(self.main)

    # def set_multi_tag(self, db_connection, context_widget):
    #     dialog = MultiTagSelectorMultiEmail(None, connection=db_connection, parent=context_widget)
    #     query = 'INSERT INTO email_tags (email_id, tag_id) VALUES (?, ?);'
    #     dialog.load_tags()
    #     cursor = db_connection.cursor()
    #     if dialog.exec():
    #         selected_rows = {item.row() for item in context_widget.selectedItems()}
    #         print(dialog.tags)
    #         for row in selected_rows:  
    #             tag_widget = context_widget.cellWidget(row, 6)  
    #             id_email = context_widget.item(row, 0) 

    #             tag_names = []
    #             if tag_widget:  
    #                 layout = tag_widget.layout()  
    #                 for i in range(layout.count()):
    #                     label = layout.itemAt(i).widget()
    #                     if isinstance(label, ClickableLabel):  
    #                         tag_names.append(label.text())
    #                         cursor.execute(query, (id_email.text(),dialog.tags.get(label.text())))
    #             print(f"Wiersz {row}: tagi={tag_names}, id = {id_email.text() if id_email else 'brak'}")
    #     db_connection.commit()



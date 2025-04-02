from PySide6.QtWidgets import QMenu, QLabel
from PySide6.QtGui import QAction
import src.db_function.db_email_function as db_email
from src.label_page.main_label_page import load_all_labels,load_clicked_email_on_labels
class ContextMenu:
    def __init__(self, main, db_connection):
        self.main = main
        self.db_connection = db_connection

    def show(self, pos, context_widget):
        raise NotImplementedError("Metoda 'show' musi być zaimplementowana w klasie pochodnej")

class LabelContextMenu(ContextMenu):
    def __init__(self, main, db_connection,parent):
        super().__init__(main, db_connection)
        self.parent= parent

    def add_lebels_to_db(self,id_labels_name,selected_text,parent):
        db_email.add_label(parent.db_connection,id_labels_name,parent.id_selected_email,selected_text)

    def show(self, pos, context_widget):
        all_labels = db_email.get_all_labels_name(self.db_connection)
        labelContextMenu = QMenu(self.main)
        submenu = QMenu("Dodaj Etykiete", labelContextMenu)

        selected_text = context_widget.selectedText()
        #print(selected_text)

        for row in all_labels:
            action = QAction(str(row[1]), self.main)
            action.triggered.connect(lambda checked, value=row[0]: self.add_lebels_to_db(value, selected_text,self.parent))
            submenu.addAction(action)

        labelContextMenu.addMenu(submenu)
        labelContextMenu.exec(context_widget.mapToGlobal(pos))

class EditLabelContextMenu(LabelContextMenu):
    def __init__(self, main, db_connection,parent):
        super().__init__(main, db_connection,parent)
        self.parent = parent

    def add_lebels_to_db(self,id_labels_name,selected_text,parent):
        super().add_lebels_to_db(id_labels_name,selected_text,parent)
        print(parent)
        print("dziecko")
        load_all_labels(parent)

    def edit_label(self,current_text,parent):
        db_email.updata_label(self.db_connection,parent.id_selected_label,current_text)
        load_all_labels(parent)
        load_clicked_email_on_labels(parent,parent.last_clicket_row)

    def show(self, pos, context_widget):
        all_labels = db_email.get_all_labels_name(self.db_connection)
        labelContextMenu = QMenu(self.main)

        submenu_labels = QMenu("Dodaj etykiete", labelContextMenu)

        selected_text = context_widget.selectedText()

        for row in all_labels:
            action = QAction(str(row[1]), self.main)
            action.triggered.connect(lambda checked, value=row[0]: self.add_lebels_to_db(value, selected_text,self.parent))
            submenu_labels.addAction(action)


        labelContextMenu.addMenu(submenu_labels)
        

        action_edit = QAction("Edytuj etykietę", self.main)
        action_edit.triggered.connect(lambda: self.edit_label(selected_text,self.parent))
        labelContextMenu.addAction(action_edit)

        labelContextMenu.exec(context_widget.mapToGlobal(pos)) 
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QTabWidget,QVBoxLayout,QPushButton,QWidget
import pandas as pd

#from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget


class TableViewer(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self

def display_table_content(df):
    table_viewer = TableViewer()    
    heder = df.columns.tolist() 
    
    
    df.fillna("",inplace=True)
    table_viewer.setColumnCount(len(heder))
    table_viewer.setHorizontalHeaderLabels(heder)
    table_viewer.setRowCount(len(df))
    #meta_data_system_file = MetaDataTableWiget(path_file)
    
    for row in range(len(df)):
        for col ,c_n in enumerate(df.columns):
            table_viewer.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))
    table_viewer.show()
    #layout = context.ui.reportsPage.layout()
    #view_cleaer(layout,context)
    #layoutRP = context.ui.rightMenu.layout()
    #layoutRP.addWidget(meta_data_system_file)

    tab_content = QWidget()
    tab_layout = QVBoxLayout(tab_content)
    tab_layout.addWidget(table_viewer)
    return tab_content
    
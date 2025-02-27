from PySide6.QtWidgets import QTableWidget,QTableWidgetItem
import pandas as pd
from src.viewers.explorer_function import view_cleaer


class TableViewer(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self

def display_table_content(context,path_file,ext):
    table_viewer = TableViewer()
    if ext == ".csv":
        df = pd.read_csv(path_file)
    elif ext in['.xlsx','.xlsm','.xlsb',]:
        df = pd.read_excel(path_file)
    elif ext in ['.odf','.ods','.odt']:
        df = pd.read_excel(path_file,engine="odf")
    elif ext in ['.xls']:
        df = pd.read_excel(path_file,engine="xlrd")    
    heder = df.columns.tolist() 
    
    
    df.fillna("",inplace=True)
    print(df)
    table_viewer.setColumnCount(len(heder))
    table_viewer.setHorizontalHeaderLabels(heder)
    table_viewer.setRowCount(len(df))

    
    for row in range(len(df)):
        for col ,c_n in enumerate(df.columns):
            table_viewer.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))
    table_viewer.show()
    layout = context.ui.reportsPage.layout()
    view_cleaer(layout,context)
    layout.addWidget(table_viewer)
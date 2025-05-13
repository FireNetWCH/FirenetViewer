from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QVBoxLayout,QWidget

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
    
    for row in range(len(df)):
        for col ,c_n in enumerate(df.columns):
            table_viewer.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))
    table_viewer.show()
    tab_content = QWidget()
    tab_layout = QVBoxLayout(tab_content)
    tab_layout.addWidget(table_viewer)
    return tab_content
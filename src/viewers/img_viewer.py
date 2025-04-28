from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QScrollArea,QPushButton,QGraphicsPixmapItem,QTableWidget,QTableWidgetItem,QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap,QPainter
from src.viewers.explorer_function import view_cleaer,get_image_metadata,MetaDataTableWiget


class IMGViewer(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setScene(scene) 
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.metaDataWiget = QTableWidget()
        self.metaDataWiget.setColumnCount(2)
        self.metaDataWiget.setHorizontalHeaderLabels(['Nazwa','Wartość'])
        

    def add_image_to_scene(self, pixmap):
        """Dodaje obraz do sceny"""
        self.scene().clear()  
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene().addItem(pixmap_item) 
        self.setSceneRect(pixmap_item.pixmap().rect())  

    def zoom_image(self):
        self.scale(1.25,1.25)
    
    def rezoom_image(self):
        self.scale(0.75,0.75)
        
def display_img_content(context, pixmap) -> None:
    """Wyświetla obraz w aplikacji"""
    try:
        scene = QGraphicsScene()
        img_viewer = IMGViewer(scene)
        # meta_data_dictonery = get_system_metadata(file_path)
        # meta_data_system_file = MetaDataTableWiget(file_path)
        # meta_data = get_image_metadata(file_path)

        # img_viewer.metaDataWiget.setRowCount(len(meta_data))
        
        # for row, (tag, value) in enumerate(meta_data.items()):
        #         img_viewer.metaDataWiget.setItem(row, 0, QTableWidgetItem(str(tag)))
        #         img_viewer.metaDataWiget.setItem(row, 1, QTableWidgetItem(str(value)))

        
        
        img_viewer.add_image_to_scene(pixmap)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(img_viewer)

        zoom_btn = QPushButton("ZOOM +")
        rezoom_btn = QPushButton("ZOOM -")
        left_rotate_image_btn = QPushButton("<-")
        rigth_rotate_image_btn = QPushButton("->")

        zoom_btn.clicked.connect(img_viewer.zoom_image)
        rezoom_btn.clicked.connect(img_viewer.rezoom_image)
        left_rotate_image_btn.clicked.connect(lambda: img_viewer.rotate(90))
        rigth_rotate_image_btn.clicked.connect(lambda: img_viewer.rotate(-90))

        layout = context.ui.reportsPage.layout()
        layoutRP = context.ui.rightMenu.layout()
        view_cleaer(layout,context)
        

        tab_content = QWidget()
        tab_layout = QVBoxLayout(tab_content)


        tab_layout.addWidget(scroll_area)
        tab_layout.addWidget(left_rotate_image_btn)
        tab_layout.addWidget(rigth_rotate_image_btn)
        tab_layout.addWidget(zoom_btn)
        tab_layout.addWidget(rezoom_btn)
        
        return tab_content
        

        # layoutRP.addWidget(img_viewer.metaDataWiget)
        # layoutRP.addWidget(meta_data_system_file)
    except Exception as e:
        print(f"Error displaying image: {e}")
        context.ui.pathLabel.setText(f"Nie można wyświetlić obrazu: {e}")


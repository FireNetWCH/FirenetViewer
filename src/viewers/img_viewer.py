from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QScrollArea,QWidget,QPushButton,QVBoxLayout,QGraphicsPixmapItem,QTableWidget,QTableWidgetItem
from PySide6.QtGui import QPixmap,QPainter
from PySide6.QtCore import Qt
from src.viewers.explorer_function import view_cleaer,get_image_metadata


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
        
def display_img_content(context, file_path: str) -> None:
    """Wyświetla obraz w aplikacji"""
    try:
        scene = QGraphicsScene()
        img_viewer = IMGViewer(scene) 
        meta_data = get_image_metadata(file_path)
        print(meta_data)
        img_viewer.metaDataWiget.setRowCount(len(meta_data))
        
        for row, (tag, value) in enumerate(meta_data.items()):
                img_viewer.metaDataWiget.setItem(row, 0, QTableWidgetItem(str(tag)))
                img_viewer.metaDataWiget.setItem(row, 1, QTableWidgetItem(str(value)))

        if file_path:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
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
        print(layoutRP)
        view_cleaer(layout,context)

        layout.addWidget(scroll_area)
        layout.addWidget(left_rotate_image_btn)
        layout.addWidget(rigth_rotate_image_btn)
        layout.addWidget(zoom_btn)
        layout.addWidget(rezoom_btn)
        layoutRP.addWidget(img_viewer.metaDataWiget)
    except Exception as e:
        print(f"Error displaying image: {e}")
        context.ui.label_11.setText(f"Nie można wyświetlić obrazu: {e}")


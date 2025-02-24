from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QScrollArea,QWidget,QPushButton,QVBoxLayout,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap,QPainter
from PySide6.QtCore import Qt


class IMGViewer(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setScene(scene) 
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def add_image_to_scene(self, pixmap):
        """Dodaje obraz do sceny"""
        self.scene().clear()  
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene().addItem(pixmap_item) 
        #self.setSceneRect(pixmap_item.pixmap().rect())  

    def zoom_image(self):
        self.scale(1.25,1.25)
    
    def rezoom_image(self):
        self.scale(0.75,0.75)
        
def display_img_content(context, file_path: str) -> None:
    """Wyświetla obraz w aplikacji"""
    try:
        scene = QGraphicsScene()
        img_viewer = IMGViewer(scene) 

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
        if layout is None:
            layout = QVBoxLayout(context.ui.reportsPage)
            context.ui.reportsPage.setLayout(layout)

        
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        layout.addWidget(scroll_area)
        layout.addWidget(left_rotate_image_btn)
        layout.addWidget(rigth_rotate_image_btn)
        layout.addWidget(zoom_btn)
        layout.addWidget(rezoom_btn)

    except Exception as e:
        print(f"Error displaying image: {e}")
        context.ui.label_11.setText(f"Nie można wyświetlić obrazu: {e}")


from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QHBoxLayout,QScrollArea,QPushButton,QGraphicsPixmapItem,QTableWidget,QWidget,QVBoxLayout
from PySide6.QtGui import QPainter,QIcon
from PySide6.QtCore import Qt
import logging
#from src.viewers.explorer_function import view_cleaer,get_image_metadata,MetaDataTableWiget


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
        self.original_pixmap = None

    def add_image_to_scene(self, pixmap, scaled=False, width=None, height=None):
        """Dodaje obraz do sceny"""
        self.scene().clear()
        if self.original_pixmap is None:
            self.original_pixmap = pixmap  # zapisujemy tylko raz oryginał

        if scaled and width and height:
            pixmap = self.original_pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.current_scale_factor = width / self.original_pixmap.width()
        else:
            self.current_scale_factor = 1.0

        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene().addItem(self.pixmap_item)
        self.setSceneRect(self.pixmap_item.boundingRect())
 

    def zoom_image(self):
        self.current_scale_factor *= 1.25
        self.rescale_from_original()
    
    def rezoom_image(self):
        self.current_scale_factor *= 0.75
        self.rescale_from_original()
    
    def rescale_from_original(self):
        if self.original_pixmap:
            width = self.original_pixmap.width() * self.current_scale_factor
            height = self.original_pixmap.height() * self.current_scale_factor
            scaled_pixmap = self.original_pixmap.scaled(
                int(width), int(height), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )

            # Zamiast dodawać do sceny od nowa – zmieniamy pixmapę istniejącego itemu
            self.pixmap_item.setPixmap(scaled_pixmap)
            self.setSceneRect(self.pixmap_item.boundingRect())
        
def display_img_content(pixmap,parent_widget = None):
    """Zwraca tab Wiget"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    try:
        scene = QGraphicsScene()
        img_viewer = IMGViewer(scene)
        
        if parent_widget is not None:
            available_width = parent_widget.width()
            available_height = parent_widget.height()
            img_viewer.add_image_to_scene(pixmap, scaled=True, width=available_width, height=available_height)

        else:
            img_viewer.add_image_to_scene(pixmap)
            

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(img_viewer)

        zoom_btn = QPushButton()
        zoom_btn.setIcon((QIcon(":feather\\icons\\feather\\zoom-in.png")))
        rezoom_btn = QPushButton()
        rezoom_btn.setIcon((QIcon(":feather\\icons\\feather\\zoom-out.png")))
        left_rotate_image_btn = QPushButton()
        left_rotate_image_btn.setIcon((QIcon(":feather\\icons\\feather\\corner-down-right.png")))
        rigth_rotate_image_btn = QPushButton()
        rigth_rotate_image_btn.setIcon((QIcon(":feather\\icons\\feather\\corner-down-left.png")))
        zoom_btn.clicked.connect(img_viewer.zoom_image)
        rezoom_btn.clicked.connect(img_viewer.rezoom_image)
        left_rotate_image_btn.clicked.connect(lambda: img_viewer.rotate(90))
        rigth_rotate_image_btn.clicked.connect(lambda: img_viewer.rotate(-90))

        tab_content = QWidget()
        tab_layout = QVBoxLayout(tab_content)

        buton_layaut = QHBoxLayout()
        buton_layaut.addWidget(left_rotate_image_btn)
        buton_layaut.addWidget(rigth_rotate_image_btn)
        buton_layaut.addWidget(zoom_btn)
        buton_layaut.addWidget(rezoom_btn)

        tab_layout.addWidget(scroll_area)
        tab_layout.addLayout(buton_layaut)

        return tab_content
        
    except Exception as e:
        print(f"Error displaying image: {e}")
        logger.error(f"Error tabImgieView: {e}")
       
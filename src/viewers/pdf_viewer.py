from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QScrollArea, QWidget,QPushButton,QHBoxLayout,QLabel
from PySide6.QtGui import QPixmap, QImage, QPainter, QWheelEvent,QIcon
from PySide6.QtCore import Qt
import fitz
import logging

class PDFViewer(QGraphicsView):
    def __init__(self,pdf_document,page_label: QLabel,all_page_count_label: QLabel,parent=None,parent_wiget = None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.curent_page_number_label = page_label
        self.all_page_count_label = all_page_count_label
        self.scale_factor = 1.25
        self.page_number = 0
        self.pdf_document = pdf_document
        self.zoom_in_factor = 1.15
        self.parent_wiget = parent_wiget
        self.zoom_factor = 1.0
        self.render_page()

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.angleDelta().y() > 0:
            self.change_page(1)
        else:
            self.change_page(-1)

    def change_page(self, delta: int):
        """Update page number and render the new page."""
        new_page_number = self.page_number + delta
        if 0 <= new_page_number < len(self.pdf_document):
            self.page_number = new_page_number
            self.render_page()

    def render_page(self):
        """Renders the current page onto the scene."""
        self.scene.clear()
        page = self.pdf_document[self.page_number]

        base_dpi = 150  # bazowa jakość
        default_pix = page.get_pixmap(dpi=base_dpi)
        
        # Jeśli pierwszy raz i mamy parent_wiget, dopasuj zoom_factor
        if self.zoom_factor == 1.0 and self.parent_wiget is not None:
            available_width = self.parent_wiget.width()
            available_height = self.parent_wiget.height()

            # Oszacuj zoom na podstawie rozmiaru okna i strony PDF
            zoom_x = available_width / default_pix.width
            zoom_y = available_height / default_pix.height
            self.zoom_factor = min(zoom_x, zoom_y)  # zachowujemy proporcje

        dpi = int(base_dpi * self.zoom_factor)
        pix = page.get_pixmap(dpi=dpi)

        img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)

        if pixmap.isNull():
            print(f"Page {self.page_number} failed to convert to QPixmap")

        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmap_item)

        self.setSceneRect(pixmap_item.boundingRect())
        self.resetTransform()
        self.curent_page_number_label.setText(str(self.page_number + 1))
        self.all_page_count_label.setText(f"/ {len(self.pdf_document)}")
        self.update()
    
    def plus_size_view_pdf_chenger(self):
        """Zwiększa rozmiar wyświetlanego PDF-a"""
        self.zoom_factor *= self.zoom_in_factor
        self.render_page()

    def minus_size_view_pdf_chenger(self):
        """Zmniejsza rozmiar wyświetlanego PDF-a"""
        self.zoom_factor /= self.zoom_in_factor
        self.render_page()
        

def display_pdf_content(pdf_document,parent_wiget = None):
    """Wyświetla zawartość pliku PDF i niezbędne przyciski w widoku aplikacji."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    try:    
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        prev_btn = QPushButton()
        prev_btn.setIcon((QIcon(":feather\\icons\\feather\\arrow_left.png")))
        curent_page_number_label = QLabel()
        all_page_count_label = QLabel()
        next_btn = QPushButton()
        next_btn.setIcon((QIcon(":feather\\icons\\feather\\arrow_right.png")))    

        zoom_btn = QPushButton()
        zoom_btn.setIcon((QIcon(":feather\\icons\\feather\\zoom-in.png")))
        rezoom_btn = QPushButton()
        rezoom_btn.setIcon((QIcon(":feather\\icons\\feather\\zoom-out.png")))
        pdf_view = PDFViewer(pdf_document,curent_page_number_label,all_page_count_label,parent_wiget=parent_wiget)
       
        prev_btn.pressed.connect(lambda: pdf_view.change_page(-1))
        next_btn.pressed.connect(lambda: pdf_view.change_page(1))
        zoom_btn.pressed.connect(lambda: pdf_view.plus_size_view_pdf_chenger())
        rezoom_btn.pressed.connect(lambda: pdf_view.minus_size_view_pdf_chenger())

        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        layout_horizontal = QHBoxLayout()
        
        layout_horizontal.addWidget(prev_btn)
        layout_horizontal.addWidget(curent_page_number_label)
        layout_horizontal.addWidget(all_page_count_label)
        layout_horizontal.addWidget(next_btn)
        layout_horizontal.addWidget(zoom_btn)
        layout_horizontal.addWidget(rezoom_btn)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(pdf_view)
        
        layout.addWidget(scroll_area)
        layout.addLayout(layout_horizontal)
        

        
        container_widget.setLayout(layout)
        logger.info("zwrucona TabWiget dla PDF")
        return container_widget

        
    except Exception as e:
        print(f"Error displaying PDF: {e}")
        logger.error(f" Error displaying PDF: {e}")
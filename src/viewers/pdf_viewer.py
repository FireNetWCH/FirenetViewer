from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QScrollArea, QWidget,QPushButton
from PySide6.QtGui import QPixmap, QImage, QPainter, QWheelEvent
from PySide6.QtCore import Qt
import fitz

class PDFViewer(QGraphicsView):
    def __init__(self,scene,zoom = 1.25, parent=None, pdf_document=None, current_page=0):
        super().__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scale_factor = zoom
        self.page_number = current_page
        self.pdf_document = pdf_document
        self.zoom_in_factor = 1.15
        

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
        page = self.pdf_document[self.page_number]
        pix = page.get_pixmap(dpi=150)
        img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)
        if pixmap.isNull():
            print(f"Page {self.page_number} failed to convert to QPixmap")
               
        scene = self.scene()
        scene.clear()  
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.setSceneRect(scene.itemsBoundingRect())
        self.resetTransform()
        self.scale(self.scale_factor, self.scale_factor)
        self.update()
    
    def plus_size_view_pdf_chenger(self):
        """Zwiększa rozmiar wyświetlanego PDF-a"""
        self.scale(self.zoom_in_factor, self.zoom_in_factor)
        self.scale_factor *= self.zoom_in_factor
        
    def minus_size_view_pdf_chenger(self):
        """Zmniejsza rozmiar wyświetlanego PDF-a"""
        self.zoom_out_factor = 1 / self.zoom_in_factor
        self.scale(self.zoom_out_factor, self.zoom_out_factor)
        self.scale_factor *= self.zoom_out_factor
        

def display_pdf_content(context, num_page,zoom,file_path: str) -> None:
    """Wyświetla zawartość pliku PDF i niezbędne przyciski w widoku aplikacji."""
    try:
        pdf_document = fitz.open(file_path)
        scene = QGraphicsScene()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        container_widget = QWidget()
        prev_btn = QPushButton("Poprzednia strona")
        next_btn = QPushButton("Następna strona")
        zoom_btn = QPushButton("ZOOM +")
        rezoom_btn = QPushButton("ZOOM -")


        layout = QVBoxLayout(container_widget)

        pdf_view = PDFViewer(scene,zoom, pdf_document=pdf_document, current_page=num_page)
        pdf_view.setScene(scene)
        pdf_view.setSceneRect(scene.itemsBoundingRect())
        pdf_view.render_page()

        prev_btn.pressed.connect(lambda: pdf_view.change_page(-1))
        next_btn.pressed.connect(lambda: pdf_view.change_page(1))
        zoom_btn.pressed.connect(lambda: pdf_view.plus_size_view_pdf_chenger())
        rezoom_btn.pressed.connect(lambda: pdf_view.minus_size_view_pdf_chenger())


        scroll_area.setWidget(pdf_view)
        layout = context.ui.reportsPage.layout()
        if layout is None:
            layout = QVBoxLayout(context.ui.reportsPage)
            context.ui.reportsPage.setLayout(layout)
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        layout.addWidget(scroll_area)
        layout.addWidget(prev_btn)
        layout.addWidget(next_btn)
        layout.addWidget(zoom_btn)
        layout.addWidget(rezoom_btn)
    except Exception as e:
        print(f"Error displaying PDF: {e}")
        context.ui.label_11.setText(f"Nie można wyświetlić PDF: {e}")



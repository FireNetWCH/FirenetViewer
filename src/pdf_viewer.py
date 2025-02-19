from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QScrollArea, QWidget
from PySide6.QtGui import QPixmap, QImage, QPainter, QWheelEvent
from PySide6.QtCore import Qt
import fitz

class PDFViewer(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scale_factor = 1.0

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
            self.scale_factor *= zoom_in_factor
        else:
            self.scale(zoom_out_factor, zoom_out_factor)
            self.scale_factor *= zoom_out_factor

def display_pdf_content(context, file_path: str) -> None:
    """Wyświetla zawartość pliku PDF w widoku aplikacji."""
    try:
        pdf_document = fitz.open(file_path)
        scene = QGraphicsScene()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        y_offset = 0
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            pix = page.get_pixmap(dpi=150)
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            if pixmap.isNull():
                print(f"Page {page_number} failed to convert to QPixmap")
            pixmap_item = QGraphicsPixmapItem(pixmap)
            pixmap_item.setPos(0, y_offset)
            scene.addItem(pixmap_item)
            y_offset += pixmap.height() + 10
        pdf_document.close()
        pdf_view = PDFViewer(scene)
        pdf_view.setScene(scene)
        pdf_view.setSceneRect(scene.itemsBoundingRect())
        pdf_view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
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
    except Exception as e:
        print(f"Error displaying PDF: {e}")
        context.ui.label_11.setText(f"Nie można wyświetlić PDF: {e}")

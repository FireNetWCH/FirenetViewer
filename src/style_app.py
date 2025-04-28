from PySide6.QtCore import Qt,QFile
from PySide6.QtGui import QPixmap,QIcon,QImage
from PySide6.QtWidgets import QSizeGrip,QLabel
import sys,os
from src.firenet_viewer_widget.scalableLabel import scalableLabel
def get_resource_path(relative_path):
    """Zwraca poprawną ścieżkę do zasobów, obsługując tryb onefile"""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS  
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class style_app():
    def __init__(self, parent):
        self.parent = parent



    def set_style(self): 
        self.parent.resize_grip_frame = self.parent.ui.sizeGrip
        self.parent.resize_grip = QSizeGrip(self.parent.resize_grip_frame)
        self.parent.resize_grip.resize(200, 200)
        self.parent.resize_grip.move(self.parent.main.width() - 20, self.parent.main.height() - 20)

        image = QImage(get_resource_path("logo.png"))
        # Ustawienie obrazu w ScalableLabel

        old_label = self.parent.ui.homePage.findChild(QLabel, "label_7")
        new_label = scalableLabel(parent=old_label.parent())
        new_label.setObjectName("label_7")
        new_label.setGeometry(old_label.geometry())

        layout = old_label.parentWidget().layout()
        if layout:
            index = layout.indexOf(old_label)
            layout.removeWidget(old_label)
            old_label.deleteLater()
            layout.insertWidget(index, new_label)
        else:
            old_label.deleteLater()
            new_label.show()
        new_label.setPixmap(QPixmap.fromImage(image))
          

        pixmap = QPixmap(get_resource_path("miniLogo.png"))
        scaled_pixmap = pixmap.scaled(40, 40, Qt.KeepAspectRatio)
        self.parent.ui.label_23.setPixmap(scaled_pixmap)
        self.parent.ui.ofertaBtn.setIcon(QIcon(scaled_pixmap))
       

        #ustawienie odpowiednich ikon i kolorów tła

        
        self.parent.ui.export_pdf.setIcon(QIcon(":feather/icons/feather/pdf.png"))
        
        self.parent.ui.exportExelBtn.setIcon(QIcon(":feather/icons/feather/xls.png"))
        
        self.parent.ui.clearBtn.setIcon(QIcon(":material_design/icons/material_design/hide_source.png"))
        self.parent.ui.show_table_btn.setIcon(QIcon(":feather/icons/feather/rotate-cw.png"))
        self.parent.ui.leftMenu.setStyleSheet("background-color: #102339; border: 3px solid #102339;")

        self.parent.ui.homeBtn.setIcon(QIcon(":feather/FFFFFF/feather/home.png"))
        self.parent.ui.infoBtn.setIcon(QIcon(":feather/FFFFFF/feather/activity.png"))
        self.parent.ui.dataBtn.setIcon(QIcon(":feather/FFFFFF/feather/mail.png"))
        self.parent.ui.restoreBtn.setIcon(QIcon(":feather/FFFFFF/feather/copy.png"))

        # file = QFile(":feather/FFFFFF/feather/copy.png")

        # if file.exists():
        #     print("Zasób został poprawnie załadowany!")
        # else:
        #     print("Zasób NIE został znaleziony.")
        self.parent.ui.closeBtn.setIcon(QIcon(":feather/FFFFFF/feather/x.png"))
        self.parent.ui.linkedinBtn.setIcon(QIcon(":feather/FFFFFF/feather/linkedin.png"))
        self.parent.ui.fbBtn.setIcon(QIcon(":feather/FFFFFF/feather/facebook.png"))

        self.parent.ui.graphsBtn.setIcon(QIcon(":font_awesome/FFFFFF/font_awesome/solid/chart-pie.png"))
        self.parent.ui.meilBoxBtn.setIcon(QIcon(":material_design/FFFFFF/material_design/format_align_justify.png"))
        
        self.parent.ui.closeCenterMenuBtn.setIcon(QIcon(":font_awesome/icons/font_awesome/solid/circle-xmark.png"))
        self.parent.ui.startDataBtn.setIcon(QIcon(":font_awesome/icons/font_awesome/regular/calendar.png"))

        self.parent.ui.minimalizeBtn.setIcon(QIcon(":feather/FFFFFF/feather/minus.png"))
        self.parent.ui.prevEmailTableBtn.setIcon(QIcon(":feather/icons/feather/arrow_left.png"))
        self.parent.ui.nextEmailTableBtn.setIcon(QIcon(":feather/icons/feather/arrow_right.png"))
       
        self.parent.ui.fbBtn.setIcon(QIcon(":feather/FFFFFF/feather/facebook.png"))
        self.parent.ui.wwwBtn.setIcon(QIcon(":feather/FFFFFF/font_awesome/solid/rss.png"))
        self.parent.ui.eksploratorImgBtn.setIcon(QIcon(":feather/FFFFFF/font_awesome/solid/rss.png"))
        self.parent.ui.exploratorImageBtn.setIcon(QIcon(":feather/FFFFFF/font_awesome/solid/rss.png"))

        #UKRYWANIE ZBĘDNYCH PRZYCISKÓW
        #
        self.parent.ui.frame_2.hide()
        self.parent.ui.searchBtn.hide()
        self.parent.ui.searchinp.hide()
        self.parent.ui.label_9.hide()
        self.parent.ui.serachinpCont.hide()
        self.parent.ui.emailHederDockWidget.hide()
        #przyciski

        self.parent.ui.graphsBtn.hide()
        self.parent.ui.dataBtn.hide()
        # self.parent.ui.infoBtn.hide()
        self.parent.ui.reportsBtn.hide()
        self.parent.ui.meilBoxBtn.hide()
        self.parent.ui.settingsBtn.hide()

        self.parent.ui.detailsBtn.hide()
        self.parent.ui.menuBtn.hide()
        self.parent.ui.helpBtn.hide()

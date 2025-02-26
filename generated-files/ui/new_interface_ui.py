# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTreeView,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1264, 634)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1264, 471))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(74, 44))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(140, 146))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.homeBtn = QPushButton(self.widget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.widget_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportsBtn = QPushButton(self.widget_2)
        self.reportsBtn.setObjectName(u"reportsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/report_problem.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportsBtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.reportsBtn)

        self.graphsBtn = QPushButton(self.widget_2)
        self.graphsBtn.setObjectName(u"graphsBtn")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome/solid/icons/font_awesome/solid/chart-pie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphsBtn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.graphsBtn)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(130, 112))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.fileBtn = QPushButton(self.widget_3)
        self.fileBtn.setObjectName(u"fileBtn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileBtn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.fileBtn)

        self.settingsBtn = QPushButton(self.widget_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.widget_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.widget_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignmentFlag.AlignLeft)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setMaximumSize(QSize(200, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/font_awesome/solid/icons/font_awesome/solid/circle-xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.Settings = QFrame(self.widget_5)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.Settings.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Settings)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.Settings)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.Settings)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.Settings)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_19 = QVBoxLayout(self.informationPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pst_files_btn = QPushButton(self.informationPage)
        self.pst_files_btn.setObjectName(u"pst_files_btn")
        icon10 = QIcon()
        icon10.addFile(u":/material_design/icons/material_design/attach_email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pst_files_btn.setIcon(icon10)

        self.verticalLayout_19.addWidget(self.pst_files_btn)

        self.select_directory = QPushButton(self.informationPage)
        self.select_directory.setObjectName(u"select_directory")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_directory.setIcon(icon11)

        self.verticalLayout_19.addWidget(self.select_directory)

        self.centerMenuPages.addWidget(self.informationPage)
        self.fileReader = QWidget()
        self.fileReader.setObjectName(u"fileReader")
        self.fileReader.setMaximumSize(QSize(199, 389))
        self.treeView = QTreeView(self.fileReader)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(0, 0, 161, 341))
        self.centerMenuPages.addWidget(self.fileReader)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_8 = QVBoxLayout(self.helpPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.helpPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.mainBody)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_8 = QHBoxLayout(self.header)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 5)
        self.titleTxt = QLabel(self.header)
        self.titleTxt.setObjectName(u"titleTxt")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.titleTxt.setFont(font1)

        self.horizontalLayout_8.addWidget(self.titleTxt, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.notificationBtn = QPushButton(self.frame_2)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon12 = QIcon()
        icon12.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.notificationBtn)

        self.moreBtn = QPushButton(self.frame_2)
        self.moreBtn.setObjectName(u"moreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn.setIcon(icon13)

        self.horizontalLayout_7.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_2)
        self.profileBtn.setObjectName(u"profileBtn")
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.profileBtn)


        self.horizontalLayout_8.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.serachinpCont = QFrame(self.header)
        self.serachinpCont.setObjectName(u"serachinpCont")
        self.serachinpCont.setMinimumSize(QSize(338, 36))
        self.serachinpCont.setMaximumSize(QSize(338, 16777215))
        self.serachinpCont.setFrameShape(QFrame.Shape.StyledPanel)
        self.serachinpCont.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.serachinpCont)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.serachinpCont)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(16, 16))
        self.label_9.setMaximumSize(QSize(16, 16))
        self.label_9.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.searchinp = QLineEdit(self.serachinpCont)
        self.searchinp.setObjectName(u"searchinp")
        self.searchinp.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.searchinp)

        self.searchBtn = QPushButton(self.serachinpCont)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_9.addWidget(self.searchBtn)


        self.horizontalLayout_8.addWidget(self.serachinpCont, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.minimalizeBtn = QPushButton(self.frame_3)
        self.minimalizeBtn.setObjectName(u"minimalizeBtn")
        icon15 = QIcon()
        icon15.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimalizeBtn.setIcon(icon15)

        self.horizontalLayout_10.addWidget(self.minimalizeBtn)

        self.restoreBtn = QPushButton(self.frame_3)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon16 = QIcon()
        icon16.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon16)

        self.horizontalLayout_10.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_3)
        self.closeBtn.setObjectName(u"closeBtn")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon17)

        self.horizontalLayout_10.addWidget(self.closeBtn)


        self.horizontalLayout_8.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.verticalLayout_10 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.mainPages = QCustomQStackedWidget(self.mainPagesCont)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_11 = QVBoxLayout(self.homePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.homePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)

        self.mainPages.addWidget(self.homePage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_12 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_8 = QWidget(self.dataAnalysisPage)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_12.addWidget(self.widget_8)

        self.label_10 = QLabel(self.dataAnalysisPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_10)

        self.widget_7 = QWidget(self.dataAnalysisPage)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.seachName = QLineEdit(self.widget_7)
        self.seachName.setObjectName(u"seachName")

        self.horizontalLayout_13.addWidget(self.seachName)

        self.seachSurname = QLineEdit(self.widget_7)
        self.seachSurname.setObjectName(u"seachSurname")

        self.horizontalLayout_13.addWidget(self.seachSurname)

        self.searchDate = QLineEdit(self.widget_7)
        self.searchDate.setObjectName(u"searchDate")

        self.horizontalLayout_13.addWidget(self.searchDate)

        self.serachOld = QLineEdit(self.widget_7)
        self.serachOld.setObjectName(u"serachOld")

        self.horizontalLayout_13.addWidget(self.serachOld)

        self.filter_table_btn = QPushButton(self.widget_7)
        self.filter_table_btn.setObjectName(u"filter_table_btn")
        icon18 = QIcon()
        icon18.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filter_table_btn.setIcon(icon18)

        self.horizontalLayout_13.addWidget(self.filter_table_btn)

        self.show_flags_btn = QPushButton(self.widget_7)
        self.show_flags_btn.setObjectName(u"show_flags_btn")
        icon19 = QIcon()
        icon19.addFile(u":/feather/icons/feather/flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_flags_btn.setIcon(icon19)

        self.horizontalLayout_13.addWidget(self.show_flags_btn)

        self.show_table_btn = QPushButton(self.widget_7)
        self.show_table_btn.setObjectName(u"show_table_btn")
        icon20 = QIcon()
        icon20.addFile(u":/material_design/icons/material_design/hide_source.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_table_btn.setIcon(icon20)

        self.horizontalLayout_13.addWidget(self.show_table_btn)

        self.export_pdf = QPushButton(self.widget_7)
        self.export_pdf.setObjectName(u"export_pdf")
        icon21 = QIcon()
        icon21.addFile(u":/font_awesome/regular/icons/font_awesome/regular/file-pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_pdf.setIcon(icon21)

        self.horizontalLayout_13.addWidget(self.export_pdf)

        self.export_excel = QPushButton(self.widget_7)
        self.export_excel.setObjectName(u"export_excel")
        icon22 = QIcon()
        icon22.addFile(u":/font_awesome/regular/icons/font_awesome/regular/file-excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_excel.setIcon(icon22)

        self.horizontalLayout_13.addWidget(self.export_excel)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.tableWidget = QTableWidget(self.dataAnalysisPage)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_12.addWidget(self.tableWidget)

        self.mainPages.addWidget(self.dataAnalysisPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_13 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.function_bar = QFrame(self.reportsPage)
        self.function_bar.setObjectName(u"function_bar")
        self.function_bar.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.horizontalLayout_4 = QHBoxLayout(self.function_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.left_btn = QPushButton(self.function_bar)
        self.left_btn.setObjectName(u"left_btn")

        self.horizontalLayout_4.addWidget(self.left_btn)

        self.rigth_btn = QPushButton(self.function_bar)
        self.rigth_btn.setObjectName(u"rigth_btn")

        self.horizontalLayout_4.addWidget(self.rigth_btn)

        self.up_btn = QPushButton(self.function_bar)
        self.up_btn.setObjectName(u"up_btn")

        self.horizontalLayout_4.addWidget(self.up_btn)

        self.label_11 = QLabel(self.function_bar)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)


        self.verticalLayout_13.addWidget(self.function_bar)

        self.graphicsView_2 = QGraphicsView(self.reportsPage)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_13.addWidget(self.graphicsView_2)

        self.mainPages.addWidget(self.reportsPage)
        self.chartPage = QWidget()
        self.chartPage.setObjectName(u"chartPage")
        self.verticalLayout_14 = QVBoxLayout(self.chartPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.graphicsView = QGraphicsView(self.chartPage)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_14.addWidget(self.graphicsView)

        self.label_12 = QLabel(self.chartPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_12)

        self.mainPages.addWidget(self.chartPage)

        self.verticalLayout_10.addWidget(self.mainPages)


        self.horizontalLayout_11.addWidget(self.mainPagesCont)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_15 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.widget_6 = QWidget(self.rightMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.closeRightMenuBtn = QPushButton(self.widget_6)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon23 = QIcon()
        icon23.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeRightMenuBtn.setIcon(icon23)

        self.horizontalLayout_12.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_15.addWidget(self.widget_6)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.verticalLayout_16 = QVBoxLayout(self.notificationsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.notificationsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_14)

        self.rightMenuPages.addWidget(self.notificationsPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_17 = QVBoxLayout(self.morePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.morePage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_15)

        self.rightMenuPages.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_18 = QVBoxLayout(self.profilePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.profilePage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.rightMenuPages.addWidget(self.profilePage)

        self.verticalLayout_15.addWidget(self.rightMenuPages)


        self.horizontalLayout_11.addWidget(self.rightMenu)


        self.verticalLayout_9.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame = QFrame(self.footer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.activityProgress = QProgressBar(self.frame)
        self.activityProgress.setObjectName(u"activityProgress")
        self.activityProgress.setMaximumSize(QSize(16777215, 10))
        self.activityProgress.setValue(24)
        self.activityProgress.setTextVisible(False)

        self.horizontalLayout_6.addWidget(self.activityProgress)


        self.horizontalLayout_5.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.sizeGrip)


        self.verticalLayout_9.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menuBtn.setDefault(False)
        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Data analysis", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.graphsBtn.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"File reader", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center menu", None))
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.pst_files_btn.setText(QCoreApplication.translate("MainWindow", u"Dodaj plik .pst", None))
        self.select_directory.setText(QCoreApplication.translate("MainWindow", u"Dodaj katalog", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"FirenetViewer", None))
        self.notificationBtn.setText("")
        self.moreBtn.setText("")
        self.profileBtn.setText("")
        self.label_9.setText("")
        self.searchinp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        self.minimalizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Analiza danych", None))
        self.seachName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wyszukaj po imieniu", None))
        self.seachSurname.setText("")
        self.seachSurname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wyszukaj po nazwisku", None))
        self.searchDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wyszukaj po dacie urodzenia", None))
        self.serachOld.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wyszukaj po wieku", None))
#if QT_CONFIG(tooltip)
        self.filter_table_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyszukaj w tabeli</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.filter_table_btn.setText("")
#if QT_CONFIG(tooltip)
        self.show_flags_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c wszystkie zaznaczone flagi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_flags_btn.setText("")
#if QT_CONFIG(tooltip)
        self.show_table_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c ca\u0142\u0105 tabel\u0119</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_table_btn.setText("")
#if QT_CONFIG(tooltip)
        self.export_pdf.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do PDF'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_pdf.setText("")
#if QT_CONFIG(tooltip)
        self.export_excel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do excel'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_excel.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Imie", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data urodzenia", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Wiek", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Flagi", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tagi", None));
        self.left_btn.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.rigth_btn.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.up_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Analiza danych", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ChartsPage", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"morePage", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright sth", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme progress", None))
    # retranslateUi


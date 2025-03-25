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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDockWidget,
    QFrame, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QTableWidget, QTableWidgetItem,
    QTreeView, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQPushButton import QCustomQPushButton
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1438, 516)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1264, 471))
        self.verticalLayout_25 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.frame_13)
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


        self.verticalLayout.addWidget(self.widget)

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


        self.verticalLayout.addWidget(self.widget_2)

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


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_24.addWidget(self.leftMenu)

        self.splitter = QSplitter(self.frame_13)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(1)
        self.widget_8 = QWidget(self.splitter)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.centerMenu = QCustomSlideMenu(self.widget_8)
        self.centerMenu.setObjectName(u"centerMenu")
        sizePolicy.setHeightForWidth(self.centerMenu.sizePolicy().hasHeightForWidth())
        self.centerMenu.setSizePolicy(sizePolicy)
        self.centerMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 6)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.centerMenuPages.sizePolicy().hasHeightForWidth())
        self.centerMenuPages.setSizePolicy(sizePolicy2)
        self.centerMenuPages.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        sizePolicy.setHeightForWidth(self.settingsPage.sizePolicy().hasHeightForWidth())
        self.settingsPage.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, 0, 0)
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
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.label_3 = QLabel(self.Settings)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.Settings)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.Settings)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        sizePolicy.setHeightForWidth(self.informationPage.sizePolicy().hasHeightForWidth())
        self.informationPage.setSizePolicy(sizePolicy)
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

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout_23.addWidget(self.centerMenu)

        self.splitter.addWidget(self.widget_8)
        self.mainBody = QWidget(self.splitter)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
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


        self.verticalLayout_9.addWidget(self.header)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy3)
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
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 0, -1, 0)
        self.serchEmailFrame = QFrame(self.dataAnalysisPage)
        self.serchEmailFrame.setObjectName(u"serchEmailFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.serchEmailFrame.sizePolicy().hasHeightForWidth())
        self.serchEmailFrame.setSizePolicy(sizePolicy4)
        self.serchEmailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.serchEmailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.serchEmailFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, 0)
        self.frame_11 = QFrame(self.serchEmailFrame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_22.setContentsMargins(0, 0, -1, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 2, -1, 2)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_10)


        self.verticalLayout_22.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy5)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.seachSurname = QLineEdit(self.frame_10)
        self.seachSurname.setObjectName(u"seachSurname")

        self.horizontalLayout_14.addWidget(self.seachSurname)

        self.seachName = QLineEdit(self.frame_10)
        self.seachName.setObjectName(u"seachName")

        self.horizontalLayout_14.addWidget(self.seachName)

        self.searchBody = QLineEdit(self.frame_10)
        self.searchBody.setObjectName(u"searchBody")

        self.horizontalLayout_14.addWidget(self.searchBody)

        self.searchDate = QLineEdit(self.frame_10)
        self.searchDate.setObjectName(u"searchDate")

        self.horizontalLayout_14.addWidget(self.searchDate)

        self.startDataBtn = QPushButton(self.frame_10)
        self.startDataBtn.setObjectName(u"startDataBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.startDataBtn.sizePolicy().hasHeightForWidth())
        self.startDataBtn.setSizePolicy(sizePolicy6)
        self.startDataBtn.setAutoFillBackground(False)
        self.startDataBtn.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.startDataBtn.setAutoRepeatInterval(100)
        self.startDataBtn.setAutoDefault(False)

        self.horizontalLayout_14.addWidget(self.startDataBtn)

        self.startDataLabel = QLineEdit(self.frame_10)
        self.startDataLabel.setObjectName(u"startDataLabel")
        self.startDataLabel.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.startDataLabel)

        self.endDataBtn = QPushButton(self.frame_10)
        self.endDataBtn.setObjectName(u"endDataBtn")
        sizePolicy6.setHeightForWidth(self.endDataBtn.sizePolicy().hasHeightForWidth())
        self.endDataBtn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.endDataBtn)

        self.endDataLabel = QLineEdit(self.frame_10)
        self.endDataLabel.setObjectName(u"endDataLabel")
        self.endDataLabel.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.endDataLabel)

        self.show_flags_btn = QCustomQPushButton(self.frame_10)
        self.show_flags_btn.setObjectName(u"show_flags_btn")
        icon18 = QIcon()
        icon18.addFile(u":/feather/icons/feather/flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_flags_btn.setIcon(icon18)
        self.show_flags_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.show_flags_btn)

        self.filter_table_btn = QPushButton(self.frame_10)
        self.filter_table_btn.setObjectName(u"filter_table_btn")
        icon19 = QIcon()
        icon19.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filter_table_btn.setIcon(icon19)

        self.horizontalLayout_14.addWidget(self.filter_table_btn)

        self.show_table_btn = QPushButton(self.frame_10)
        self.show_table_btn.setObjectName(u"show_table_btn")
        icon20 = QIcon()
        icon20.addFile(u":/material_design/icons/material_design/hide_source.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_table_btn.setIcon(icon20)

        self.horizontalLayout_14.addWidget(self.show_table_btn)

        self.tagPuschBtn = QPushButton(self.frame_10)
        self.tagPuschBtn.setObjectName(u"tagPuschBtn")

        self.horizontalLayout_14.addWidget(self.tagPuschBtn)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 1)
        self.horizontalLayout_14.setStretch(3, 1)
        self.horizontalLayout_14.setStretch(4, 1)
        self.horizontalLayout_14.setStretch(5, 1)
        self.horizontalLayout_14.setStretch(6, 1)
        self.horizontalLayout_14.setStretch(7, 1)

        self.verticalLayout_22.addWidget(self.frame_10)


        self.horizontalLayout_18.addWidget(self.frame_11)

        self.widget_7 = QWidget(self.serchEmailFrame)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy4.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy4)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)
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

        self.detailsBtn = QPushButton(self.widget_7)
        self.detailsBtn.setObjectName(u"detailsBtn")

        self.horizontalLayout_13.addWidget(self.detailsBtn)


        self.horizontalLayout_18.addWidget(self.widget_7)


        self.verticalLayout_12.addWidget(self.serchEmailFrame)

        self.frame_9 = QFrame(self.dataAnalysisPage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 0, 2, 2)
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy7)

        self.horizontalLayout_16.addWidget(self.label_22)

        self.sqlEmailDbName = QLabel(self.frame_9)
        self.sqlEmailDbName.setObjectName(u"sqlEmailDbName")
        sizePolicy6.setHeightForWidth(self.sqlEmailDbName.sizePolicy().hasHeightForWidth())
        self.sqlEmailDbName.setSizePolicy(sizePolicy6)

        self.horizontalLayout_16.addWidget(self.sqlEmailDbName)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.widget_9 = QWidget(self.dataAnalysisPage)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy6.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy6)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.prevEmailTableBtn = QPushButton(self.widget_9)
        self.prevEmailTableBtn.setObjectName(u"prevEmailTableBtn")
        sizePolicy6.setHeightForWidth(self.prevEmailTableBtn.sizePolicy().hasHeightForWidth())
        self.prevEmailTableBtn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.prevEmailTableBtn)

        self.nextEmailTableBtn = QPushButton(self.widget_9)
        self.nextEmailTableBtn.setObjectName(u"nextEmailTableBtn")
        sizePolicy6.setHeightForWidth(self.nextEmailTableBtn.sizePolicy().hasHeightForWidth())
        self.nextEmailTableBtn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.nextEmailTableBtn)

        self.label_20 = QLabel(self.widget_9)
        self.label_20.setObjectName(u"label_20")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy8)

        self.horizontalLayout_4.addWidget(self.label_20)

        self.pageNumberLabel = QLabel(self.widget_9)
        self.pageNumberLabel.setObjectName(u"pageNumberLabel")
        sizePolicy8.setHeightForWidth(self.pageNumberLabel.sizePolicy().hasHeightForWidth())
        self.pageNumberLabel.setSizePolicy(sizePolicy8)

        self.horizontalLayout_4.addWidget(self.pageNumberLabel)

        self.showSearchPanelBtn = QPushButton(self.widget_9)
        self.showSearchPanelBtn.setObjectName(u"showSearchPanelBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.showSearchPanelBtn.sizePolicy().hasHeightForWidth())
        self.showSearchPanelBtn.setSizePolicy(sizePolicy9)
        self.showSearchPanelBtn.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.showSearchPanelBtn.setFont(font2)
        self.showSearchPanelBtn.setAutoDefault(False)
        self.showSearchPanelBtn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.showSearchPanelBtn)

        self.selectedTagLabel = QLabel(self.widget_9)
        self.selectedTagLabel.setObjectName(u"selectedTagLabel")
        self.selectedTagLabel.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_4.addWidget(self.selectedTagLabel)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget = QTableWidget(self.dataAnalysisPage)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(8)
        self.tableWidget.setFont(font3)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_15.addWidget(self.tableWidget)

        self.EmailtabWidget = QTabWidget(self.dataAnalysisPage)
        self.EmailtabWidget.setObjectName(u"EmailtabWidget")
        sizePolicy2.setHeightForWidth(self.EmailtabWidget.sizePolicy().hasHeightForWidth())
        self.EmailtabWidget.setSizePolicy(sizePolicy2)
        self.EmailtabWidget.setTabsClosable(True)
        self.EmailtabWidgetPage1 = QWidget()
        self.EmailtabWidgetPage1.setObjectName(u"EmailtabWidgetPage1")
        sizePolicy3.setHeightForWidth(self.EmailtabWidgetPage1.sizePolicy().hasHeightForWidth())
        self.EmailtabWidgetPage1.setSizePolicy(sizePolicy3)
        self.horizontalLayout_17 = QHBoxLayout(self.EmailtabWidgetPage1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.scrollArea = QScrollArea(self.EmailtabWidgetPage1)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.Shape.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 520, 338))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.emailLayouts = QVBoxLayout()
        self.emailLayouts.setObjectName(u"emailLayouts")
        self.listAttachments = QListWidget(self.scrollAreaWidgetContents)
        self.listAttachments.setObjectName(u"listAttachments")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.listAttachments.sizePolicy().hasHeightForWidth())
        self.listAttachments.setSizePolicy(sizePolicy10)
        self.listAttachments.setMinimumSize(QSize(500, 150))
        self.listAttachments.setFrameShape(QFrame.Shape.Box)
        self.listAttachments.setFrameShadow(QFrame.Shadow.Sunken)
        self.listAttachments.setLineWidth(1)
        self.listAttachments.setMidLineWidth(1)
        self.listAttachments.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listAttachments.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.listAttachments.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.listAttachments.setAutoScrollMargin(5)
        self.listAttachments.setFlow(QListView.Flow.LeftToRight)
        self.listAttachments.setModelColumn(0)
        self.listAttachments.setUniformItemSizes(False)
        self.listAttachments.setBatchSize(100)

        self.emailLayouts.addWidget(self.listAttachments)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy11)
        self.frame_8.setMinimumSize(QSize(500, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.hederEmailBtn = QPushButton(self.frame_8)
        self.hederEmailBtn.setObjectName(u"hederEmailBtn")
        sizePolicy11.setHeightForWidth(self.hederEmailBtn.sizePolicy().hasHeightForWidth())
        self.hederEmailBtn.setSizePolicy(sizePolicy11)
        self.hederEmailBtn.setMinimumSize(QSize(125, 0))

        self.verticalLayout_21.addWidget(self.hederEmailBtn)

        self.widget_10 = QWidget(self.frame_8)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy6.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy6)
        self.horizontalLayout_26 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setIndent(3)

        self.horizontalLayout_26.addWidget(self.label_4)

        self.sender = QLabel(self.widget_10)
        self.sender.setObjectName(u"sender")
        sizePolicy6.setHeightForWidth(self.sender.sizePolicy().hasHeightForWidth())
        self.sender.setSizePolicy(sizePolicy6)
        self.sender.setFrameShape(QFrame.Shape.Panel)
        self.sender.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_26.addWidget(self.sender)


        self.verticalLayout_21.addWidget(self.widget_10)

        self.widget_51 = QWidget(self.frame_8)
        self.widget_51.setObjectName(u"widget_51")
        sizePolicy6.setHeightForWidth(self.widget_51.sizePolicy().hasHeightForWidth())
        self.widget_51.setSizePolicy(sizePolicy6)
        self.widget_51.setMinimumSize(QSize(0, 0))
        self.widget_51.setBaseSize(QSize(0, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.label_17 = QLabel(self.widget_51)
        self.label_17.setObjectName(u"label_17")
        sizePolicy6.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy6)

        self.horizontalLayout_19.addWidget(self.label_17)

        self.cc = QLabel(self.widget_51)
        self.cc.setObjectName(u"cc")
        sizePolicy6.setHeightForWidth(self.cc.sizePolicy().hasHeightForWidth())
        self.cc.setSizePolicy(sizePolicy6)
        self.cc.setFrameShape(QFrame.Shape.Box)
        self.cc.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_19.addWidget(self.cc)


        self.verticalLayout_21.addWidget(self.widget_51)

        self.widget_71 = QWidget(self.frame_8)
        self.widget_71.setObjectName(u"widget_71")
        sizePolicy6.setHeightForWidth(self.widget_71.sizePolicy().hasHeightForWidth())
        self.widget_71.setSizePolicy(sizePolicy6)
        self.widget_71.setMinimumSize(QSize(0, 0))
        self.widget_71.setBaseSize(QSize(0, 100))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_22.setSpacing(2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.label_19 = QLabel(self.widget_71)
        self.label_19.setObjectName(u"label_19")
        sizePolicy6.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy6)

        self.horizontalLayout_22.addWidget(self.label_19)

        self.date = QLabel(self.widget_71)
        self.date.setObjectName(u"date")
        sizePolicy6.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy6)
        self.date.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.date.setFrameShape(QFrame.Shape.StyledPanel)
        self.date.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_22.addWidget(self.date)


        self.verticalLayout_21.addWidget(self.widget_71)

        self.widget_6 = QWidget(self.frame_8)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.label_18 = QLabel(self.widget_6)
        self.label_18.setObjectName(u"label_18")
        sizePolicy6.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy6)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.subject = QLabel(self.widget_6)
        self.subject.setObjectName(u"subject")
        sizePolicy6.setHeightForWidth(self.subject.sizePolicy().hasHeightForWidth())
        self.subject.setSizePolicy(sizePolicy6)
        self.subject.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_21.addWidget(self.subject)


        self.verticalLayout_21.addWidget(self.widget_6)


        self.emailLayouts.addWidget(self.frame_8)

        self.body = QLabel(self.scrollAreaWidgetContents)
        self.body.setObjectName(u"body")
        sizePolicy7.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy7)
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.Shape.Box)
        self.body.setWordWrap(True)
        self.body.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.emailLayouts.addWidget(self.body)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.emailLayouts.addItem(self.verticalSpacer_5)


        self.verticalLayout_20.addLayout(self.emailLayouts)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_17.addWidget(self.scrollArea)

        self.EmailtabWidget.addTab(self.EmailtabWidgetPage1, "")

        self.horizontalLayout_15.addWidget(self.EmailtabWidget)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.mainPages.addWidget(self.dataAnalysisPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_13 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.graphicsView_2 = QGraphicsView(self.reportsPage)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_13.addWidget(self.graphicsView_2)

        self.label_11 = QLabel(self.reportsPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_11)

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
        self.widget_61 = QWidget(self.rightMenu)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.widget_61)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.closeRightMenuBtn = QPushButton(self.widget_61)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon23 = QIcon()
        icon23.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeRightMenuBtn.setIcon(icon23)

        self.horizontalLayout_12.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_15.addWidget(self.widget_61)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.verticalLayout_16 = QVBoxLayout(self.notificationsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.notificationsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setIndent(0)

        self.verticalLayout_16.addWidget(self.label_14)

        self.rightMenuPages.addWidget(self.notificationsPage)
        self.headerEmailWiget = QWidget()
        self.headerEmailWiget.setObjectName(u"headerEmailWiget")
        self.verticalLayout_17 = QVBoxLayout(self.headerEmailWiget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.rightMenuPages.addWidget(self.headerEmailWiget)
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

        self.splitter.addWidget(self.mainBody)

        self.horizontalLayout_24.addWidget(self.splitter)


        self.verticalLayout_25.addWidget(self.frame_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.emailHederDockWidget = QDockWidget(MainWindow)
        self.emailHederDockWidget.setObjectName(u"emailHederDockWidget")
        sizePolicy7.setHeightForWidth(self.emailHederDockWidget.sizePolicy().hasHeightForWidth())
        self.emailHederDockWidget.setSizePolicy(sizePolicy7)
        self.emailHederDockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.emailHederDockWidget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        sizePolicy7.setHeightForWidth(self.dockWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_8.setSizePolicy(sizePolicy7)
        self.verticalLayout_27 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_7 = QFrame(self.dockWidgetContents_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 150, 452))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy6.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy6)
        self.verticalLayout_30 = QVBoxLayout(self.widget_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_6 = QFrame(self.widget_11)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.hiddenHederWindowBtn = QPushButton(self.frame_6)
        self.hiddenHederWindowBtn.setObjectName(u"hiddenHederWindowBtn")

        self.horizontalLayout_25.addWidget(self.hiddenHederWindowBtn)


        self.verticalLayout_30.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.widget_11)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        sizePolicy6.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy6)

        self.horizontalLayout_20.addWidget(self.label_21)

        self.idEmailHeaderLabel = QLabel(self.frame_4)
        self.idEmailHeaderLabel.setObjectName(u"idEmailHeaderLabel")
        sizePolicy6.setHeightForWidth(self.idEmailHeaderLabel.sizePolicy().hasHeightForWidth())
        self.idEmailHeaderLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_20.addWidget(self.idEmailHeaderLabel)


        self.verticalLayout_30.addWidget(self.frame_4)


        self.verticalLayout_29.addWidget(self.widget_11)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.headerEmailLabel = QLabel(self.frame_5)
        self.headerEmailLabel.setObjectName(u"headerEmailLabel")
        self.headerEmailLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.headerEmailLabel.setWordWrap(True)
        self.headerEmailLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.headerEmailLabel)


        self.verticalLayout_29.addWidget(self.frame_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)

        self.verticalLayout_29.setStretch(1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_28.addWidget(self.scrollArea_2)


        self.verticalLayout_27.addWidget(self.frame_7)

        self.emailHederDockWidget.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.emailHederDockWidget)

        self.retranslateUi(MainWindow)

        self.menuBtn.setDefault(False)
        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(1)
        self.startDataBtn.setDefault(False)
        self.rightMenuPages.setCurrentIndex(1)


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
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"FireNet E-mail Viewer", None))
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
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.seachSurname.setText("")
        self.seachSurname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Odbiorca", None))
        self.seachName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nadawca", None))
        self.searchBody.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W tre\u015bci", None))
        self.searchDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W temacie", None))
        self.startDataBtn.setText("")
        self.startDataLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endDataBtn.setText("")
        self.endDataLabel.setText("")
        self.endDataLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Do", None))
#if QT_CONFIG(tooltip)
        self.show_flags_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c wszystkie zaznaczone flagi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_flags_btn.setText("")
#if QT_CONFIG(tooltip)
        self.filter_table_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyszukaj w tabeli</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.filter_table_btn.setText("")
#if QT_CONFIG(tooltip)
        self.show_table_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c ca\u0142\u0105 tabel\u0119</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_table_btn.setText("")
        self.tagPuschBtn.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
#if QT_CONFIG(tooltip)
        self.export_pdf.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do PDF'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_pdf.setText("")
#if QT_CONFIG(tooltip)
        self.export_excel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do excel'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_excel.setText("")
        self.detailsBtn.setText(QCoreApplication.translate("MainWindow", u"P/U", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Skrzynka: ", None))
        self.sqlEmailDbName.setText(QCoreApplication.translate("MainWindow", u"Skrzynka", None))
        self.prevEmailTableBtn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.nextEmailTableBtn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Strona : ", None))
        self.pageNumberLabel.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.showSearchPanelBtn.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.selectedTagLabel.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nadawca", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Odbiorca", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Temat", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data nadani", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Flagi", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tagi", None));
        self.hederEmailBtn.setText(QCoreApplication.translate("MainWindow", u"Nag\u0142owek", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Nadawca:</span></p></body></html>", None))
        self.sender.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Odbiorca:</span></p></body></html>", None))
        self.cc.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Data wys\u0142ania:</span></p></body></html>", None))
        self.date.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Temat:</span></p></body></html>", None))
        self.subject.setText("")
        self.body.setText("")
        self.EmailtabWidget.setTabText(self.EmailtabWidget.indexOf(self.EmailtabWidgetPage1), QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Analiza danych", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ChartsPage", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright sth", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme progress", None))
        self.hiddenHederWindowBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ID Wiadomo\u015bci: ", None))
        self.idEmailHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.headerEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Header", None))
    # retranslateUi


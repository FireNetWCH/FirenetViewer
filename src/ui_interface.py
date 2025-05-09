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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDockWidget,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
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
        MainWindow.resize(2250, 654)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1264, 471))
        self.verticalLayout_50 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setEnabled(False)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(140, 146))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.homeBtn = QPushButton(self.widget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.meilBoxBtn = QPushButton(self.widget_2)
        self.meilBoxBtn.setObjectName(u"meilBoxBtn")
        self.meilBoxBtn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.meilBoxBtn)

        self.eksploratorImgBtn = QPushButton(self.widget_2)
        self.eksploratorImgBtn.setObjectName(u"eksploratorImgBtn")

        self.verticalLayout_3.addWidget(self.eksploratorImgBtn)

        self.exploratorImageBtn = QPushButton(self.widget_2)
        self.exploratorImageBtn.setObjectName(u"exploratorImageBtn")

        self.verticalLayout_3.addWidget(self.exploratorImageBtn)

        self.dataBtn = QPushButton(self.widget_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportsBtn = QPushButton(self.widget_2)
        self.reportsBtn.setObjectName(u"reportsBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/report_problem.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportsBtn.setIcon(icon2)
        self.reportsBtn.setIconSize(QSize(21, 16))

        self.verticalLayout_3.addWidget(self.reportsBtn)

        self.graphsBtn = QPushButton(self.widget_2)
        self.graphsBtn.setObjectName(u"graphsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome/solid/icons/font_awesome/solid/chart-pie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphsBtn.setIcon(icon3)

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
        self.pcTreeBtn = QPushButton(self.widget_3)
        self.pcTreeBtn.setObjectName(u"pcTreeBtn")

        self.verticalLayout_4.addWidget(self.pcTreeBtn)

        self.fileBtn = QPushButton(self.widget_3)
        self.fileBtn.setObjectName(u"fileBtn")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileBtn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.fileBtn)

        self.settingsBtn = QPushButton(self.widget_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.widget_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.widget_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_24.addWidget(self.leftMenu)

        self.splitter = QSplitter(self.frame_13)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(1)
        self.widget_8 = QWidget(self.splitter)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.centerMenu = QCustomSlideMenu(self.widget_8)
        self.centerMenu.setObjectName(u"centerMenu")
        sizePolicy1.setHeightForWidth(self.centerMenu.sizePolicy().hasHeightForWidth())
        self.centerMenu.setSizePolicy(sizePolicy1)
        self.centerMenu.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 6)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeCenterMenuBtn.sizePolicy().hasHeightForWidth())
        self.closeCenterMenuBtn.setSizePolicy(sizePolicy2)
        self.closeCenterMenuBtn.setMaximumSize(QSize(200, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/font_awesome/solid/icons/font_awesome/solid/circle-xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.centerMenuPages.sizePolicy().hasHeightForWidth())
        self.centerMenuPages.setSizePolicy(sizePolicy3)
        self.centerMenuPages.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        sizePolicy1.setHeightForWidth(self.settingsPage.sizePolicy().hasHeightForWidth())
        self.settingsPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.informationPage.sizePolicy().hasHeightForWidth())
        self.informationPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_19 = QVBoxLayout(self.informationPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pst_files_btn = QPushButton(self.informationPage)
        self.pst_files_btn.setObjectName(u"pst_files_btn")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/attach_email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pst_files_btn.setIcon(icon9)

        self.verticalLayout_19.addWidget(self.pst_files_btn)

        self.select_directory = QPushButton(self.informationPage)
        self.select_directory.setObjectName(u"select_directory")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_directory.setIcon(icon10)

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
        self.pcTreePage = QWidget()
        self.pcTreePage.setObjectName(u"pcTreePage")
        sizePolicy1.setHeightForWidth(self.pcTreePage.sizePolicy().hasHeightForWidth())
        self.pcTreePage.setSizePolicy(sizePolicy1)
        self.horizontalLayout_78 = QHBoxLayout(self.pcTreePage)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.pcTree = QTreeView(self.pcTreePage)
        self.pcTree.setObjectName(u"pcTree")
        sizePolicy3.setHeightForWidth(self.pcTree.sizePolicy().hasHeightForWidth())
        self.pcTree.setSizePolicy(sizePolicy3)

        self.horizontalLayout_78.addWidget(self.pcTree)

        self.centerMenuPages.addWidget(self.pcTreePage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout_23.addWidget(self.centerMenu)

        self.splitter.addWidget(self.widget_8)
        self.mainBody = QWidget(self.splitter)
        self.mainBody.setObjectName(u"mainBody")
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
        self.label_23 = QLabel(self.header)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_8.addWidget(self.label_23)

        self.titleTxt = QLabel(self.header)
        self.titleTxt.setObjectName(u"titleTxt")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.titleTxt.setFont(font1)

        self.horizontalLayout_8.addWidget(self.titleTxt, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.notificationBtn = QPushButton(self.frame_2)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon11 = QIcon()
        icon11.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon11)

        self.horizontalLayout_7.addWidget(self.notificationBtn)

        self.moreBtn = QPushButton(self.frame_2)
        self.moreBtn.setObjectName(u"moreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_2)
        self.profileBtn.setObjectName(u"profileBtn")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon13)

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
        self.searchinp = QLineEdit(self.serachinpCont)
        self.searchinp.setObjectName(u"searchinp")
        self.searchinp.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.searchinp)

        self.label_9 = QLabel(self.serachinpCont)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(16, 16))
        self.label_9.setMaximumSize(QSize(16, 16))
        self.label_9.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_9)

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

        self.horizontalLayout_10.addWidget(self.minimalizeBtn)

        self.restoreBtn = QPushButton(self.frame_3)
        self.restoreBtn.setObjectName(u"restoreBtn")

        self.horizontalLayout_10.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_3)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout_10.addWidget(self.closeBtn)


        self.horizontalLayout_8.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.header)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy4)
        self.horizontalLayout_11 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.verticalLayout_10 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.customQStackedWidget = QCustomQStackedWidget(self.mainPagesCont)
        self.customQStackedWidget.setObjectName(u"customQStackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_36 = QVBoxLayout(self.page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_21 = QWidget(self.page)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_37 = QVBoxLayout(self.widget_21)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.labelNameCrudBtn = QPushButton(self.widget_21)
        self.labelNameCrudBtn.setObjectName(u"labelNameCrudBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelNameCrudBtn.sizePolicy().hasHeightForWidth())
        self.labelNameCrudBtn.setSizePolicy(sizePolicy5)

        self.verticalLayout_37.addWidget(self.labelNameCrudBtn)

        self.widget_43 = QWidget(self.widget_21)
        self.widget_43.setObjectName(u"widget_43")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy6)
        self.horizontalLayout_51 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.widget_43)
        self.label_33.setObjectName(u"label_33")
        sizePolicy6.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy6)

        self.horizontalLayout_51.addWidget(self.label_33)

        self.sqlNameLabelPageLabel = QLabel(self.widget_43)
        self.sqlNameLabelPageLabel.setObjectName(u"sqlNameLabelPageLabel")
        sizePolicy6.setHeightForWidth(self.sqlNameLabelPageLabel.sizePolicy().hasHeightForWidth())
        self.sqlNameLabelPageLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_51.addWidget(self.sqlNameLabelPageLabel)


        self.verticalLayout_37.addWidget(self.widget_43)

        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_44 = QVBoxLayout(self.widget_27)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.widget_44 = QWidget(self.widget_27)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.LabelTableWidget = QTableWidget(self.widget_44)
        if (self.LabelTableWidget.columnCount() < 5):
            self.LabelTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.LabelTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.LabelTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.LabelTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.LabelTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.LabelTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.LabelTableWidget.setObjectName(u"LabelTableWidget")
        self.LabelTableWidget.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.LabelTableWidget.sizePolicy().hasHeightForWidth())
        self.LabelTableWidget.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(8)
        self.LabelTableWidget.setFont(font2)
        self.LabelTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.LabelTableWidget.horizontalHeader().setStretchLastSection(True)
        self.LabelTableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_52.addWidget(self.LabelTableWidget)

        self.EmailtabWidget_2 = QTabWidget(self.widget_44)
        self.EmailtabWidget_2.setObjectName(u"EmailtabWidget_2")
        sizePolicy3.setHeightForWidth(self.EmailtabWidget_2.sizePolicy().hasHeightForWidth())
        self.EmailtabWidget_2.setSizePolicy(sizePolicy3)
        self.EmailtabWidget_2.setTabsClosable(True)
        self.EmailtabWidgetPage1_2 = QWidget()
        self.EmailtabWidgetPage1_2.setObjectName(u"EmailtabWidgetPage1_2")
        sizePolicy4.setHeightForWidth(self.EmailtabWidgetPage1_2.sizePolicy().hasHeightForWidth())
        self.EmailtabWidgetPage1_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_31 = QHBoxLayout(self.EmailtabWidgetPage1_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.scrollArea_3 = QScrollArea(self.EmailtabWidgetPage1_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy1.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy1)
        self.scrollArea_3.setFrameShape(QFrame.Shape.Box)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 520, 360))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.emailLayouts_2 = QVBoxLayout()
        self.emailLayouts_2.setObjectName(u"emailLayouts_2")
        self.listAttachments_2 = QListWidget(self.scrollAreaWidgetContents_3)
        self.listAttachments_2.setObjectName(u"listAttachments_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listAttachments_2.sizePolicy().hasHeightForWidth())
        self.listAttachments_2.setSizePolicy(sizePolicy7)
        self.listAttachments_2.setMinimumSize(QSize(500, 150))
        self.listAttachments_2.setFrameShape(QFrame.Shape.Box)
        self.listAttachments_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.listAttachments_2.setLineWidth(1)
        self.listAttachments_2.setMidLineWidth(1)
        self.listAttachments_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listAttachments_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.listAttachments_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.listAttachments_2.setAutoScrollMargin(5)
        self.listAttachments_2.setFlow(QListView.Flow.LeftToRight)
        self.listAttachments_2.setModelColumn(0)
        self.listAttachments_2.setUniformItemSizes(False)
        self.listAttachments_2.setBatchSize(100)

        self.emailLayouts_2.addWidget(self.listAttachments_2)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy8)
        self.frame_14.setMinimumSize(QSize(500, 0))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_14)
        self.verticalLayout_35.setSpacing(3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.hederEmailBtn_2 = QPushButton(self.frame_14)
        self.hederEmailBtn_2.setObjectName(u"hederEmailBtn_2")
        sizePolicy8.setHeightForWidth(self.hederEmailBtn_2.sizePolicy().hasHeightForWidth())
        self.hederEmailBtn_2.setSizePolicy(sizePolicy8)
        self.hederEmailBtn_2.setMinimumSize(QSize(125, 0))

        self.verticalLayout_35.addWidget(self.hederEmailBtn_2)

        self.widget_22 = QWidget(self.frame_14)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy6.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy6)
        self.horizontalLayout_32 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_32.setSpacing(2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(2, 2, 2, 2)
        self.label_25 = QLabel(self.widget_22)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)
        self.label_25.setIndent(3)

        self.horizontalLayout_32.addWidget(self.label_25)

        self.sender_2 = QLabel(self.widget_22)
        self.sender_2.setObjectName(u"sender_2")
        sizePolicy6.setHeightForWidth(self.sender_2.sizePolicy().hasHeightForWidth())
        self.sender_2.setSizePolicy(sizePolicy6)
        self.sender_2.setFrameShape(QFrame.Shape.Panel)
        self.sender_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_32.addWidget(self.sender_2)


        self.verticalLayout_35.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.frame_14)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy6.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy6)
        self.widget_23.setMinimumSize(QSize(0, 0))
        self.widget_23.setBaseSize(QSize(0, 0))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_33.setSpacing(2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(2, 2, 2, 2)
        self.label_27 = QLabel(self.widget_23)
        self.label_27.setObjectName(u"label_27")
        sizePolicy6.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy6)

        self.horizontalLayout_33.addWidget(self.label_27)

        self.cc_2 = QLabel(self.widget_23)
        self.cc_2.setObjectName(u"cc_2")
        sizePolicy6.setHeightForWidth(self.cc_2.sizePolicy().hasHeightForWidth())
        self.cc_2.setSizePolicy(sizePolicy6)
        self.cc_2.setFrameShape(QFrame.Shape.Box)
        self.cc_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_33.addWidget(self.cc_2)


        self.verticalLayout_35.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.frame_14)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy6.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy6)
        self.widget_24.setMinimumSize(QSize(0, 0))
        self.widget_24.setBaseSize(QSize(0, 100))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_34.setSpacing(2)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(2, 2, 2, 2)
        self.label_28 = QLabel(self.widget_24)
        self.label_28.setObjectName(u"label_28")
        sizePolicy6.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy6)

        self.horizontalLayout_34.addWidget(self.label_28)

        self.date_2 = QLabel(self.widget_24)
        self.date_2.setObjectName(u"date_2")
        sizePolicy6.setHeightForWidth(self.date_2.sizePolicy().hasHeightForWidth())
        self.date_2.setSizePolicy(sizePolicy6)
        self.date_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.date_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.date_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_34.addWidget(self.date_2)


        self.verticalLayout_35.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.frame_14)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy6.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy6)
        self.widget_25.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_35.setSpacing(2)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(2, 2, 2, 2)
        self.label_29 = QLabel(self.widget_25)
        self.label_29.setObjectName(u"label_29")
        sizePolicy6.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy6)

        self.horizontalLayout_35.addWidget(self.label_29)

        self.subject_2 = QLabel(self.widget_25)
        self.subject_2.setObjectName(u"subject_2")
        sizePolicy6.setHeightForWidth(self.subject_2.sizePolicy().hasHeightForWidth())
        self.subject_2.setSizePolicy(sizePolicy6)
        self.subject_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_35.addWidget(self.subject_2)


        self.verticalLayout_35.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.frame_14)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy6.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy6)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.widget_26)
        self.label_30.setObjectName(u"label_30")
        sizePolicy6.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_30.setFont(font3)

        self.horizontalLayout_37.addWidget(self.label_30)

        self.frazeLabel = QLabel(self.widget_26)
        self.frazeLabel.setObjectName(u"frazeLabel")
        sizePolicy6.setHeightForWidth(self.frazeLabel.sizePolicy().hasHeightForWidth())
        self.frazeLabel.setSizePolicy(sizePolicy6)
        self.frazeLabel.setFrameShape(QFrame.Shape.Box)
        self.frazeLabel.setWordWrap(True)

        self.horizontalLayout_37.addWidget(self.frazeLabel)


        self.verticalLayout_35.addWidget(self.widget_26)


        self.emailLayouts_2.addWidget(self.frame_14)

        self.body_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.body_2.setObjectName(u"body_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.body_2.sizePolicy().hasHeightForWidth())
        self.body_2.setSizePolicy(sizePolicy9)
        self.body_2.setStyleSheet(u"")
        self.body_2.setFrameShape(QFrame.Shape.Box)
        self.body_2.setWordWrap(True)
        self.body_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.emailLayouts_2.addWidget(self.body_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.emailLayouts_2.addItem(self.verticalSpacer_6)


        self.verticalLayout_34.addLayout(self.emailLayouts_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_31.addWidget(self.scrollArea_3)

        self.EmailtabWidget_2.addTab(self.EmailtabWidgetPage1_2, "")

        self.horizontalLayout_52.addWidget(self.EmailtabWidget_2)


        self.verticalLayout_44.addWidget(self.widget_44)


        self.verticalLayout_37.addWidget(self.widget_27)


        self.verticalLayout_36.addWidget(self.widget_21)

        self.customQStackedWidget.addWidget(self.page)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_12 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 0, -1, 0)
        self.serchEmailFrame = QFrame(self.dataAnalysisPage)
        self.serchEmailFrame.setObjectName(u"serchEmailFrame")
        sizePolicy5.setHeightForWidth(self.serchEmailFrame.sizePolicy().hasHeightForWidth())
        self.serchEmailFrame.setSizePolicy(sizePolicy5)
        self.serchEmailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.serchEmailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.serchEmailFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, 0)
        self.frame_11 = QFrame(self.serchEmailFrame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_22.setContentsMargins(0, 0, -1, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 2, -1, 2)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_10)


        self.verticalLayout_22.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.seachName = QLineEdit(self.frame_10)
        self.seachName.setObjectName(u"seachName")

        self.horizontalLayout_14.addWidget(self.seachName)

        self.seachSurname = QLineEdit(self.frame_10)
        self.seachSurname.setObjectName(u"seachSurname")

        self.horizontalLayout_14.addWidget(self.seachSurname)

        self.searchDate = QLineEdit(self.frame_10)
        self.searchDate.setObjectName(u"searchDate")

        self.horizontalLayout_14.addWidget(self.searchDate)

        self.searchBody = QLineEdit(self.frame_10)
        self.searchBody.setObjectName(u"searchBody")

        self.horizontalLayout_14.addWidget(self.searchBody)

        self.startDataBtn = QPushButton(self.frame_10)
        self.startDataBtn.setObjectName(u"startDataBtn")
        sizePolicy6.setHeightForWidth(self.startDataBtn.sizePolicy().hasHeightForWidth())
        self.startDataBtn.setSizePolicy(sizePolicy6)
        self.startDataBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startDataBtn.setAutoFillBackground(False)
        self.startDataBtn.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.startDataBtn.setAutoRepeatInterval(100)
        self.startDataBtn.setAutoDefault(False)

        self.horizontalLayout_14.addWidget(self.startDataBtn)

        self.startDataLabel = QLineEdit(self.frame_10)
        self.startDataLabel.setObjectName(u"startDataLabel")
        self.startDataLabel.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.startDataLabel)

        self.endDataLabel = QLineEdit(self.frame_10)
        self.endDataLabel.setObjectName(u"endDataLabel")
        self.endDataLabel.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.endDataLabel)

        self.show_flags_btn = QCustomQPushButton(self.frame_10)
        self.show_flags_btn.setObjectName(u"show_flags_btn")
        self.show_flags_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_flags_btn.setIcon(icon14)
        self.show_flags_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.show_flags_btn)

        self.show_table_btn = QPushButton(self.frame_10)
        self.show_table_btn.setObjectName(u"show_table_btn")
        self.show_table_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.show_table_btn)

        self.clearBtn = QPushButton(self.frame_10)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.clearBtn)

        self.tagPuschBtn = QPushButton(self.frame_10)
        self.tagPuschBtn.setObjectName(u"tagPuschBtn")
        sizePolicy4.setHeightForWidth(self.tagPuschBtn.sizePolicy().hasHeightForWidth())
        self.tagPuschBtn.setSizePolicy(sizePolicy4)
        self.tagPuschBtn.setMinimumSize(QSize(175, 0))
        self.tagPuschBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.tagPuschBtn)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 1)
        self.horizontalLayout_14.setStretch(3, 1)
        self.horizontalLayout_14.setStretch(5, 1)
        self.horizontalLayout_14.setStretch(6, 1)
        self.horizontalLayout_14.setStretch(10, 1)

        self.verticalLayout_22.addWidget(self.frame_10)


        self.horizontalLayout_18.addWidget(self.frame_11)

        self.widget_41 = QWidget(self.serchEmailFrame)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy6.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy6)
        self.verticalLayout_42 = QVBoxLayout(self.widget_41)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, -1, 0)
        self.widget_7 = QWidget(self.widget_41)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy5.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy5)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)
        self.export_pdf = QPushButton(self.widget_7)
        self.export_pdf.setObjectName(u"export_pdf")
        self.export_pdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/font_awesome/regular/icons/font_awesome/regular/file-pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_pdf.setIcon(icon15)

        self.horizontalLayout_13.addWidget(self.export_pdf)

        self.exportExelBtn = QPushButton(self.widget_7)
        self.exportExelBtn.setObjectName(u"exportExelBtn")
        self.exportExelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/font_awesome/regular/icons/font_awesome/regular/file-excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportExelBtn.setIcon(icon16)

        self.horizontalLayout_13.addWidget(self.exportExelBtn)

        self.detailsBtn = QPushButton(self.widget_7)
        self.detailsBtn.setObjectName(u"detailsBtn")

        self.horizontalLayout_13.addWidget(self.detailsBtn)


        self.verticalLayout_42.addWidget(self.widget_7)

        self.widget_42 = QWidget(self.widget_41)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.exportCountLabel = QLabel(self.widget_42)
        self.exportCountLabel.setObjectName(u"exportCountLabel")

        self.horizontalLayout_50.addWidget(self.exportCountLabel)


        self.verticalLayout_42.addWidget(self.widget_42)

        self.progressBar = QProgressBar(self.widget_41)
        self.progressBar.setObjectName(u"progressBar")
        font4 = QFont()
        font4.setPointSize(5)
        self.progressBar.setFont(font4)
        self.progressBar.setValue(100)

        self.verticalLayout_42.addWidget(self.progressBar)


        self.horizontalLayout_18.addWidget(self.widget_41)


        self.verticalLayout_12.addWidget(self.serchEmailFrame)

        self.frame_9 = QFrame(self.dataAnalysisPage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setSpacing(1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 0, 2, 2)
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        sizePolicy9.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy9)

        self.horizontalLayout_16.addWidget(self.label_22)

        self.sqlEmailDbName = QLabel(self.frame_9)
        self.sqlEmailDbName.setObjectName(u"sqlEmailDbName")
        sizePolicy6.setHeightForWidth(self.sqlEmailDbName.sizePolicy().hasHeightForWidth())
        self.sqlEmailDbName.setSizePolicy(sizePolicy6)

        self.horizontalLayout_16.addWidget(self.sqlEmailDbName)

        self.dirNameLabel = QLabel(self.frame_9)
        self.dirNameLabel.setObjectName(u"dirNameLabel")
        self.dirNameLabel.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_16.addWidget(self.dirNameLabel)


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
        self.prevEmailTableBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.prevEmailTableBtn)

        self.label_20 = QLabel(self.widget_9)
        self.label_20.setObjectName(u"label_20")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy10)

        self.horizontalLayout_4.addWidget(self.label_20)

        self.jumpToPagelineEdit = QLineEdit(self.widget_9)
        self.jumpToPagelineEdit.setObjectName(u"jumpToPagelineEdit")

        self.horizontalLayout_4.addWidget(self.jumpToPagelineEdit)

        self.pageNumberLabel = QLabel(self.widget_9)
        self.pageNumberLabel.setObjectName(u"pageNumberLabel")
        sizePolicy10.setHeightForWidth(self.pageNumberLabel.sizePolicy().hasHeightForWidth())
        self.pageNumberLabel.setSizePolicy(sizePolicy10)

        self.horizontalLayout_4.addWidget(self.pageNumberLabel)

        self.nextEmailTableBtn = QPushButton(self.widget_9)
        self.nextEmailTableBtn.setObjectName(u"nextEmailTableBtn")
        sizePolicy6.setHeightForWidth(self.nextEmailTableBtn.sizePolicy().hasHeightForWidth())
        self.nextEmailTableBtn.setSizePolicy(sizePolicy6)
        self.nextEmailTableBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.nextEmailTableBtn)

        self.showSearchPanelBtn = QPushButton(self.widget_9)
        self.showSearchPanelBtn.setObjectName(u"showSearchPanelBtn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.showSearchPanelBtn.sizePolicy().hasHeightForWidth())
        self.showSearchPanelBtn.setSizePolicy(sizePolicy11)
        self.showSearchPanelBtn.setMinimumSize(QSize(100, 0))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        self.showSearchPanelBtn.setFont(font5)
        self.showSearchPanelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setFont(font2)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_15.addWidget(self.tableWidget)

        self.EmailtabWidget = QTabWidget(self.dataAnalysisPage)
        self.EmailtabWidget.setObjectName(u"EmailtabWidget")
        sizePolicy3.setHeightForWidth(self.EmailtabWidget.sizePolicy().hasHeightForWidth())
        self.EmailtabWidget.setSizePolicy(sizePolicy3)
        self.EmailtabWidget.setTabsClosable(True)
        self.EmailtabWidgetPage1 = QWidget()
        self.EmailtabWidgetPage1.setObjectName(u"EmailtabWidgetPage1")
        sizePolicy4.setHeightForWidth(self.EmailtabWidgetPage1.sizePolicy().hasHeightForWidth())
        self.EmailtabWidgetPage1.setSizePolicy(sizePolicy4)
        self.horizontalLayout_17 = QHBoxLayout(self.EmailtabWidgetPage1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.scrollArea = QScrollArea(self.EmailtabWidgetPage1)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.Shape.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 520, 382))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.emailLayouts = QVBoxLayout()
        self.emailLayouts.setObjectName(u"emailLayouts")
        self.listAttachments = QListWidget(self.scrollAreaWidgetContents)
        self.listAttachments.setObjectName(u"listAttachments")
        sizePolicy7.setHeightForWidth(self.listAttachments.sizePolicy().hasHeightForWidth())
        self.listAttachments.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy8)
        self.frame_8.setMinimumSize(QSize(500, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.hederEmailBtn = QPushButton(self.frame_8)
        self.hederEmailBtn.setObjectName(u"hederEmailBtn")
        sizePolicy8.setHeightForWidth(self.hederEmailBtn.sizePolicy().hasHeightForWidth())
        self.hederEmailBtn.setSizePolicy(sizePolicy8)
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

        self.recipientsLabel = QLabel(self.widget_51)
        self.recipientsLabel.setObjectName(u"recipientsLabel")
        sizePolicy6.setHeightForWidth(self.recipientsLabel.sizePolicy().hasHeightForWidth())
        self.recipientsLabel.setSizePolicy(sizePolicy6)
        self.recipientsLabel.setFrameShape(QFrame.Shape.Box)
        self.recipientsLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_19.addWidget(self.recipientsLabel)


        self.verticalLayout_21.addWidget(self.widget_51)

        self.ccWidget = QWidget(self.frame_8)
        self.ccWidget.setObjectName(u"ccWidget")
        sizePolicy6.setHeightForWidth(self.ccWidget.sizePolicy().hasHeightForWidth())
        self.ccWidget.setSizePolicy(sizePolicy6)
        self.horizontalLayout_30 = QHBoxLayout(self.ccWidget)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.ccTitleLabel = QLabel(self.ccWidget)
        self.ccTitleLabel.setObjectName(u"ccTitleLabel")
        sizePolicy6.setHeightForWidth(self.ccTitleLabel.sizePolicy().hasHeightForWidth())
        self.ccTitleLabel.setSizePolicy(sizePolicy6)
        self.ccTitleLabel.setFont(font3)

        self.horizontalLayout_30.addWidget(self.ccTitleLabel)

        self.ccLabel = QLabel(self.ccWidget)
        self.ccLabel.setObjectName(u"ccLabel")
        self.ccLabel.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_30.addWidget(self.ccLabel)


        self.verticalLayout_21.addWidget(self.ccWidget)

        self.bccWidget = QWidget(self.frame_8)
        self.bccWidget.setObjectName(u"bccWidget")
        sizePolicy6.setHeightForWidth(self.bccWidget.sizePolicy().hasHeightForWidth())
        self.bccWidget.setSizePolicy(sizePolicy6)
        self.horizontalLayout_36 = QHBoxLayout(self.bccWidget)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.bccTitleLabel = QLabel(self.bccWidget)
        self.bccTitleLabel.setObjectName(u"bccTitleLabel")
        sizePolicy6.setHeightForWidth(self.bccTitleLabel.sizePolicy().hasHeightForWidth())
        self.bccTitleLabel.setSizePolicy(sizePolicy6)
        self.bccTitleLabel.setFont(font3)

        self.horizontalLayout_36.addWidget(self.bccTitleLabel)

        self.bccLabel = QLabel(self.bccWidget)
        self.bccLabel.setObjectName(u"bccLabel")
        sizePolicy6.setHeightForWidth(self.bccLabel.sizePolicy().hasHeightForWidth())
        self.bccLabel.setSizePolicy(sizePolicy6)
        self.bccLabel.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_36.addWidget(self.bccLabel)


        self.verticalLayout_21.addWidget(self.bccWidget)

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

        self.widget_50 = QWidget(self.widget_6)
        self.widget_50.setObjectName(u"widget_50")

        self.horizontalLayout_21.addWidget(self.widget_50)

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
        sizePolicy9.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy9)
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

        self.widget_46 = QWidget(self.dataAnalysisPage)
        self.widget_46.setObjectName(u"widget_46")
        sizePolicy2.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy2)
        self.horizontalLayout_53 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_6 = QScrollArea(self.widget_46)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 98, 28))
        self.horizontalLayout_56 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.widget_48 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_48.setObjectName(u"widget_48")
        sizePolicy1.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy1)
        self.horizontalLayout_38 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_56.addWidget(self.widget_48)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_53.addWidget(self.scrollArea_6)

        self.scrollArea_5 = QScrollArea(self.widget_46)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 98, 28))
        self.horizontalLayout_55 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.widget_45 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_45.setObjectName(u"widget_45")
        sizePolicy1.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy1)
        self.widget_45.setSizeIncrement(QSize(0, 1000))
        self.widget_45.setBaseSize(QSize(0, 100))
        self.widget_45.setAutoFillBackground(False)
        self.horizontalLayout_54 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_55.addWidget(self.widget_45)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_53.addWidget(self.scrollArea_5)


        self.verticalLayout_12.addWidget(self.widget_46)

        self.customQStackedWidget.addWidget(self.dataAnalysisPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_11 = QVBoxLayout(self.homePage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.widget_12 = QWidget(self.homePage)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_24 = QVBoxLayout(self.widget_12)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_26 = QVBoxLayout(self.widget_14)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(self.widget_14)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_26.addWidget(self.label_7)


        self.verticalLayout_24.addWidget(self.widget_14)


        self.verticalLayout_11.addWidget(self.widget_12)

        self.homePageFooterWidget = QWidget(self.homePage)
        self.homePageFooterWidget.setObjectName(u"homePageFooterWidget")
        self.verticalLayout_25 = QVBoxLayout(self.homePageFooterWidget)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)

        self.widget_13 = QWidget(self.homePageFooterWidget)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.widget_38 = QWidget(self.widget_13)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_2)

        self.widget_35 = QWidget(self.widget_38)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.tagiBtn = QPushButton(self.widget_35)
        self.tagiBtn.setObjectName(u"tagiBtn")
        sizePolicy2.setHeightForWidth(self.tagiBtn.sizePolicy().hasHeightForWidth())
        self.tagiBtn.setSizePolicy(sizePolicy2)
        self.tagiBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_44.addWidget(self.tagiBtn)


        self.horizontalLayout_47.addWidget(self.widget_35)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget_13)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_4)

        self.widget_36 = QWidget(self.widget_39)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.lableBtn = QPushButton(self.widget_36)
        self.lableBtn.setObjectName(u"lableBtn")
        sizePolicy2.setHeightForWidth(self.lableBtn.sizePolicy().hasHeightForWidth())
        self.lableBtn.setSizePolicy(sizePolicy2)
        self.lableBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_45.addWidget(self.lableBtn)


        self.horizontalLayout_48.addWidget(self.widget_36)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_6.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_13)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_6)

        self.widget_37 = QWidget(self.widget_40)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.contactBtn = QPushButton(self.widget_37)
        self.contactBtn.setObjectName(u"contactBtn")
        sizePolicy2.setHeightForWidth(self.contactBtn.sizePolicy().hasHeightForWidth())
        self.contactBtn.setSizePolicy(sizePolicy2)
        self.contactBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_46.addWidget(self.contactBtn)


        self.horizontalLayout_49.addWidget(self.widget_37)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_6.addWidget(self.widget_40)


        self.verticalLayout_25.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.homePageFooterWidget)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_31 = QVBoxLayout(self.widget_16)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.label_24 = QLabel(self.widget_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_24)

        self.ofertaBtn = QPushButton(self.widget_16)
        self.ofertaBtn.setObjectName(u"ofertaBtn")
        sizePolicy6.setHeightForWidth(self.ofertaBtn.sizePolicy().hasHeightForWidth())
        self.ofertaBtn.setSizePolicy(sizePolicy6)
        self.ofertaBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ofertaBtn.setIconSize(QSize(40, 40))
        self.ofertaBtn.setAutoExclusive(False)
        self.ofertaBtn.setFlat(False)

        self.verticalLayout_31.addWidget(self.ofertaBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_25.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_33 = QVBoxLayout(self.widget_17)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.TutorialLabel = QLabel(self.widget_17)
        self.TutorialLabel.setObjectName(u"TutorialLabel")
        self.TutorialLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.TutorialLabel)

        self.yotubeBtn = QPushButton(self.widget_17)
        self.yotubeBtn.setObjectName(u"yotubeBtn")
        self.yotubeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_33.addWidget(self.yotubeBtn)


        self.horizontalLayout_25.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_32 = QVBoxLayout(self.widget_18)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_26 = QLabel(self.widget_20)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_26)


        self.verticalLayout_32.addWidget(self.widget_20)

        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.linkedinBtn = QPushButton(self.widget_19)
        self.linkedinBtn.setObjectName(u"linkedinBtn")
        self.linkedinBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.linkedinBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_28.addWidget(self.linkedinBtn)

        self.fbBtn = QPushButton(self.widget_19)
        self.fbBtn.setObjectName(u"fbBtn")
        self.fbBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fbBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_28.addWidget(self.fbBtn)

        self.wwwBtn = QPushButton(self.widget_19)
        self.wwwBtn.setObjectName(u"wwwBtn")
        self.wwwBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.wwwBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_28.addWidget(self.wwwBtn)


        self.verticalLayout_32.addWidget(self.widget_19)


        self.horizontalLayout_25.addWidget(self.widget_18)


        self.verticalLayout_25.addWidget(self.widget_15)


        self.verticalLayout_11.addWidget(self.homePageFooterWidget)

        self.customQStackedWidget.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_13 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.function_bar = QFrame(self.reportsPage)
        self.function_bar.setObjectName(u"function_bar")
        sizePolicy7.setHeightForWidth(self.function_bar.sizePolicy().hasHeightForWidth())
        self.function_bar.setSizePolicy(sizePolicy7)
        self.function_bar.setMinimumSize(QSize(679, 288))
        self.function_bar.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.function_bar.setAutoFillBackground(True)
        self.verticalLayout_49 = QVBoxLayout(self.function_bar)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_18 = QFrame(self.function_bar)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy6)
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.left_btn = QPushButton(self.frame_18)
        self.left_btn.setObjectName(u"left_btn")
        sizePolicy6.setHeightForWidth(self.left_btn.sizePolicy().hasHeightForWidth())
        self.left_btn.setSizePolicy(sizePolicy6)
        self.left_btn.setAutoDefault(False)
        self.left_btn.setFlat(False)

        self.horizontalLayout_59.addWidget(self.left_btn)

        self.rigth_btn = QPushButton(self.frame_18)
        self.rigth_btn.setObjectName(u"rigth_btn")
        self.rigth_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.rigth_btn.sizePolicy().hasHeightForWidth())
        self.rigth_btn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_59.addWidget(self.rigth_btn)

        self.up_btn = QPushButton(self.frame_18)
        self.up_btn.setObjectName(u"up_btn")
        sizePolicy6.setHeightForWidth(self.up_btn.sizePolicy().hasHeightForWidth())
        self.up_btn.setSizePolicy(sizePolicy6)
        self.up_btn.setAutoDefault(False)
        self.up_btn.setFlat(False)

        self.horizontalLayout_59.addWidget(self.up_btn)


        self.verticalLayout_49.addWidget(self.frame_18)

        self.pathLabel = QLabel(self.function_bar)
        self.pathLabel.setObjectName(u"pathLabel")
        sizePolicy6.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy6)
        self.pathLabel.setAutoFillBackground(False)
        self.pathLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.pathLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.pathLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pathLabel.setWordWrap(False)

        self.verticalLayout_49.addWidget(self.pathLabel)

        self.tabWidget = QTabWidget(self.function_bar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)

        self.verticalLayout_49.addWidget(self.tabWidget)


        self.verticalLayout_13.addWidget(self.function_bar)

        self.customQStackedWidget.addWidget(self.reportsPage)
        self.pcInfoPage = QWidget()
        self.pcInfoPage.setObjectName(u"pcInfoPage")
        self.verticalLayout_48 = QVBoxLayout(self.pcInfoPage)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.tabWidget_3 = QTabWidget(self.pcInfoPage)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.softwareInfoTableWidget = QTableWidget(self.tab)
        self.softwareInfoTableWidget.setObjectName(u"softwareInfoTableWidget")

        self.gridLayout.addWidget(self.softwareInfoTableWidget, 0, 1, 1, 1)

        self.deviceInfoTableWidget = QTableWidget(self.tab)
        self.deviceInfoTableWidget.setObjectName(u"deviceInfoTableWidget")

        self.gridLayout.addWidget(self.deviceInfoTableWidget, 0, 0, 1, 1)

        self.networkConfigTableWidget = QTableWidget(self.tab)
        self.networkConfigTableWidget.setObjectName(u"networkConfigTableWidget")

        self.gridLayout.addWidget(self.networkConfigTableWidget, 1, 0, 1, 1)

        self.installedSoftwareTableWidget = QTableWidget(self.tab)
        self.installedSoftwareTableWidget.setObjectName(u"installedSoftwareTableWidget")

        self.gridLayout.addWidget(self.installedSoftwareTableWidget, 1, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab, "")

        self.verticalLayout_48.addWidget(self.tabWidget_3)

        self.customQStackedWidget.addWidget(self.pcInfoPage)
        self.browserPage = QWidget()
        self.browserPage.setObjectName(u"browserPage")
        self.horizontalLayout_39 = QHBoxLayout(self.browserPage)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.widget_65 = QWidget(self.browserPage)
        self.widget_65.setObjectName(u"widget_65")
        self.verticalLayout_56 = QVBoxLayout(self.widget_65)
        self.verticalLayout_56.setSpacing(3)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_66 = QWidget(self.widget_65)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_76.setSpacing(3)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(-1, 0, 0, 0)
        self.downloadDomenLineEdit = QLineEdit(self.widget_66)
        self.downloadDomenLineEdit.setObjectName(u"downloadDomenLineEdit")

        self.horizontalLayout_76.addWidget(self.downloadDomenLineEdit)

        self.fileNameLineEdit = QLineEdit(self.widget_66)
        self.fileNameLineEdit.setObjectName(u"fileNameLineEdit")

        self.horizontalLayout_76.addWidget(self.fileNameLineEdit)

        self.downloadHistoryCalendarBtn = QPushButton(self.widget_66)
        self.downloadHistoryCalendarBtn.setObjectName(u"downloadHistoryCalendarBtn")

        self.horizontalLayout_76.addWidget(self.downloadHistoryCalendarBtn)

        self.startDateDownloadLineEdit = QLineEdit(self.widget_66)
        self.startDateDownloadLineEdit.setObjectName(u"startDateDownloadLineEdit")

        self.horizontalLayout_76.addWidget(self.startDateDownloadLineEdit)

        self.endDateDownloadLineEdit = QLineEdit(self.widget_66)
        self.endDateDownloadLineEdit.setObjectName(u"endDateDownloadLineEdit")

        self.horizontalLayout_76.addWidget(self.endDateDownloadLineEdit)

        self.downloadProfileComboBox = QComboBox(self.widget_66)
        self.downloadProfileComboBox.setObjectName(u"downloadProfileComboBox")

        self.horizontalLayout_76.addWidget(self.downloadProfileComboBox)

        self.downloadBrowserComboBox = QComboBox(self.widget_66)
        self.downloadBrowserComboBox.setObjectName(u"downloadBrowserComboBox")

        self.horizontalLayout_76.addWidget(self.downloadBrowserComboBox)

        self.downladaUserComboBox = QComboBox(self.widget_66)
        self.downladaUserComboBox.setObjectName(u"downladaUserComboBox")

        self.horizontalLayout_76.addWidget(self.downladaUserComboBox)


        self.verticalLayout_56.addWidget(self.widget_66)

        self.label_11 = QLabel(self.widget_65)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_56.addWidget(self.label_11)

        self.widget_64 = QWidget(self.widget_65)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_75.setSpacing(3)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.networkBrowserTable = QTableWidget(self.widget_64)
        self.networkBrowserTable.setObjectName(u"networkBrowserTable")

        self.horizontalLayout_75.addWidget(self.networkBrowserTable)

        self.widget_52 = QWidget(self.widget_64)
        self.widget_52.setObjectName(u"widget_52")
        sizePolicy1.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy1)
        self.widget_52.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.widget_52.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.widget_52.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_52 = QVBoxLayout(self.widget_52)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.widget_52)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        sizePolicy1.setHeightForWidth(self.scrollArea_7.sizePolicy().hasHeightForWidth())
        self.scrollArea_7.setSizePolicy(sizePolicy1)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 228, 179))
        self.verticalLayout_53 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_15)

        self.widget_511 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_511.setObjectName(u"widget_511")
        sizePolicy6.setHeightForWidth(self.widget_511.sizePolicy().hasHeightForWidth())
        self.widget_511.setSizePolicy(sizePolicy6)
        self.horizontalLayout_62 = QHBoxLayout(self.widget_511)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.urlStaticLabel = QLabel(self.widget_511)
        self.urlStaticLabel.setObjectName(u"urlStaticLabel")
        sizePolicy6.setHeightForWidth(self.urlStaticLabel.sizePolicy().hasHeightForWidth())
        self.urlStaticLabel.setSizePolicy(sizePolicy6)
        self.urlStaticLabel.setFont(font3)

        self.horizontalLayout_62.addWidget(self.urlStaticLabel)

        self.urlLabel = QLabel(self.widget_511)
        self.urlLabel.setObjectName(u"urlLabel")
        sizePolicy10.setHeightForWidth(self.urlLabel.sizePolicy().hasHeightForWidth())
        self.urlLabel.setSizePolicy(sizePolicy10)
        self.urlLabel.setWordWrap(False)

        self.horizontalLayout_62.addWidget(self.urlLabel)


        self.verticalLayout_53.addWidget(self.widget_511)

        self.widget_49 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_49.setObjectName(u"widget_49")
        sizePolicy6.setHeightForWidth(self.widget_49.sizePolicy().hasHeightForWidth())
        self.widget_49.setSizePolicy(sizePolicy6)
        self.horizontalLayout_61 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.downloadStaticPath = QLabel(self.widget_49)
        self.downloadStaticPath.setObjectName(u"downloadStaticPath")
        sizePolicy6.setHeightForWidth(self.downloadStaticPath.sizePolicy().hasHeightForWidth())
        self.downloadStaticPath.setSizePolicy(sizePolicy6)
        self.downloadStaticPath.setFont(font3)

        self.horizontalLayout_61.addWidget(self.downloadStaticPath)

        self.pathDownloadLabel = QLabel(self.widget_49)
        self.pathDownloadLabel.setObjectName(u"pathDownloadLabel")
        sizePolicy9.setHeightForWidth(self.pathDownloadLabel.sizePolicy().hasHeightForWidth())
        self.pathDownloadLabel.setSizePolicy(sizePolicy9)
        self.pathDownloadLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pathDownloadLabel.setWordWrap(False)

        self.horizontalLayout_61.addWidget(self.pathDownloadLabel)


        self.verticalLayout_53.addWidget(self.widget_49)

        self.widget_56 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_56.setObjectName(u"widget_56")
        sizePolicy6.setHeightForWidth(self.widget_56.sizePolicy().hasHeightForWidth())
        self.widget_56.setSizePolicy(sizePolicy6)
        self.horizontalLayout_66 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_56)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.horizontalLayout_66.addWidget(self.label_41)

        self.sizeFileLabel = QLabel(self.widget_56)
        self.sizeFileLabel.setObjectName(u"sizeFileLabel")

        self.horizontalLayout_66.addWidget(self.sizeFileLabel)


        self.verticalLayout_53.addWidget(self.widget_56)

        self.widget_53 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_53.setObjectName(u"widget_53")
        sizePolicy6.setHeightForWidth(self.widget_53.sizePolicy().hasHeightForWidth())
        self.widget_53.setSizePolicy(sizePolicy6)
        self.horizontalLayout_63 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.widget_53)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.horizontalLayout_63.addWidget(self.label_35)

        self.startTimeLabel = QLabel(self.widget_53)
        self.startTimeLabel.setObjectName(u"startTimeLabel")

        self.horizontalLayout_63.addWidget(self.startTimeLabel)


        self.verticalLayout_53.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_54.setObjectName(u"widget_54")
        sizePolicy6.setHeightForWidth(self.widget_54.sizePolicy().hasHeightForWidth())
        self.widget_54.setSizePolicy(sizePolicy6)
        self.horizontalLayout_64 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_54)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.horizontalLayout_64.addWidget(self.label_37)

        self.endTimeLabel = QLabel(self.widget_54)
        self.endTimeLabel.setObjectName(u"endTimeLabel")

        self.horizontalLayout_64.addWidget(self.endTimeLabel)


        self.verticalLayout_53.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_55.setObjectName(u"widget_55")
        sizePolicy6.setHeightForWidth(self.widget_55.sizePolicy().hasHeightForWidth())
        self.widget_55.setSizePolicy(sizePolicy6)
        self.horizontalLayout_65 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_55)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.horizontalLayout_65.addWidget(self.label_39)

        self.downloadTimeLabel = QLabel(self.widget_55)
        self.downloadTimeLabel.setObjectName(u"downloadTimeLabel")

        self.horizontalLayout_65.addWidget(self.downloadTimeLabel)


        self.verticalLayout_53.addWidget(self.widget_55)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_11)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_52.addWidget(self.scrollArea_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_8)


        self.horizontalLayout_75.addWidget(self.widget_52)


        self.verticalLayout_56.addWidget(self.widget_64)


        self.horizontalLayout_39.addWidget(self.widget_65)

        self.customQStackedWidget.addWidget(self.browserPage)
        self.disgImagePage = QWidget()
        self.disgImagePage.setObjectName(u"disgImagePage")
        self.verticalLayout_47 = QVBoxLayout(self.disgImagePage)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_15 = QFrame(self.disgImagePage)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy9.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy9)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_15)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy6)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.left_btn_2 = QPushButton(self.frame_16)
        self.left_btn_2.setObjectName(u"left_btn_2")
        sizePolicy6.setHeightForWidth(self.left_btn_2.sizePolicy().hasHeightForWidth())
        self.left_btn_2.setSizePolicy(sizePolicy6)
        self.left_btn_2.setAutoDefault(False)
        self.left_btn_2.setFlat(False)

        self.horizontalLayout_58.addWidget(self.left_btn_2)

        self.rigth_btn_2 = QPushButton(self.frame_16)
        self.rigth_btn_2.setObjectName(u"rigth_btn_2")
        self.rigth_btn_2.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.rigth_btn_2.sizePolicy().hasHeightForWidth())
        self.rigth_btn_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_58.addWidget(self.rigth_btn_2)

        self.up_btn_2 = QPushButton(self.frame_16)
        self.up_btn_2.setObjectName(u"up_btn_2")
        sizePolicy6.setHeightForWidth(self.up_btn_2.sizePolicy().hasHeightForWidth())
        self.up_btn_2.setSizePolicy(sizePolicy6)
        self.up_btn_2.setAutoDefault(False)
        self.up_btn_2.setFlat(False)

        self.horizontalLayout_58.addWidget(self.up_btn_2)


        self.verticalLayout_46.addWidget(self.frame_16)

        self.widget_47 = QWidget(self.frame_15)
        self.widget_47.setObjectName(u"widget_47")
        sizePolicy6.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy6)
        self.horizontalLayout_57 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(-1, 0, 0, 0)
        self.startPathImageLabel = QLabel(self.widget_47)
        self.startPathImageLabel.setObjectName(u"startPathImageLabel")
        sizePolicy6.setHeightForWidth(self.startPathImageLabel.sizePolicy().hasHeightForWidth())
        self.startPathImageLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_57.addWidget(self.startPathImageLabel)

        self.pathImageLabel = QLabel(self.widget_47)
        self.pathImageLabel.setObjectName(u"pathImageLabel")

        self.horizontalLayout_57.addWidget(self.pathImageLabel)


        self.verticalLayout_46.addWidget(self.widget_47)

        self.tabWidget_2 = QTabWidget(self.frame_15)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabsClosable(True)

        self.verticalLayout_46.addWidget(self.tabWidget_2)


        self.verticalLayout_47.addWidget(self.frame_15)

        self.customQStackedWidget.addWidget(self.disgImagePage)
        self.chartPage = QWidget()
        self.chartPage.setObjectName(u"chartPage")
        self.verticalLayout_14 = QVBoxLayout(self.chartPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_34 = QWidget(self.chartPage)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy6.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy6)
        self.horizontalLayout_42 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_12 = QLabel(self.widget_34)
        self.label_12.setObjectName(u"label_12")
        sizePolicy6.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy6)

        self.horizontalLayout_42.addWidget(self.label_12)

        self.nameLabel = QLabel(self.widget_34)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy6.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_42.addWidget(self.nameLabel)

        self.emailLabel = QLabel(self.widget_34)
        self.emailLabel.setObjectName(u"emailLabel")
        sizePolicy6.setHeightForWidth(self.emailLabel.sizePolicy().hasHeightForWidth())
        self.emailLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_42.addWidget(self.emailLabel)


        self.verticalLayout_14.addWidget(self.widget_34)

        self.staticCountWiget = QWidget(self.chartPage)
        self.staticCountWiget.setObjectName(u"staticCountWiget")
        sizePolicy5.setHeightForWidth(self.staticCountWiget.sizePolicy().hasHeightForWidth())
        self.staticCountWiget.setSizePolicy(sizePolicy5)
        self.horizontalLayout_41 = QHBoxLayout(self.staticCountWiget)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.staticCountWiget)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy5.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy5)
        self.verticalLayout_39 = QVBoxLayout(self.widget_28)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_28)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_8)

        self.attachmentsCountLabel = QLabel(self.widget_28)
        self.attachmentsCountLabel.setObjectName(u"attachmentsCountLabel")
        sizePolicy5.setHeightForWidth(self.attachmentsCountLabel.sizePolicy().hasHeightForWidth())
        self.attachmentsCountLabel.setSizePolicy(sizePolicy5)
        self.attachmentsCountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.attachmentsCountLabel)


        self.horizontalLayout_41.addWidget(self.widget_28)

        self.widget_32 = QWidget(self.staticCountWiget)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy5.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy5)
        self.verticalLayout_40 = QVBoxLayout(self.widget_32)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.countLabel = QLabel(self.widget_32)
        self.countLabel.setObjectName(u"countLabel")
        sizePolicy5.setHeightForWidth(self.countLabel.sizePolicy().hasHeightForWidth())
        self.countLabel.setSizePolicy(sizePolicy5)
        self.countLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.countLabel)

        self.recipientsCountLabel = QLabel(self.widget_32)
        self.recipientsCountLabel.setObjectName(u"recipientsCountLabel")
        sizePolicy5.setHeightForWidth(self.recipientsCountLabel.sizePolicy().hasHeightForWidth())
        self.recipientsCountLabel.setSizePolicy(sizePolicy5)
        self.recipientsCountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.recipientsCountLabel)


        self.horizontalLayout_41.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.staticCountWiget)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy5.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy5)
        self.verticalLayout_41 = QVBoxLayout(self.widget_33)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_33)
        self.label_32.setObjectName(u"label_32")
        sizePolicy5.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy5)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_32)

        self.emailCountLablel = QLabel(self.widget_33)
        self.emailCountLablel.setObjectName(u"emailCountLablel")
        sizePolicy5.setHeightForWidth(self.emailCountLablel.sizePolicy().hasHeightForWidth())
        self.emailCountLablel.setSizePolicy(sizePolicy5)
        self.emailCountLablel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.emailCountLablel)


        self.horizontalLayout_41.addWidget(self.widget_33)


        self.verticalLayout_14.addWidget(self.staticCountWiget)

        self.label_31 = QLabel(self.chartPage)
        self.label_31.setObjectName(u"label_31")
        sizePolicy6.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy6)

        self.verticalLayout_14.addWidget(self.label_31)

        self.widget_29 = QWidget(self.chartPage)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.widget_29)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy)
        self.verticalLayout_38 = QVBoxLayout(self.widget_31)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.graphWidget = QWidget(self.widget_31)
        self.graphWidget.setObjectName(u"graphWidget")
        sizePolicy1.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_40 = QHBoxLayout(self.graphWidget)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, 0, -1, -1)
        self.widget_30 = QWidget(self.graphWidget)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, -1)

        self.horizontalLayout_40.addWidget(self.widget_30)


        self.verticalLayout_38.addWidget(self.graphWidget)


        self.horizontalLayout_27.addWidget(self.widget_31)


        self.verticalLayout_14.addWidget(self.widget_29)

        self.scrollArea_4 = QScrollArea(self.chartPage)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_43 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.timeLineWiget = QWidget(self.scrollAreaWidgetContents_4)
        self.timeLineWiget.setObjectName(u"timeLineWiget")
        sizePolicy1.setHeightForWidth(self.timeLineWiget.sizePolicy().hasHeightForWidth())
        self.timeLineWiget.setSizePolicy(sizePolicy1)

        self.verticalLayout_43.addWidget(self.timeLineWiget)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_14.addWidget(self.scrollArea_4)

        self.customQStackedWidget.addWidget(self.chartPage)
        self.historyBrowserPage = QWidget()
        self.historyBrowserPage.setObjectName(u"historyBrowserPage")
        self.verticalLayout_59 = QVBoxLayout(self.historyBrowserPage)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.widget_76 = QWidget(self.historyBrowserPage)
        self.widget_76.setObjectName(u"widget_76")
        sizePolicy6.setHeightForWidth(self.widget_76.sizePolicy().hasHeightForWidth())
        self.widget_76.setSizePolicy(sizePolicy6)
        self.horizontalLayout_87 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_87.setSpacing(3)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 1, 0, 1)

        self.verticalLayout_59.addWidget(self.widget_76)

        self.widget_78 = QWidget(self.historyBrowserPage)
        self.widget_78.setObjectName(u"widget_78")
        sizePolicy2.setHeightForWidth(self.widget_78.sizePolicy().hasHeightForWidth())
        self.widget_78.setSizePolicy(sizePolicy2)
        self.horizontalLayout_89 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_89.setSpacing(3)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.domenaLineEdit = QLineEdit(self.widget_78)
        self.domenaLineEdit.setObjectName(u"domenaLineEdit")

        self.horizontalLayout_89.addWidget(self.domenaLineEdit)

        self.titleLineEdit = QLineEdit(self.widget_78)
        self.titleLineEdit.setObjectName(u"titleLineEdit")

        self.horizontalLayout_89.addWidget(self.titleLineEdit)

        self.visitCountLineEdit = QLineEdit(self.widget_78)
        self.visitCountLineEdit.setObjectName(u"visitCountLineEdit")

        self.horizontalLayout_89.addWidget(self.visitCountLineEdit)

        self.calendarBtn = QPushButton(self.widget_78)
        self.calendarBtn.setObjectName(u"calendarBtn")

        self.horizontalLayout_89.addWidget(self.calendarBtn)

        self.startDateLineEdit = QLineEdit(self.widget_78)
        self.startDateLineEdit.setObjectName(u"startDateLineEdit")
        self.startDateLineEdit.setReadOnly(True)

        self.horizontalLayout_89.addWidget(self.startDateLineEdit)

        self.endDatelineEdit = QLineEdit(self.widget_78)
        self.endDatelineEdit.setObjectName(u"endDatelineEdit")
        self.endDatelineEdit.setReadOnly(True)

        self.horizontalLayout_89.addWidget(self.endDatelineEdit)

        self.profileComboBox = QComboBox(self.widget_78)
        self.profileComboBox.setObjectName(u"profileComboBox")
        sizePolicy6.setHeightForWidth(self.profileComboBox.sizePolicy().hasHeightForWidth())
        self.profileComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_89.addWidget(self.profileComboBox)

        self.userComboBox = QComboBox(self.widget_78)
        self.userComboBox.setObjectName(u"userComboBox")
        sizePolicy6.setHeightForWidth(self.userComboBox.sizePolicy().hasHeightForWidth())
        self.userComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_89.addWidget(self.userComboBox)

        self.browserComboBox = QComboBox(self.widget_78)
        self.browserComboBox.setObjectName(u"browserComboBox")
        sizePolicy6.setHeightForWidth(self.browserComboBox.sizePolicy().hasHeightForWidth())
        self.browserComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_89.addWidget(self.browserComboBox)


        self.verticalLayout_59.addWidget(self.widget_78)

        self.label_55 = QLabel(self.historyBrowserPage)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_59.addWidget(self.label_55)

        self.widget_68 = QWidget(self.historyBrowserPage)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_80.setSpacing(3)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.historyBrowserTablet = QTableWidget(self.widget_68)
        self.historyBrowserTablet.setObjectName(u"historyBrowserTablet")

        self.horizontalLayout_80.addWidget(self.historyBrowserTablet)

        self.widget_69 = QWidget(self.widget_68)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_57 = QVBoxLayout(self.widget_69)
        self.verticalLayout_57.setSpacing(3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_9 = QScrollArea(self.widget_69)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        sizePolicy2.setHeightForWidth(self.scrollArea_9.sizePolicy().hasHeightForWidth())
        self.scrollArea_9.setSizePolicy(sizePolicy2)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 369, 180))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_58.setSpacing(3)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_61.setObjectName(u"label_61")
        sizePolicy5.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy5)
        self.label_61.setFont(font3)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_58.addWidget(self.label_61)

        self.widget_70 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_70.setObjectName(u"widget_70")
        sizePolicy6.setHeightForWidth(self.widget_70.sizePolicy().hasHeightForWidth())
        self.widget_70.setSizePolicy(sizePolicy6)
        self.horizontalLayout_81 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_81.setSpacing(6)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.widget_70)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font3)

        self.horizontalLayout_81.addWidget(self.label_49)

        self.profileNameLabel = QLabel(self.widget_70)
        self.profileNameLabel.setObjectName(u"profileNameLabel")

        self.horizontalLayout_81.addWidget(self.profileNameLabel)


        self.verticalLayout_58.addWidget(self.widget_70)

        self.widget_711 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_711.setObjectName(u"widget_711")
        sizePolicy6.setHeightForWidth(self.widget_711.sizePolicy().hasHeightForWidth())
        self.widget_711.setSizePolicy(sizePolicy6)
        self.horizontalLayout_82 = QHBoxLayout(self.widget_711)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.widget_711)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.horizontalLayout_82.addWidget(self.label_50)

        self.historyUrlLabel = QLabel(self.widget_711)
        self.historyUrlLabel.setObjectName(u"historyUrlLabel")

        self.horizontalLayout_82.addWidget(self.historyUrlLabel)


        self.verticalLayout_58.addWidget(self.widget_711)

        self.widget_72 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_72.setObjectName(u"widget_72")
        sizePolicy6.setHeightForWidth(self.widget_72.sizePolicy().hasHeightForWidth())
        self.widget_72.setSizePolicy(sizePolicy6)
        self.horizontalLayout_83 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.widget_72)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font3)

        self.horizontalLayout_83.addWidget(self.label_51)

        self.titleTabLabel = QLabel(self.widget_72)
        self.titleTabLabel.setObjectName(u"titleTabLabel")

        self.horizontalLayout_83.addWidget(self.titleTabLabel)


        self.verticalLayout_58.addWidget(self.widget_72)

        self.widget_73 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_73.setObjectName(u"widget_73")
        sizePolicy6.setHeightForWidth(self.widget_73.sizePolicy().hasHeightForWidth())
        self.widget_73.setSizePolicy(sizePolicy6)
        self.horizontalLayout_84 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.widget_73)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.horizontalLayout_84.addWidget(self.label_52)

        self.dateVisitLabel = QLabel(self.widget_73)
        self.dateVisitLabel.setObjectName(u"dateVisitLabel")

        self.horizontalLayout_84.addWidget(self.dateVisitLabel)


        self.verticalLayout_58.addWidget(self.widget_73)

        self.widget_74 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_74.setObjectName(u"widget_74")
        sizePolicy6.setHeightForWidth(self.widget_74.sizePolicy().hasHeightForWidth())
        self.widget_74.setSizePolicy(sizePolicy6)
        self.horizontalLayout_85 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.widget_74)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)

        self.horizontalLayout_85.addWidget(self.label_53)

        self.lastVisitLabel = QLabel(self.widget_74)
        self.lastVisitLabel.setObjectName(u"lastVisitLabel")

        self.horizontalLayout_85.addWidget(self.lastVisitLabel)


        self.verticalLayout_58.addWidget(self.widget_74)

        self.widget_75 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_75.setObjectName(u"widget_75")
        sizePolicy6.setHeightForWidth(self.widget_75.sizePolicy().hasHeightForWidth())
        self.widget_75.setSizePolicy(sizePolicy6)
        self.horizontalLayout_86 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.widget_75)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.horizontalLayout_86.addWidget(self.label_54)

        self.countVisit = QLabel(self.widget_75)
        self.countVisit.setObjectName(u"countVisit")

        self.horizontalLayout_86.addWidget(self.countVisit)


        self.verticalLayout_58.addWidget(self.widget_75)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_13)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_57.addWidget(self.scrollArea_9)

        self.scrollArea_13 = QScrollArea(self.widget_69)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 369, 308))
        self.verticalLayout_61 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.historyWebEngineView = QWebEngineView(self.scrollAreaWidgetContents_13)
        self.historyWebEngineView.setObjectName(u"historyWebEngineView")
        sizePolicy1.setHeightForWidth(self.historyWebEngineView.sizePolicy().hasHeightForWidth())
        self.historyWebEngineView.setSizePolicy(sizePolicy1)
        self.historyWebEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_61.addWidget(self.historyWebEngineView)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_57.addWidget(self.scrollArea_13)


        self.horizontalLayout_80.addWidget(self.widget_69)


        self.verticalLayout_59.addWidget(self.widget_68)

        self.customQStackedWidget.addWidget(self.historyBrowserPage)
        self.saveLoginPage = QWidget()
        self.saveLoginPage.setObjectName(u"saveLoginPage")
        self.verticalLayout_54 = QVBoxLayout(self.saveLoginPage)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.widget_63 = QWidget(self.saveLoginPage)
        self.widget_63.setObjectName(u"widget_63")
        sizePolicy2.setHeightForWidth(self.widget_63.sizePolicy().hasHeightForWidth())
        self.widget_63.setSizePolicy(sizePolicy2)
        self.horizontalLayout_70 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_70.setSpacing(3)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.saveLoginDomenLineEdit = QLineEdit(self.widget_63)
        self.saveLoginDomenLineEdit.setObjectName(u"saveLoginDomenLineEdit")

        self.horizontalLayout_70.addWidget(self.saveLoginDomenLineEdit)

        self.loginLineEdit = QLineEdit(self.widget_63)
        self.loginLineEdit.setObjectName(u"loginLineEdit")

        self.horizontalLayout_70.addWidget(self.loginLineEdit)

        self.saveLoginCalendarBtn = QPushButton(self.widget_63)
        self.saveLoginCalendarBtn.setObjectName(u"saveLoginCalendarBtn")

        self.horizontalLayout_70.addWidget(self.saveLoginCalendarBtn)

        self.startDataSaveLoginLineEdit = QLineEdit(self.widget_63)
        self.startDataSaveLoginLineEdit.setObjectName(u"startDataSaveLoginLineEdit")

        self.horizontalLayout_70.addWidget(self.startDataSaveLoginLineEdit)

        self.endDataSaveLoginLineEdit = QLineEdit(self.widget_63)
        self.endDataSaveLoginLineEdit.setObjectName(u"endDataSaveLoginLineEdit")

        self.horizontalLayout_70.addWidget(self.endDataSaveLoginLineEdit)

        self.saveLoginUserComboBox = QComboBox(self.widget_63)
        self.saveLoginUserComboBox.setObjectName(u"saveLoginUserComboBox")

        self.horizontalLayout_70.addWidget(self.saveLoginUserComboBox)

        self.saveLoginBrowserComboBox = QComboBox(self.widget_63)
        self.saveLoginBrowserComboBox.setObjectName(u"saveLoginBrowserComboBox")

        self.horizontalLayout_70.addWidget(self.saveLoginBrowserComboBox)

        self.saveLoginProfilComboBox = QComboBox(self.widget_63)
        self.saveLoginProfilComboBox.setObjectName(u"saveLoginProfilComboBox")

        self.horizontalLayout_70.addWidget(self.saveLoginProfilComboBox)


        self.verticalLayout_54.addWidget(self.widget_63)

        self.label_40 = QLabel(self.saveLoginPage)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_54.addWidget(self.label_40)

        self.widget_57 = QWidget(self.saveLoginPage)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_67.setSpacing(3)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.saveLoginTableWidget = QTableWidget(self.widget_57)
        self.saveLoginTableWidget.setObjectName(u"saveLoginTableWidget")

        self.horizontalLayout_67.addWidget(self.saveLoginTableWidget)

        self.widget_58 = QWidget(self.widget_57)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy1.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy1)
        self.verticalLayout_55 = QVBoxLayout(self.widget_58)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.widget_58)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 175, 110))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_47 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_47.setObjectName(u"label_47")
        sizePolicy5.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy5)
        self.label_47.setFont(font3)
        self.label_47.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.label_47)

        self.widget_60 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_60.setObjectName(u"widget_60")
        sizePolicy6.setHeightForWidth(self.widget_60.sizePolicy().hasHeightForWidth())
        self.widget_60.setSizePolicy(sizePolicy6)
        self.horizontalLayout_69 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_60)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.horizontalLayout_69.addWidget(self.label_36)

        self.saveLoginUrlLabel = QLabel(self.widget_60)
        self.saveLoginUrlLabel.setObjectName(u"saveLoginUrlLabel")

        self.horizontalLayout_69.addWidget(self.saveLoginUrlLabel)


        self.verticalLayout_60.addWidget(self.widget_60)

        self.widget_61 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_61.setObjectName(u"widget_61")
        sizePolicy6.setHeightForWidth(self.widget_61.sizePolicy().hasHeightForWidth())
        self.widget_61.setSizePolicy(sizePolicy6)
        self.horizontalLayout_68 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.lablel_44 = QLabel(self.widget_61)
        self.lablel_44.setObjectName(u"lablel_44")
        self.lablel_44.setFont(font3)

        self.horizontalLayout_68.addWidget(self.lablel_44)

        self.loginLabel = QLabel(self.widget_61)
        self.loginLabel.setObjectName(u"loginLabel")

        self.horizontalLayout_68.addWidget(self.loginLabel)


        self.verticalLayout_60.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_62.setObjectName(u"widget_62")
        sizePolicy6.setHeightForWidth(self.widget_62.sizePolicy().hasHeightForWidth())
        self.widget_62.setSizePolicy(sizePolicy6)
        self.horizontalLayout_60 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.widget_62)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.horizontalLayout_60.addWidget(self.label_45)

        self.lastDateUseLabel = QLabel(self.widget_62)
        self.lastDateUseLabel.setObjectName(u"lastDateUseLabel")

        self.horizontalLayout_60.addWidget(self.lastDateUseLabel)


        self.verticalLayout_60.addWidget(self.widget_62)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_10)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_55.addWidget(self.scrollArea_8)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_9)


        self.horizontalLayout_67.addWidget(self.widget_58)


        self.verticalLayout_54.addWidget(self.widget_57)

        self.customQStackedWidget.addWidget(self.saveLoginPage)
        self.searcherPage = QWidget()
        self.searcherPage.setObjectName(u"searcherPage")
        self.verticalLayout_62 = QVBoxLayout(self.searcherPage)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.widget_84 = QWidget(self.searcherPage)
        self.widget_84.setObjectName(u"widget_84")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_77.setSpacing(3)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.termLineEdit = QLineEdit(self.widget_84)
        self.termLineEdit.setObjectName(u"termLineEdit")

        self.horizontalLayout_77.addWidget(self.termLineEdit)

        self.sercherUrlLineEdit = QLineEdit(self.widget_84)
        self.sercherUrlLineEdit.setObjectName(u"sercherUrlLineEdit")

        self.horizontalLayout_77.addWidget(self.sercherUrlLineEdit)

        self.sercherCalendarBtn = QPushButton(self.widget_84)
        self.sercherCalendarBtn.setObjectName(u"sercherCalendarBtn")

        self.horizontalLayout_77.addWidget(self.sercherCalendarBtn)

        self.startSercharDateLineEdit = QLineEdit(self.widget_84)
        self.startSercharDateLineEdit.setObjectName(u"startSercharDateLineEdit")

        self.horizontalLayout_77.addWidget(self.startSercharDateLineEdit)

        self.endSercharDateLineEdit = QLineEdit(self.widget_84)
        self.endSercharDateLineEdit.setObjectName(u"endSercharDateLineEdit")

        self.horizontalLayout_77.addWidget(self.endSercharDateLineEdit)

        self.sercherUserComboBox = QComboBox(self.widget_84)
        self.sercherUserComboBox.setObjectName(u"sercherUserComboBox")

        self.horizontalLayout_77.addWidget(self.sercherUserComboBox)

        self.sercherBrowserComboBox = QComboBox(self.widget_84)
        self.sercherBrowserComboBox.setObjectName(u"sercherBrowserComboBox")

        self.horizontalLayout_77.addWidget(self.sercherBrowserComboBox)

        self.sercherProfilComboBox = QComboBox(self.widget_84)
        self.sercherProfilComboBox.setObjectName(u"sercherProfilComboBox")

        self.horizontalLayout_77.addWidget(self.sercherProfilComboBox)


        self.verticalLayout_62.addWidget(self.widget_84)

        self.label_38 = QLabel(self.searcherPage)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_62.addWidget(self.label_38)

        self.widget_79 = QWidget(self.searcherPage)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_71.setSpacing(3)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.sercherTableWidget = QTableWidget(self.widget_79)
        self.sercherTableWidget.setObjectName(u"sercherTableWidget")

        self.horizontalLayout_71.addWidget(self.sercherTableWidget)

        self.widget_67 = QWidget(self.widget_79)
        self.widget_67.setObjectName(u"widget_67")
        sizePolicy1.setHeightForWidth(self.widget_67.sizePolicy().hasHeightForWidth())
        self.widget_67.setSizePolicy(sizePolicy1)
        self.verticalLayout_63 = QVBoxLayout(self.widget_67)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_80 = QWidget(self.widget_67)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_64 = QVBoxLayout(self.widget_80)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.widget_80)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        sizePolicy1.setHeightForWidth(self.scrollArea_10.sizePolicy().hasHeightForWidth())
        self.scrollArea_10.setSizePolicy(sizePolicy1)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 175, 77))
        self.verticalLayout_65 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.widget_59 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_59.setObjectName(u"widget_59")
        sizePolicy2.setHeightForWidth(self.widget_59.sizePolicy().hasHeightForWidth())
        self.widget_59.setSizePolicy(sizePolicy2)
        self.verticalLayout_69 = QVBoxLayout(self.widget_59)
        self.verticalLayout_69.setSpacing(3)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_59)
        self.label_43.setObjectName(u"label_43")
        sizePolicy5.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy5)
        self.label_43.setFont(font3)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_43)

        self.widget_82 = QWidget(self.widget_59)
        self.widget_82.setObjectName(u"widget_82")
        sizePolicy6.setHeightForWidth(self.widget_82.sizePolicy().hasHeightForWidth())
        self.widget_82.setSizePolicy(sizePolicy6)
        self.horizontalLayout_73 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_82)
        self.label_48.setObjectName(u"label_48")
        sizePolicy6.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy6)
        self.label_48.setFont(font3)

        self.horizontalLayout_73.addWidget(self.label_48)

        self.termLabel = QLabel(self.widget_82)
        self.termLabel.setObjectName(u"termLabel")
        sizePolicy6.setHeightForWidth(self.termLabel.sizePolicy().hasHeightForWidth())
        self.termLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_73.addWidget(self.termLabel)


        self.verticalLayout_69.addWidget(self.widget_82)

        self.widget_81 = QWidget(self.widget_59)
        self.widget_81.setObjectName(u"widget_81")
        sizePolicy6.setHeightForWidth(self.widget_81.sizePolicy().hasHeightForWidth())
        self.widget_81.setSizePolicy(sizePolicy6)
        self.horizontalLayout_74 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.widget_81)
        self.label_62.setObjectName(u"label_62")
        sizePolicy6.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy6)
        self.label_62.setFont(font3)

        self.horizontalLayout_74.addWidget(self.label_62)

        self.sercherDateLabel = QLabel(self.widget_81)
        self.sercherDateLabel.setObjectName(u"sercherDateLabel")
        sizePolicy6.setHeightForWidth(self.sercherDateLabel.sizePolicy().hasHeightForWidth())
        self.sercherDateLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_74.addWidget(self.sercherDateLabel)


        self.verticalLayout_69.addWidget(self.widget_81)

        self.widget_83 = QWidget(self.widget_59)
        self.widget_83.setObjectName(u"widget_83")
        sizePolicy6.setHeightForWidth(self.widget_83.sizePolicy().hasHeightForWidth())
        self.widget_83.setSizePolicy(sizePolicy6)
        self.horizontalLayout_72 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_83)
        self.label_44.setObjectName(u"label_44")
        sizePolicy6.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy6)
        self.label_44.setFont(font3)

        self.horizontalLayout_72.addWidget(self.label_44)

        self.sercherUrlLabel = QLabel(self.widget_83)
        self.sercherUrlLabel.setObjectName(u"sercherUrlLabel")
        sizePolicy6.setHeightForWidth(self.sercherUrlLabel.sizePolicy().hasHeightForWidth())
        self.sercherUrlLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_72.addWidget(self.sercherUrlLabel)


        self.verticalLayout_69.addWidget(self.widget_83)


        self.verticalLayout_65.addWidget(self.widget_59)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_12)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_64.addWidget(self.scrollArea_10)


        self.verticalLayout_63.addWidget(self.widget_80)

        self.scrollArea_12 = QScrollArea(self.widget_67)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_51 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.sercherWebEngineView = QWebEngineView(self.scrollAreaWidgetContents_12)
        self.sercherWebEngineView.setObjectName(u"sercherWebEngineView")
        sizePolicy1.setHeightForWidth(self.sercherWebEngineView.sizePolicy().hasHeightForWidth())
        self.sercherWebEngineView.setSizePolicy(sizePolicy1)
        self.sercherWebEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_51.addWidget(self.sercherWebEngineView)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_63.addWidget(self.scrollArea_12)

        self.verticalLayout_63.setStretch(1, 1)

        self.horizontalLayout_71.addWidget(self.widget_67)


        self.verticalLayout_62.addWidget(self.widget_79)

        self.customQStackedWidget.addWidget(self.searcherPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_66 = QVBoxLayout(self.page_2)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.widget_91 = QWidget(self.page_2)
        self.widget_91.setObjectName(u"widget_91")
        sizePolicy5.setHeightForWidth(self.widget_91.sizePolicy().hasHeightForWidth())
        self.widget_91.setSizePolicy(sizePolicy5)
        self.horizontalLayout_94 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_94.setSpacing(3)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.autofillFieldnameLineEdit = QLineEdit(self.widget_91)
        self.autofillFieldnameLineEdit.setObjectName(u"autofillFieldnameLineEdit")

        self.horizontalLayout_94.addWidget(self.autofillFieldnameLineEdit)

        self.autofillValueLineEdit = QLineEdit(self.widget_91)
        self.autofillValueLineEdit.setObjectName(u"autofillValueLineEdit")

        self.horizontalLayout_94.addWidget(self.autofillValueLineEdit)

        self.autofillCalendarBtn = QPushButton(self.widget_91)
        self.autofillCalendarBtn.setObjectName(u"autofillCalendarBtn")

        self.horizontalLayout_94.addWidget(self.autofillCalendarBtn)

        self.autofillStartDateLineEdit = QLineEdit(self.widget_91)
        self.autofillStartDateLineEdit.setObjectName(u"autofillStartDateLineEdit")

        self.horizontalLayout_94.addWidget(self.autofillStartDateLineEdit)

        self.autofillEndDateLineEdit = QLineEdit(self.widget_91)
        self.autofillEndDateLineEdit.setObjectName(u"autofillEndDateLineEdit")

        self.horizontalLayout_94.addWidget(self.autofillEndDateLineEdit)

        self.autofillUserComboBox = QComboBox(self.widget_91)
        self.autofillUserComboBox.setObjectName(u"autofillUserComboBox")

        self.horizontalLayout_94.addWidget(self.autofillUserComboBox)

        self.autofillBrowserComboBox = QComboBox(self.widget_91)
        self.autofillBrowserComboBox.setObjectName(u"autofillBrowserComboBox")

        self.horizontalLayout_94.addWidget(self.autofillBrowserComboBox)

        self.autofillProfileComboBox = QComboBox(self.widget_91)
        self.autofillProfileComboBox.setObjectName(u"autofillProfileComboBox")

        self.horizontalLayout_94.addWidget(self.autofillProfileComboBox)


        self.verticalLayout_66.addWidget(self.widget_91)

        self.label_56 = QLabel(self.page_2)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_66.addWidget(self.label_56)

        self.widget_77 = QWidget(self.page_2)
        self.widget_77.setObjectName(u"widget_77")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_79.setSpacing(3)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.autofillTableWidget = QTableWidget(self.widget_77)
        self.autofillTableWidget.setObjectName(u"autofillTableWidget")

        self.horizontalLayout_79.addWidget(self.autofillTableWidget)

        self.widget_85 = QWidget(self.widget_77)
        self.widget_85.setObjectName(u"widget_85")
        sizePolicy1.setHeightForWidth(self.widget_85.sizePolicy().hasHeightForWidth())
        self.widget_85.setSizePolicy(sizePolicy1)
        self.verticalLayout_67 = QVBoxLayout(self.widget_85)
        self.verticalLayout_67.setSpacing(3)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11 = QScrollArea(self.widget_85)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 177, 156))
        self.verticalLayout_68 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_42 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_42)

        self.widget_86 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_86.setObjectName(u"widget_86")
        sizePolicy6.setHeightForWidth(self.widget_86.sizePolicy().hasHeightForWidth())
        self.widget_86.setSizePolicy(sizePolicy6)
        self.horizontalLayout_88 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_86)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.horizontalLayout_88.addWidget(self.label_46)

        self.autofillNameLabel = QLabel(self.widget_86)
        self.autofillNameLabel.setObjectName(u"autofillNameLabel")

        self.horizontalLayout_88.addWidget(self.autofillNameLabel)


        self.verticalLayout_68.addWidget(self.widget_86)

        self.widget_87 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_87.setObjectName(u"widget_87")
        sizePolicy6.setHeightForWidth(self.widget_87.sizePolicy().hasHeightForWidth())
        self.widget_87.setSizePolicy(sizePolicy6)
        self.horizontalLayout_90 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.widget_87)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)

        self.horizontalLayout_90.addWidget(self.label_57)

        self.autofillValueLabel = QLabel(self.widget_87)
        self.autofillValueLabel.setObjectName(u"autofillValueLabel")

        self.horizontalLayout_90.addWidget(self.autofillValueLabel)


        self.verticalLayout_68.addWidget(self.widget_87)

        self.widget_88 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_88.setObjectName(u"widget_88")
        sizePolicy6.setHeightForWidth(self.widget_88.sizePolicy().hasHeightForWidth())
        self.widget_88.setSizePolicy(sizePolicy6)
        self.horizontalLayout_91 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.widget_88)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)

        self.horizontalLayout_91.addWidget(self.label_63)

        self.autofillCreateDateLabel = QLabel(self.widget_88)
        self.autofillCreateDateLabel.setObjectName(u"autofillCreateDateLabel")

        self.horizontalLayout_91.addWidget(self.autofillCreateDateLabel)


        self.verticalLayout_68.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_89.setObjectName(u"widget_89")
        sizePolicy6.setHeightForWidth(self.widget_89.sizePolicy().hasHeightForWidth())
        self.widget_89.setSizePolicy(sizePolicy6)
        self.horizontalLayout_92 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.widget_89)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font3)

        self.horizontalLayout_92.addWidget(self.label_65)

        self.autofillLastUseDateLabel = QLabel(self.widget_89)
        self.autofillLastUseDateLabel.setObjectName(u"autofillLastUseDateLabel")

        self.horizontalLayout_92.addWidget(self.autofillLastUseDateLabel)


        self.verticalLayout_68.addWidget(self.widget_89)

        self.widget_90 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_90.setObjectName(u"widget_90")
        sizePolicy6.setHeightForWidth(self.widget_90.sizePolicy().hasHeightForWidth())
        self.widget_90.setSizePolicy(sizePolicy6)
        self.horizontalLayout_93 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.widget_90)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font3)

        self.horizontalLayout_93.addWidget(self.label_67)

        self.autofillCountUseLabel = QLabel(self.widget_90)
        self.autofillCountUseLabel.setObjectName(u"autofillCountUseLabel")

        self.horizontalLayout_93.addWidget(self.autofillCountUseLabel)


        self.verticalLayout_68.addWidget(self.widget_90)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_68.addItem(self.verticalSpacer_17)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_67.addWidget(self.scrollArea_11)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_16)


        self.horizontalLayout_79.addWidget(self.widget_85)


        self.verticalLayout_66.addWidget(self.widget_77)

        self.customQStackedWidget.addWidget(self.page_2)

        self.verticalLayout_10.addWidget(self.customQStackedWidget)


        self.horizontalLayout_11.addWidget(self.mainPagesCont)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_15 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.widget_610 = QWidget(self.rightMenu)
        self.widget_610.setObjectName(u"widget_610")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_610)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.widget_610)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.closeRightMenuBtn = QPushButton(self.widget_610)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeRightMenuBtn.setIcon(icon17)

        self.horizontalLayout_12.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_15.addWidget(self.widget_610)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_45 = QVBoxLayout(self.morePage)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_34 = QLabel(self.morePage)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_45.addWidget(self.label_34)

        self.rightMenuPages.addWidget(self.morePage)
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
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

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


        self.verticalLayout_50.addWidget(self.frame_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.emailHederDockWidget = QDockWidget(MainWindow)
        self.emailHederDockWidget.setObjectName(u"emailHederDockWidget")
        sizePolicy9.setHeightForWidth(self.emailHederDockWidget.sizePolicy().hasHeightForWidth())
        self.emailHederDockWidget.setSizePolicy(sizePolicy9)
        self.emailHederDockWidget.setMinimumSize(QSize(982, 200))
        self.emailHederDockWidget.setFloating(True)
        self.emailHederDockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable|QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.emailHederDockWidget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        sizePolicy9.setHeightForWidth(self.dockWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_8.setSizePolicy(sizePolicy9)
        self.verticalLayout_27 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_7 = QFrame(self.dockWidgetContents_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy9.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy9)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 960, 607))
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
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
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
#if QT_CONFIG(shortcut)
        self.startPathImageLabel.setBuddy(self.startPathImageLabel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.menuBtn.setDefault(False)
        self.centerMenuPages.setCurrentIndex(0)
        self.customQStackedWidget.setCurrentIndex(8)
        self.startDataBtn.setDefault(False)
        self.left_btn.setDefault(True)
        self.rigth_btn.setDefault(True)
        self.up_btn.setDefault(True)
        self.tabWidget_3.setCurrentIndex(0)
        self.left_btn_2.setDefault(True)
        self.rigth_btn_2.setDefault(True)
        self.up_btn_2.setDefault(True)
        self.tabWidget_2.setCurrentIndex(-1)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"          Home", None))
        self.meilBoxBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.eksploratorImgBtn.setText(QCoreApplication.translate("MainWindow", u"Eksplorator Dysku", None))
        self.exploratorImageBtn.setText(QCoreApplication.translate("MainWindow", u"Eksplorator obrazu", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"          Data analysis", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"          Reports", None))
        self.graphsBtn.setText(QCoreApplication.translate("MainWindow", u"          Graphs", None))
        self.pcTreeBtn.setText(QCoreApplication.translate("MainWindow", u"Urz\u0105dzenie", None))
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
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"FireNet Viewer e-mail ", None))
        self.notificationBtn.setText("")
        self.moreBtn.setText("")
        self.profileBtn.setText("")
        self.searchinp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.label_9.setText("")
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        self.minimalizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.labelNameCrudBtn.setText(QCoreApplication.translate("MainWindow", u"            Ustawienia Etykiet            ", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Skrzynka: ", None))
        self.sqlNameLabelPageLabel.setText(QCoreApplication.translate("MainWindow", u"sql_name", None))
        ___qtablewidgetitem = self.LabelTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.LabelTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tekst", None));
        ___qtablewidgetitem2 = self.LabelTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Etykieta", None));
        ___qtablewidgetitem3 = self.LabelTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Id meila", None));
        ___qtablewidgetitem4 = self.LabelTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Usuwanie", None));
        self.hederEmailBtn_2.setText(QCoreApplication.translate("MainWindow", u"Pokarz nag\u0142owek", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Nadawca:</span></p></body></html>", None))
        self.sender_2.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Odbiorca:</span></p></body></html>", None))
        self.cc_2.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Data wys\u0142ania:</span></p></body></html>", None))
        self.date_2.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Temat:</span></p></body></html>", None))
        self.subject_2.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fraza: ", None))
        self.frazeLabel.setText("")
        self.body_2.setText("")
        self.EmailtabWidget_2.setTabText(self.EmailtabWidget_2.indexOf(self.EmailtabWidgetPage1_2), QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.seachName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nadawca", None))
        self.seachSurname.setText("")
        self.seachSurname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Odbiorca", None))
        self.searchDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W temacie", None))
        self.searchBody.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W tre\u015bci", None))
#if QT_CONFIG(tooltip)
        self.startDataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zakres czasowy wiadomo\u015bci", None))
#endif // QT_CONFIG(tooltip)
        self.startDataBtn.setText("")
        self.startDataLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endDataLabel.setText("")
        self.endDataLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Do", None))
#if QT_CONFIG(tooltip)
        self.show_flags_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c wszystkie zaznaczone flagi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_flags_btn.setText("")
#if QT_CONFIG(tooltip)
        self.show_table_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Poka\u017c ca\u0142\u0105 tabel\u0119</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_table_btn.setText("")
#if QT_CONFIG(tooltip)
        self.clearBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyszy\u015b\u0107 filtry</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clearBtn.setText("")
#if QT_CONFIG(tooltip)
        self.tagPuschBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz kategorie do sortowania", None))
#endif // QT_CONFIG(tooltip)
        self.tagPuschBtn.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
#if QT_CONFIG(tooltip)
        self.export_pdf.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do PDF'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_pdf.setText("")
#if QT_CONFIG(tooltip)
        self.exportExelBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eksportuj do excel'a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exportExelBtn.setText("")
        self.detailsBtn.setText(QCoreApplication.translate("MainWindow", u"P/U", None))
        self.exportCountLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Skrzynka: ", None))
        self.sqlEmailDbName.setText(QCoreApplication.translate("MainWindow", u"Skrzynka", None))
        self.dirNameLabel.setText("")
#if QT_CONFIG(tooltip)
        self.prevEmailTableBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Strona poprzednia", None))
#endif // QT_CONFIG(tooltip)
        self.prevEmailTableBtn.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Strona : ", None))
        self.jumpToPagelineEdit.setPlaceholderText("")
        self.pageNumberLabel.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
#if QT_CONFIG(tooltip)
        self.nextEmailTableBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Strona Nast\u0119pna", None))
#endif // QT_CONFIG(tooltip)
        self.nextEmailTableBtn.setText("")
#if QT_CONFIG(tooltip)
        self.showSearchPanelBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pokarz/Ukryj belk\u0119 szukaj", None))
#endif // QT_CONFIG(tooltip)
        self.showSearchPanelBtn.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.selectedTagLabel.setText("")
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nadawca", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Odbiorca", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Temat", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data nadani", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Flagi", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None));
#if QT_CONFIG(tooltip)
        self.hederEmailBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hederEmailBtn.setText(QCoreApplication.translate("MainWindow", u"Poka\u017c nag\u0142owek", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Nadawca:</span></p></body></html>", None))
        self.sender.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Odbiorca:</span></p></body></html>", None))
        self.recipientsLabel.setText("")
        self.ccTitleLabel.setText(QCoreApplication.translate("MainWindow", u"CC:", None))
        self.ccLabel.setText("")
        self.bccTitleLabel.setText(QCoreApplication.translate("MainWindow", u"BCC:", None))
        self.bccLabel.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Data wys\u0142ania:</span></p></body></html>", None))
        self.date.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Temat:</span></p></body></html>", None))
        self.subject.setText("")
        self.body.setText("")
        self.EmailtabWidget.setTabText(self.EmailtabWidget.indexOf(self.EmailtabWidgetPage1), QCoreApplication.translate("MainWindow", u"E-mail", None))
#if QT_CONFIG(accessibility)
        self.label_7.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_7.setText("")
        self.tagiBtn.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        self.lableBtn.setText(QCoreApplication.translate("MainWindow", u"Etykiety", None))
        self.contactBtn.setText(QCoreApplication.translate("MainWindow", u"Kontakt", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a ofert\u0119", None))
        self.ofertaBtn.setText("")
        self.TutorialLabel.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.yotubeBtn.setText(QCoreApplication.translate("MainWindow", u"YT", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Odwied\u017a te\u017c", None))
        self.linkedinBtn.setText("")
        self.fbBtn.setText("")
        self.wwwBtn.setText("")
        self.left_btn.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.rigth_btn.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.up_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"Analiza danych", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.downloadDomenLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Domena", None))
        self.fileNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nazwa pliku", None))
        self.downloadHistoryCalendarBtn.setText("")
        self.startDateDownloadLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endDateDownloadLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data do", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Historia pobieranych plik\u00f3w:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SZCZWG\u00d3\u0141Y", None))
        self.urlStaticLabel.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.urlLabel.setText(QCoreApplication.translate("MainWindow", u"url", None))
        self.downloadStaticPath.setText(QCoreApplication.translate("MainWindow", u"Scie\u017cka docelowa:", None))
        self.pathDownloadLabel.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Rozmiar pliku:", None))
        self.sizeFileLabel.setText(QCoreApplication.translate("MainWindow", u"sizeFilel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Pocz\u0105tek pobierania:", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"startTime", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Koniec pobierania:", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"endTime", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"D\u0142ugo\u015b\u0107 pobierania:", None))
        self.downloadTimeLabel.setText(QCoreApplication.translate("MainWindow", u"downloadTime", None))
        self.left_btn_2.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.rigth_btn_2.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.up_btn_2.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.startPathImageLabel.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.pathImageLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"W\u0142a\u015bciciel skrzynki:", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Nazwa", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Adres Email", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Liczba za\u0142\u0105cznik\u00f3w:", None))
        self.attachmentsCountLabel.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.countLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba Odbiorc\u00f3w:", None))
        self.recipientsCountLabel.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Liczba Wiadomo\u015bci:", None))
        self.emailCountLablel.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Najcz\u0119stsze konwersacje u\u017cytkownika:", None))
        self.domenaLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Domena:", None))
        self.titleLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tytu\u0142:", None))
        self.visitCountLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ods\u0142ony:", None))
        self.calendarBtn.setText("")
        self.startDateLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endDatelineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data do", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Historia przegl\u0105danych stron internetowych", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"SZCZEG\u00d3\u0141Y", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Nazwa Profilu:", None))
        self.profileNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.historyUrlLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tytu\u0142:", None))
        self.titleTabLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Data wizyty:", None))
        self.dateVisitLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Pierwsza wizyta na stronie:", None))
        self.lastVisitLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Liczba wizyt:", None))
        self.countVisit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.saveLoginDomenLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Domena", None))
        self.loginLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.saveLoginCalendarBtn.setText("")
        self.startDataSaveLoginLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endDataSaveLoginLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data do", None))
#if QT_CONFIG(tooltip)
        self.saveLoginUserComboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Loginy zapisane w przegl\u0105darkach: ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"SZCZEG\u00d3\u0141Y", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.saveLoginUrlLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lablel_44.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ostatnie urzycie:", None))
        self.lastDateUseLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.termLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Domena:", None))
        self.sercherUrlLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fraza:", None))
        self.sercherCalendarBtn.setText("")
        self.startSercharDateLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data od", None))
        self.endSercharDateLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data do", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Historasz wyszukiwanych s\u0142\u00f3w", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"SZCZEG\u00d3\u0141Y", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Fraza:", None))
        self.termLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Data wyszukiwania:", None))
        self.sercherDateLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Url:", None))
        self.sercherUrlLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.autofillCalendarBtn.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Zapisane dane autouzupe\u0142nianie w przegl\u0105darkach", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"SZCZEG\u00d3\u0141Y", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Nazwa rekordu:", None))
        self.autofillNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107:", None))
        self.autofillValueLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Data utworzenia:", None))
        self.autofillCreateDateLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Ostatnie urzycie:", None))
        self.autofillLastUseDateLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"IIlo\u015b\u0107 urzycia:", None))
        self.autofillCountUseLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright FireNet\u00ae2025", None))
        self.emailHederDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nag\u0142\u00f3wek wiadomo\u015bci e-mail", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ID Wiadomo\u015bci: ", None))
        self.idEmailHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.headerEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Header", None))
    # retranslateUi


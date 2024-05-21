# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 666)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_onlyIcon = QWidget(self.centralwidget)
        self.widget_onlyIcon.setObjectName(u"widget_onlyIcon")
        self.widget_onlyIcon.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(102, 202, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color : white;\n"
"	height : 50px;\n"
"	border : none;\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(225, 247, 255);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_onlyIcon)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_onlyIcon)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u"0. Icon/bamos_icon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.pushButton_Dashboard_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Dashboard_ic.setObjectName(u"pushButton_Dashboard_ic")
        icon = QIcon()
        icon.addFile(u"0. Icon/dashboard_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Dashboard_ic.setIcon(icon)
        self.pushButton_Dashboard_ic.setCheckable(True)
        self.pushButton_Dashboard_ic.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_Dashboard_ic)

        self.pushButton_Training_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Training_ic.setObjectName(u"pushButton_Training_ic")
        icon1 = QIcon()
        icon1.addFile(u"0. Icon/Machine_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Training_ic.setIcon(icon1)
        self.pushButton_Training_ic.setCheckable(True)
        self.pushButton_Training_ic.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_Training_ic)

        self.pushButton_Data_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Data_ic.setObjectName(u"pushButton_Data_ic")
        icon2 = QIcon()
        icon2.addFile(u"0. Icon/database_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Data_ic.setIcon(icon2)
        self.pushButton_Data_ic.setCheckable(True)
        self.pushButton_Data_ic.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_Data_ic)

        self.pushButton_Setting_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Setting_ic.setObjectName(u"pushButton_Setting_ic")
        icon3 = QIcon()
        icon3.addFile(u"0. Icon/setting_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Setting_ic.setIcon(icon3)
        self.pushButton_Setting_ic.setCheckable(True)
        self.pushButton_Setting_ic.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_Setting_ic)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.widget_onlyIcon)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon4 = QIcon()
        icon4.addFile(u"0. Icon/exit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_9)


        self.gridLayout.addWidget(self.widget_onlyIcon, 0, 0, 1, 1)

        self.widget_NameIcon = QWidget(self.centralwidget)
        self.widget_NameIcon.setObjectName(u"widget_NameIcon")
        self.widget_NameIcon.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(102, 202, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"color : white;\n"
"text-align : left;\n"
"height : 50px;\n"
"border : none;\n"
"padding-left : 10px;\n"
"border-top-left-radius : 10px;\n"
"border-bottom-left-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(225, 247, 255);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_NameIcon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 11, -1)
        self.label_2 = QLabel(self.widget_NameIcon)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u"0. Icon/bamos_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_NameIcon)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.pushButton_Dashboard = QPushButton(self.widget_NameIcon)
        self.pushButton_Dashboard.setObjectName(u"pushButton_Dashboard")
        self.pushButton_Dashboard.setIcon(icon)
        self.pushButton_Dashboard.setCheckable(True)
        self.pushButton_Dashboard.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_Dashboard)

        self.pushButton_Training = QPushButton(self.widget_NameIcon)
        self.pushButton_Training.setObjectName(u"pushButton_Training")
        self.pushButton_Training.setIcon(icon1)
        self.pushButton_Training.setCheckable(True)
        self.pushButton_Training.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_Training)

        self.pushButton_Data = QPushButton(self.widget_NameIcon)
        self.pushButton_Data.setObjectName(u"pushButton_Data")
        self.pushButton_Data.setIcon(icon2)
        self.pushButton_Data.setCheckable(True)
        self.pushButton_Data.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_Data)

        self.pushButton_Setting = QPushButton(self.widget_NameIcon)
        self.pushButton_Setting.setObjectName(u"pushButton_Setting")
        self.pushButton_Setting.setIcon(icon3)
        self.pushButton_Setting.setCheckable(True)
        self.pushButton_Setting.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_Setting)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.widget_NameIcon)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.widget_NameIcon, 0, 1, 1, 1)

        self.widget_Content = QWidget(self.centralwidget)
        self.widget_Content.setObjectName(u"widget_Content")
        self.verticalLayout_5 = QVBoxLayout(self.widget_Content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.widget_Content)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_Menu = QPushButton(self.widget_4)
        self.pushButton_Menu.setObjectName(u"pushButton_Menu")
        self.pushButton_Menu.setStyleSheet(u"border : none;")
        icon5 = QIcon()
        icon5.addFile(u"0. Icon/menu_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Menu.setIcon(icon5)
        self.pushButton_Menu.setIconSize(QSize(30, 30))
        self.pushButton_Menu.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_Menu)

        self.horizontalSpacer = QSpacerItem(816, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_Profile = QPushButton(self.widget_4)
        self.pushButton_Profile.setObjectName(u"pushButton_Profile")
        self.pushButton_Profile.setStyleSheet(u"border : none;")
        icon6 = QIcon()
        icon6.addFile(u"0. Icon/profile_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Profile.setIcon(icon6)
        self.pushButton_Profile.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_Profile)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.widget_Content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(133, 245, 255);\n"
"")
        self.dashborad_page = QWidget()
        self.dashborad_page.setObjectName(u"dashborad_page")
        self.gridLayout_2 = QGridLayout(self.dashborad_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_12 = QWidget(self.dashborad_page)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"background-color: rgb(185, 198, 255);")
        self.gridLayout_5 = QGridLayout(self.widget_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget_3 = QStackedWidget(self.widget_12)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.gridLayout_6 = QGridLayout(self.page_21)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_5 = QWidget(self.page_21)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(170, 255, 0);")

        self.gridLayout_6.addWidget(self.widget_5, 1, 2, 1, 1)

        self.widget = QWidget(self.page_21)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.layouts_plot2 = QVBoxLayout()
        self.layouts_plot2.setObjectName(u"layouts_plot2")

        self.gridLayout_8.addLayout(self.layouts_plot2, 0, 0, 2, 2)


        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.page_21)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(170, 255, 0);")

        self.gridLayout_6.addWidget(self.widget_2, 0, 1, 1, 2)

        self.widget_chart = QWidget(self.page_21)
        self.widget_chart.setObjectName(u"widget_chart")
        self.widget_chart.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_chart)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.layouts_plot = QVBoxLayout()
        self.layouts_plot.setObjectName(u"layouts_plot")
        self.layouts_plot.setSizeConstraint(QLayout.SetNoConstraint)

        self.horizontalLayout_4.addLayout(self.layouts_plot)


        self.gridLayout_6.addWidget(self.widget_chart, 1, 0, 1, 2)

        self.stackedWidget_3.addWidget(self.page_21)
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.label_11 = QLabel(self.page_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(110, 150, 55, 16))
        self.stackedWidget_3.addWidget(self.page_25)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.label_12 = QLabel(self.page_26)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(130, 160, 55, 16))
        self.label_13 = QLabel(self.page_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 210, 55, 16))
        self.stackedWidget_3.addWidget(self.page_26)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.widget_11 = QWidget(self.page_22)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(15, 231, 384, 214))
        self.widget_11.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.widget_13 = QWidget(self.page_22)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(15, 10, 188, 214))
        self.widget_13.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 120, 55, 16))
        self.widget_14 = QWidget(self.page_22)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(406, 231, 188, 214))
        self.widget_14.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.widget_15 = QWidget(self.page_22)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(210, 10, 384, 214))
        self.widget_15.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.stackedWidget_3.addWidget(self.page_22)

        self.gridLayout_5.addWidget(self.stackedWidget_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_12, 0, 0, 3, 3)

        self.stackedWidget_2 = QStackedWidget(self.dashborad_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(200, 300))
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.stackedWidget_2.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.stackedWidget_2.addWidget(self.page_20)

        self.gridLayout_2.addWidget(self.stackedWidget_2, 2, 3, 1, 1)

        self.widget_6 = QWidget(self.dashborad_page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(185, 198, 255);")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setContentsMargins(-1, 1, 6, 1)
        self.pushButton_sales = QPushButton(self.widget_6)
        self.pushButton_sales.setObjectName(u"pushButton_sales")
        self.pushButton_sales.setStyleSheet(u"height : 60px;\n"
"border : none;\n"
"border-radius : 10px;\n"
"background-color: rgb(197, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_sales, 0, 0, 1, 1)

        self.pushButton_Inventory = QPushButton(self.widget_6)
        self.pushButton_Inventory.setObjectName(u"pushButton_Inventory")
        self.pushButton_Inventory.setStyleSheet(u"height : 60px;\n"
"border : none;\n"
"border-radius : 10px;\n"
"background-color: rgb(197, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_Inventory, 1, 1, 1, 1)

        self.pushButton_Employee = QPushButton(self.widget_6)
        self.pushButton_Employee.setObjectName(u"pushButton_Employee")
        self.pushButton_Employee.setStyleSheet(u"height : 60px;\n"
"border : none;\n"
"border-radius : 10px;\n"
"background-color: rgb(197, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_Employee, 0, 1, 1, 1)

        self.pushButton_Customer = QPushButton(self.widget_6)
        self.pushButton_Customer.setObjectName(u"pushButton_Customer")
        self.pushButton_Customer.setStyleSheet(u"height : 60px;\n"
"border : none;\n"
"border-radius : 10px;\n"
"background-color: rgb(197, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_Customer, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_6, 0, 3, 2, 1)

        self.stackedWidget.addWidget(self.dashborad_page)
        self.training_page = QWidget()
        self.training_page.setObjectName(u"training_page")
        self.gridLayout_3 = QGridLayout(self.training_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.training_page)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.training_page)
        self.data_page = QWidget()
        self.data_page.setObjectName(u"data_page")
        self.label_6 = QLabel(self.data_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 220, 241, 31))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.data_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.label_7 = QLabel(self.setting_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 220, 241, 31))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_Content, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1104, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_Menu.toggled.connect(self.widget_onlyIcon.setHidden)
        self.pushButton_Menu.toggled.connect(self.widget_NameIcon.setVisible)
        self.pushButton_Dashboard_ic.toggled.connect(self.pushButton_Dashboard.setChecked)
        self.pushButton_Training_ic.toggled.connect(self.pushButton_Training.setChecked)
        self.pushButton_Data_ic.toggled.connect(self.pushButton_Data.setChecked)
        self.pushButton_Setting_ic.toggled.connect(self.pushButton_Setting.setChecked)
        self.pushButton_Dashboard.toggled.connect(self.pushButton_Dashboard_ic.setChecked)
        self.pushButton_Training.toggled.connect(self.pushButton_Training_ic.setChecked)
        self.pushButton_Data.toggled.connect(self.pushButton_Data_ic.setChecked)
        self.pushButton_Setting.toggled.connect(self.pushButton_Setting_ic.setChecked)
        self.pushButton_9.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_Dashboard_ic.setText("")
        self.pushButton_Training_ic.setText("")
        self.pushButton_Data_ic.setText("")
        self.pushButton_Setting_ic.setText("")
        self.pushButton_9.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bamos", None))
        self.pushButton_Dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_Training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.pushButton_Data.setText(QCoreApplication.translate("MainWindow", u"0. Data", None))
        self.pushButton_Setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_Menu.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome Luan", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hope you have a good Day", None))
        self.pushButton_Profile.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"emplyee", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"emplyee", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.pushButton_sales.setText(QCoreApplication.translate("MainWindow", u"sales", None))
        self.pushButton_Inventory.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.pushButton_Employee.setText(QCoreApplication.translate("MainWindow", u"employee", None))
        self.pushButton_Customer.setText(QCoreApplication.translate("MainWindow", u"customer", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Training Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0. Data Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Setting Page", None))
    # retranslateUi


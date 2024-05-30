# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1204, 930)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.actionConnect_to_Database = QAction(MainWindow)
        self.actionConnect_to_Database.setObjectName(u"actionConnect_to_Database")
        self.actionImport_CSV = QAction(MainWindow)
        self.actionImport_CSV.setObjectName(u"actionImport_CSV")
        self.actionExport_CSV = QAction(MainWindow)
        self.actionExport_CSV.setObjectName(u"actionExport_CSV")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_NameIcon = QWidget(self.centralwidget)
        self.widget_NameIcon.setObjectName(u"widget_NameIcon")
        self.widget_NameIcon.setStyleSheet(u"#widget_NameIcon{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(234, 234, 234);\n"
"height : 50px;\n"
"width : 50px;\n"
"border : none;\n"
"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"padding-left : -40px;\n"
"	font: 87 8pt \"Lato Black\";\n"
"}\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_NameIcon)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 11, -1)
        self.label_Bamos_ic_2 = QLabel(self.widget_NameIcon)
        self.label_Bamos_ic_2.setObjectName(u"label_Bamos_ic_2")
        self.label_Bamos_ic_2.setMinimumSize(QSize(35, 35))
        self.label_Bamos_ic_2.setMaximumSize(QSize(50, 50))
        self.label_Bamos_ic_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")
        self.label_Bamos_ic_2.setPixmap(QPixmap(u"Icon/coffee-cup_ic.png"))
        self.label_Bamos_ic_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_Bamos_ic_2)

        self.label_Bamos = QLabel(self.widget_NameIcon)
        self.label_Bamos.setObjectName(u"label_Bamos")
        font = QFont()
        font.setFamilies([u"Lato"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_Bamos.setFont(font)
        self.label_Bamos.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(239, 239, 239);")

        self.horizontalLayout_3.addWidget(self.label_Bamos)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 14, -1, -1)
        self.pushButton_Data = QPushButton(self.widget_NameIcon)
        self.pushButton_Data.setObjectName(u"pushButton_Data")
        self.pushButton_Data.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(170, 85, 0);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"Icon/database_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Data.setIcon(icon)
        self.pushButton_Data.setCheckable(True)
        self.pushButton_Data.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.pushButton_Data)

        self.widget_Dashboard_func = QWidget(self.widget_NameIcon)
        self.widget_Dashboard_func.setObjectName(u"widget_Dashboard_func")
        self.widget_Dashboard_func.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.gridLayout_8 = QGridLayout(self.widget_Dashboard_func)
        self.gridLayout_8.setSpacing(9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 15, 0, 0)
        self.widget_sale_cus_Inv = QWidget(self.widget_Dashboard_func)
        self.widget_sale_cus_Inv.setObjectName(u"widget_sale_cus_Inv")
        self.widget_sale_cus_Inv.setStyleSheet(u"QPushButton{\n"
"padding-left : 20px;\n"
"border : none;\n"
"	font: 87 8pt \"Lato Black\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(170, 85, 0);\n"
"}\n"
"")
        self.gridLayout_9 = QGridLayout(self.widget_sale_cus_Inv)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(9)
        self.gridLayout_9.setVerticalSpacing(11)
        self.gridLayout_9.setContentsMargins(16, 0, 15, 0)
        self.widget_icon_in_dashboard = QWidget(self.widget_sale_cus_Inv)
        self.widget_icon_in_dashboard.setObjectName(u"widget_icon_in_dashboard")
        self.widget_icon_in_dashboard.setStyleSheet(u"font: 7pt \"Lato\";")
        self.verticalLayout_2 = QVBoxLayout(self.widget_icon_in_dashboard)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.pushButton_Sales = QPushButton(self.widget_icon_in_dashboard)
        self.pushButton_Sales.setObjectName(u"pushButton_Sales")
        font1 = QFont()
        font1.setFamilies([u"Lato"])
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_Sales.setFont(font1)
        self.pushButton_Sales.setStyleSheet(u"")
        self.pushButton_Sales.setCheckable(True)
        self.pushButton_Sales.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.pushButton_Sales, 0, Qt.AlignLeft)

        self.pushButton_Customer = QPushButton(self.widget_icon_in_dashboard)
        self.pushButton_Customer.setObjectName(u"pushButton_Customer")
        self.pushButton_Customer.setStyleSheet(u"")
        self.pushButton_Customer.setCheckable(True)
        self.pushButton_Customer.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.pushButton_Customer, 0, Qt.AlignLeft)

        self.pushButton_Inventory = QPushButton(self.widget_icon_in_dashboard)
        self.pushButton_Inventory.setObjectName(u"pushButton_Inventory")
        self.pushButton_Inventory.setStyleSheet(u"")
        self.pushButton_Inventory.setCheckable(True)
        self.pushButton_Inventory.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.pushButton_Inventory, 0, Qt.AlignLeft)


        self.gridLayout_9.addWidget(self.widget_icon_in_dashboard, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_sale_cus_Inv, 2, 0, 1, 1)

        self.pushButton_Dashboard = QPushButton(self.widget_Dashboard_func)
        self.pushButton_Dashboard.setObjectName(u"pushButton_Dashboard")
        self.pushButton_Dashboard.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(170, 85, 0);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding-left : -12px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Icon/dashboard_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Dashboard.setIcon(icon1)
        self.pushButton_Dashboard.setCheckable(True)
        self.pushButton_Dashboard.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.pushButton_Dashboard, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_Dashboard_func)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 13, -1, -1)
        self.pushButton_Training = QPushButton(self.widget_NameIcon)
        self.pushButton_Training.setObjectName(u"pushButton_Training")
        self.pushButton_Training.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"background-color: rgb(170, 85, 0);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Icon/training_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Training.setIcon(icon2)
        self.pushButton_Training.setIconSize(QSize(25, 25))
        self.pushButton_Training.setCheckable(True)
        self.pushButton_Training.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_Training)

        self.pushButton_Setting = QPushButton(self.widget_NameIcon)
        self.pushButton_Setting.setObjectName(u"pushButton_Setting")
        self.pushButton_Setting.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(170, 85, 0);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}\n"
"	\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Icon/setting_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Setting.setIcon(icon3)
        self.pushButton_Setting.setCheckable(True)
        self.pushButton_Setting.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_Setting)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(120, 76, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.pushButton_Logut = QPushButton(self.widget_NameIcon)
        self.pushButton_Logut.setObjectName(u"pushButton_Logut")
        font2 = QFont()
        font2.setFamilies([u"Lato Black"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_Logut.setFont(font2)
        self.pushButton_Logut.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	color: rgb(47, 68, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Icon/logout_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Logut.setIcon(icon4)
        self.pushButton_Logut.setCheckable(True)
        self.pushButton_Logut.setAutoExclusive(True)

        self.gridLayout_5.addWidget(self.pushButton_Logut, 3, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_NameIcon, 0, 1, 2, 1)

        self.widget_onlyIcon = QWidget(self.centralwidget)
        self.widget_onlyIcon.setObjectName(u"widget_onlyIcon")
        self.widget_onlyIcon.setStyleSheet(u"#widget_onlyIcon{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color : white;\n"
"height : 50px;\n"
"width : 50px;\n"
"border : none;\n"
"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 0);;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(170, 85, 0);\n"
"	color: rgb(58, 58, 58);\n"
"	font-weight : bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_onlyIcon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_bamos_icon = QHBoxLayout()
        self.horizontalLayout_bamos_icon.setObjectName(u"horizontalLayout_bamos_icon")
        self.label_bamos_icon_1 = QLabel(self.widget_onlyIcon)
        self.label_bamos_icon_1.setObjectName(u"label_bamos_icon_1")
        self.label_bamos_icon_1.setMinimumSize(QSize(50, 50))
        self.label_bamos_icon_1.setMaximumSize(QSize(50, 50))
        self.label_bamos_icon_1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")
        self.label_bamos_icon_1.setPixmap(QPixmap(u"Icon/coffee-cup_ic.png"))
        self.label_bamos_icon_1.setScaledContents(True)

        self.horizontalLayout_bamos_icon.addWidget(self.label_bamos_icon_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_bamos_icon)

        self.verticalLayout_onlyicon_func = QVBoxLayout()
        self.verticalLayout_onlyicon_func.setSpacing(20)
        self.verticalLayout_onlyicon_func.setObjectName(u"verticalLayout_onlyicon_func")
        self.verticalLayout_onlyicon_func.setContentsMargins(-1, 15, -1, -1)
        self.pushButton_Data_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Data_ic.setObjectName(u"pushButton_Data_ic")
        self.pushButton_Data_ic.setIcon(icon)
        self.pushButton_Data_ic.setCheckable(True)
        self.pushButton_Data_ic.setAutoExclusive(True)

        self.verticalLayout_onlyicon_func.addWidget(self.pushButton_Data_ic)

        self.pushButton_Dashboard_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Dashboard_ic.setObjectName(u"pushButton_Dashboard_ic")
        self.pushButton_Dashboard_ic.setIcon(icon1)
        self.pushButton_Dashboard_ic.setCheckable(True)
        self.pushButton_Dashboard_ic.setAutoExclusive(True)

        self.verticalLayout_onlyicon_func.addWidget(self.pushButton_Dashboard_ic)

        self.pushButton_Training_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Training_ic.setObjectName(u"pushButton_Training_ic")
        self.pushButton_Training_ic.setIcon(icon2)
        self.pushButton_Training_ic.setCheckable(True)
        self.pushButton_Training_ic.setAutoExclusive(True)

        self.verticalLayout_onlyicon_func.addWidget(self.pushButton_Training_ic)

        self.pushButton_Setting_ic = QPushButton(self.widget_onlyIcon)
        self.pushButton_Setting_ic.setObjectName(u"pushButton_Setting_ic")
        self.pushButton_Setting_ic.setIcon(icon3)
        self.pushButton_Setting_ic.setCheckable(True)
        self.pushButton_Setting_ic.setAutoExclusive(True)

        self.verticalLayout_onlyicon_func.addWidget(self.pushButton_Setting_ic)


        self.verticalLayout_4.addLayout(self.verticalLayout_onlyicon_func)

        self.verticalSpacer = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.widget_onlyIcon)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_9)


        self.gridLayout_7.addWidget(self.widget_onlyIcon, 0, 0, 2, 1)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"border-color: rgb(171, 255, 202);")
        self.gridLayout_10 = QGridLayout(self.widget_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(129, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setFamilies([u"Lato Black"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 83);")

        self.gridLayout_10.addWidget(self.label_10, 0, 2, 1, 1)

        self.pushButton_Menu_2 = QPushButton(self.widget_5)
        self.pushButton_Menu_2.setObjectName(u"pushButton_Menu_2")
        self.pushButton_Menu_2.setStyleSheet(u"border : none;")
        icon5 = QIcon()
        icon5.addFile(u"Icon/slidebar-left_ic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Menu_2.setIcon(icon5)
        self.pushButton_Menu_2.setIconSize(QSize(30, 30))
        self.pushButton_Menu_2.setCheckable(True)

        self.gridLayout_10.addWidget(self.pushButton_Menu_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(129, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.pushButton_Profile_2 = QPushButton(self.widget_5)
        self.pushButton_Profile_2.setObjectName(u"pushButton_Profile_2")
        self.pushButton_Profile_2.setStyleSheet(u"border : none;")
        icon6 = QIcon()
        icon6.addFile(u"Icon/ic_profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Profile_2.setIcon(icon6)
        self.pushButton_Profile_2.setIconSize(QSize(40, 40))

        self.gridLayout_10.addWidget(self.pushButton_Profile_2, 0, 5, 1, 1)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setFamilies([u"PoetsenOne"])
        font4.setBold(False)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(31, 31, 31);")

        self.gridLayout_10.addWidget(self.label_8, 0, 4, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#stackWidget{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.stackedWidgetData = QWidget()
        self.stackedWidgetData.setObjectName(u"stackedWidgetData")
        self.stackedWidgetData.setStyleSheet(u"font: 10pt \"Lato\";\n"
"color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(self.stackedWidgetData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.stackedWidgetData)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 87 10pt \"Lato Black\";")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.stackedWidgetData)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255,0.85);\n"
"border-radius : 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButtonConnectDatabase = QPushButton(self.stackedWidgetData)
        self.pushButtonConnectDatabase.setObjectName(u"pushButtonConnectDatabase")
        self.pushButtonConnectDatabase.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height: 40px;")

        self.horizontalLayout.addWidget(self.pushButtonConnectDatabase)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_choosetable = QHBoxLayout()
        self.horizontalLayout_choosetable.setObjectName(u"horizontalLayout_choosetable")
        self.label_2 = QLabel(self.stackedWidgetData)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 87 10pt \"Lato Black\";")

        self.horizontalLayout_choosetable.addWidget(self.label_2)

        self.comboBoxChooseTable = QComboBox(self.stackedWidgetData)
        self.comboBoxChooseTable.setObjectName(u"comboBoxChooseTable")
        self.comboBoxChooseTable.setStyleSheet(u"background-color: rgba(255, 255, 255,0.85);\n"
"border-radius : 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_choosetable.addWidget(self.comboBoxChooseTable)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_choosetable)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.stackedWidgetData)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 87 10pt \"Lato Black\";")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEditquery = QLineEdit(self.stackedWidgetData)
        self.lineEditquery.setObjectName(u"lineEditquery")
        self.lineEditquery.setStyleSheet(u"background-color: rgba(255, 255, 255,0.85);\n"
"border-radius : 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.lineEditquery)

        self.pushButtonExecuteQuerry = QPushButton(self.stackedWidgetData)
        self.pushButtonExecuteQuerry.setObjectName(u"pushButtonExecuteQuerry")
        self.pushButtonExecuteQuerry.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 40px;")

        self.horizontalLayout_8.addWidget(self.pushButtonExecuteQuerry)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableViewShow = QTableView(self.stackedWidgetData)
        self.tableViewShow.setObjectName(u"tableViewShow")
        self.tableViewShow.setStyleSheet(u"background-color: rgba(255, 255, 255,0.85);\n"
"border-radius : 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.tableViewShow)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.pushButtonFetchMore = QPushButton(self.stackedWidgetData)
        self.pushButtonFetchMore.setObjectName(u"pushButtonFetchMore")
        self.pushButtonFetchMore.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 30px;")

        self.gridLayout.addWidget(self.pushButtonFetchMore, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetData)
        self.stackedWidgetSales = QWidget()
        self.stackedWidgetSales.setObjectName(u"stackedWidgetSales")
        self.gridLayout_41 = QGridLayout(self.stackedWidgetSales)
        self.gridLayout_41.setSpacing(15)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.widget_16 = QWidget(self.stackedWidgetSales)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 10px;")
        self.gridLayout_26 = QGridLayout(self.widget_16)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitleMRR = QLabel(self.widget_16)
        self.labelTitleMRR.setObjectName(u"labelTitleMRR")
        self.labelTitleMRR.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.labelTitleMRR, 0, Qt.AlignHCenter)

        self.labelMRR = QLabel(self.widget_16)
        self.labelMRR.setObjectName(u"labelMRR")

        self.verticalLayout.addWidget(self.labelMRR)


        self.gridLayout_26.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_16, 0, 0, 1, 1)

        self.widget_17 = QWidget(self.stackedWidgetSales)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 10px;")
        self.gridLayout_40 = QGridLayout(self.widget_17)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelTitleNumberofSales = QLabel(self.widget_17)
        self.labelTitleNumberofSales.setObjectName(u"labelTitleNumberofSales")
        self.labelTitleNumberofSales.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.labelTitleNumberofSales, 0, Qt.AlignHCenter)

        self.labelNumberofSales = QLabel(self.widget_17)
        self.labelNumberofSales.setObjectName(u"labelNumberofSales")

        self.verticalLayout_6.addWidget(self.labelNumberofSales)


        self.gridLayout_40.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_17, 0, 1, 1, 1)

        self.widget_drinkherewego = QWidget(self.stackedWidgetSales)
        self.widget_drinkherewego.setObjectName(u"widget_drinkherewego")
        self.widget_drinkherewego.setStyleSheet(u"#widget_drinkherewego{background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.gridLayout_14 = QGridLayout(self.widget_drinkherewego)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayoutDrinkHereOrGo = QVBoxLayout()
        self.verticalLayoutDrinkHereOrGo.setObjectName(u"verticalLayoutDrinkHereOrGo")

        self.gridLayout_14.addLayout(self.verticalLayoutDrinkHereOrGo, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_drinkherewego, 0, 2, 2, 1)

        self.widget_salesbydate = QWidget(self.stackedWidgetSales)
        self.widget_salesbydate.setObjectName(u"widget_salesbydate")
        self.widget_salesbydate.setStyleSheet(u"#widget_salesbydate{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.gridLayout_12 = QGridLayout(self.widget_salesbydate)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayoutTotalSalesbyDates = QVBoxLayout()
        self.verticalLayoutTotalSalesbyDates.setSpacing(7)
        self.verticalLayoutTotalSalesbyDates.setObjectName(u"verticalLayoutTotalSalesbyDates")
        self.verticalLayoutTotalSalesbyDates.setContentsMargins(-1, -1, 0, -1)

        self.gridLayout_12.addLayout(self.verticalLayoutTotalSalesbyDates, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_salesbydate, 1, 0, 2, 2)

        self.widget_ratebyweek = QWidget(self.stackedWidgetSales)
        self.widget_ratebyweek.setObjectName(u"widget_ratebyweek")
        self.widget_ratebyweek.setStyleSheet(u"#widget_ratebyweek{background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.gridLayout_16 = QGridLayout(self.widget_ratebyweek)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayoutSalesGrowthRatebyWeek = QVBoxLayout()
        self.verticalLayoutSalesGrowthRatebyWeek.setObjectName(u"verticalLayoutSalesGrowthRatebyWeek")

        self.gridLayout_16.addLayout(self.verticalLayoutSalesGrowthRatebyWeek, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_ratebyweek, 2, 2, 1, 1)

        self.widget_Partoftheday = QWidget(self.stackedWidgetSales)
        self.widget_Partoftheday.setObjectName(u"widget_Partoftheday")
        self.widget_Partoftheday.setStyleSheet(u"#widget_Partoftheday{background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.gridLayout_13 = QGridLayout(self.widget_Partoftheday)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayoutSalesGrowthRateByPartOfTheDays = QVBoxLayout()
        self.verticalLayoutSalesGrowthRateByPartOfTheDays.setObjectName(u"verticalLayoutSalesGrowthRateByPartOfTheDays")

        self.gridLayout_13.addLayout(self.verticalLayoutSalesGrowthRateByPartOfTheDays, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_Partoftheday, 3, 0, 1, 2)

        self.widget_whichstore = QWidget(self.stackedWidgetSales)
        self.widget_whichstore.setObjectName(u"widget_whichstore")
        self.widget_whichstore.setStyleSheet(u"#widget_whichstore{background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.gridLayout_17 = QGridLayout(self.widget_whichstore)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayoutFromWhichStore = QVBoxLayout()
        self.verticalLayoutFromWhichStore.setObjectName(u"verticalLayoutFromWhichStore")

        self.gridLayout_17.addLayout(self.verticalLayoutFromWhichStore, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.widget_whichstore, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetSales)
        self.stackWidgetCustomer = QWidget()
        self.stackWidgetCustomer.setObjectName(u"stackWidgetCustomer")
        self.widget_PurchasebyGenderr = QWidget(self.stackWidgetCustomer)
        self.widget_PurchasebyGenderr.setObjectName(u"widget_PurchasebyGenderr")
        self.widget_PurchasebyGenderr.setGeometry(QRect(11, 149, 311, 371))
        self.widget_PurchasebyGenderr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_18 = QGridLayout(self.widget_PurchasebyGenderr)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayoutPurchasebyGender = QVBoxLayout()
        self.verticalLayoutPurchasebyGender.setObjectName(u"verticalLayoutPurchasebyGender")

        self.gridLayout_18.addLayout(self.verticalLayoutPurchasebyGender, 0, 0, 1, 1)

        self.widget_PurchasebyGender = QWidget(self.stackWidgetCustomer)
        self.widget_PurchasebyGender.setObjectName(u"widget_PurchasebyGender")
        self.widget_PurchasebyGender.setGeometry(QRect(632, 11, 301, 511))
        self.widget_PurchasebyGender.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_21 = QGridLayout(self.widget_PurchasebyGender)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalLayoutPurchasebyGenderandbyProductCategory = QVBoxLayout()
        self.verticalLayoutPurchasebyGenderandbyProductCategory.setObjectName(u"verticalLayoutPurchasebyGenderandbyProductCategory")

        self.gridLayout_21.addLayout(self.verticalLayoutPurchasebyGenderandbyProductCategory, 0, 0, 1, 1)

        self.widget_PurchasebyAgeGroup = QWidget(self.stackWidgetCustomer)
        self.widget_PurchasebyAgeGroup.setObjectName(u"widget_PurchasebyAgeGroup")
        self.widget_PurchasebyAgeGroup.setGeometry(QRect(330, 150, 291, 371))
        self.widget_PurchasebyAgeGroup.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_19 = QGridLayout(self.widget_PurchasebyAgeGroup)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayoutPurchasebyAgeGroup = QVBoxLayout()
        self.verticalLayoutPurchasebyAgeGroup.setObjectName(u"verticalLayoutPurchasebyAgeGroup")

        self.gridLayout_19.addLayout(self.verticalLayoutPurchasebyAgeGroup, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.stackWidgetCustomer)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(11, 526, 941, 251))
        self.gridLayout_34 = QGridLayout(self.widget_9)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.widget_LayoutRFM = QWidget(self.widget_9)
        self.widget_LayoutRFM.setObjectName(u"widget_LayoutRFM")
        self.widget_LayoutRFM.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_20 = QGridLayout(self.widget_LayoutRFM)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayoutRFM = QVBoxLayout()
        self.verticalLayoutRFM.setObjectName(u"verticalLayoutRFM")

        self.gridLayout_20.addLayout(self.verticalLayoutRFM, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_LayoutRFM, 0, 0, 1, 1)

        self.widget_12 = QWidget(self.stackWidgetCustomer)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(11, 11, 271, 131))
        self.widget_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_35 = QGridLayout(self.widget_12)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.labelTitleNewCustomer = QLabel(self.widget_12)
        self.labelTitleNewCustomer.setObjectName(u"labelTitleNewCustomer")
        self.labelTitleNewCustomer.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.labelTitleNewCustomer, 0, Qt.AlignHCenter)

        self.labelNewCustomer = QLabel(self.widget_12)
        self.labelNewCustomer.setObjectName(u"labelNewCustomer")

        self.verticalLayout_7.addWidget(self.labelNewCustomer, 0, Qt.AlignHCenter)


        self.gridLayout_35.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.widget_13 = QWidget(self.stackWidgetCustomer)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(322, 11, 271, 131))
        self.widget_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_36 = QGridLayout(self.widget_13)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelTitleChurnRate = QLabel(self.widget_13)
        self.labelTitleChurnRate.setObjectName(u"labelTitleChurnRate")
        self.labelTitleChurnRate.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.labelTitleChurnRate, 0, Qt.AlignHCenter)

        self.labelChurnRate = QLabel(self.widget_13)
        self.labelChurnRate.setObjectName(u"labelChurnRate")

        self.verticalLayout_8.addWidget(self.labelChurnRate, 0, Qt.AlignHCenter)


        self.gridLayout_36.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackWidgetCustomer)
        self.stackWidgetInventory = QWidget()
        self.stackWidgetInventory.setObjectName(u"stackWidgetInventory")
        self.gridLayout_39 = QGridLayout(self.stackWidgetInventory)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.widget_14 = QWidget(self.stackWidgetInventory)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_28 = QGridLayout(self.widget_14)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelTitleTotalPurchase = QLabel(self.widget_14)
        self.labelTitleTotalPurchase.setObjectName(u"labelTitleTotalPurchase")
        self.labelTitleTotalPurchase.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.labelTitleTotalPurchase, 0, Qt.AlignHCenter)

        self.labelTotalPurchase = QLabel(self.widget_14)
        self.labelTotalPurchase.setObjectName(u"labelTotalPurchase")

        self.verticalLayout_9.addWidget(self.labelTotalPurchase, 0, Qt.AlignHCenter)


        self.gridLayout_28.addLayout(self.verticalLayout_9, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.stackWidgetInventory)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_38 = QGridLayout(self.widget_15)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelTitleTotalSale = QLabel(self.widget_15)
        self.labelTitleTotalSale.setObjectName(u"labelTitleTotalSale")
        self.labelTitleTotalSale.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.labelTitleTotalSale, 0, Qt.AlignHCenter)

        self.labelTotalSale = QLabel(self.widget_15)
        self.labelTotalSale.setObjectName(u"labelTotalSale")

        self.verticalLayout_10.addWidget(self.labelTotalSale, 0, Qt.AlignHCenter)


        self.gridLayout_38.addLayout(self.verticalLayout_10, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_15, 0, 1, 1, 1)

        self.widget_11 = QWidget(self.stackWidgetInventory)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_25 = QGridLayout(self.widget_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.verticalLayoutSaleTarget = QVBoxLayout()
        self.verticalLayoutSaleTarget.setObjectName(u"verticalLayoutSaleTarget")

        self.gridLayout_25.addLayout(self.verticalLayoutSaleTarget, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_11, 0, 2, 3, 1)

        self.widget_3 = QWidget(self.stackWidgetInventory)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_22 = QGridLayout(self.widget_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.verticalLayoutQuantitySold = QVBoxLayout()
        self.verticalLayoutQuantitySold.setObjectName(u"verticalLayoutQuantitySold")

        self.gridLayout_22.addLayout(self.verticalLayoutQuantitySold, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_3, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.stackWidgetInventory)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_23 = QGridLayout(self.widget_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalLayoutPercentWaste = QVBoxLayout()
        self.verticalLayoutPercentWaste.setObjectName(u"verticalLayoutPercentWaste")

        self.gridLayout_23.addLayout(self.verticalLayoutPercentWaste, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_8, 1, 1, 1, 1)

        self.widget_10 = QWidget(self.stackWidgetInventory)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;")
        self.gridLayout_24 = QGridLayout(self.widget_10)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalLayoutTotalInventorySoldByDay = QVBoxLayout()
        self.verticalLayoutTotalInventorySoldByDay.setObjectName(u"verticalLayoutTotalInventorySoldByDay")

        self.gridLayout_24.addLayout(self.verticalLayoutTotalInventorySoldByDay, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_10, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.stackWidgetInventory)
        self.stackedWidgetTraining = QWidget()
        self.stackedWidgetTraining.setObjectName(u"stackedWidgetTraining")
        self.stackedWidgetTraining.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_33 = QGridLayout(self.stackedWidgetTraining)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_TitlePredict = QLabel(self.stackedWidgetTraining)
        self.label_TitlePredict.setObjectName(u"label_TitlePredict")

        self.gridLayout_33.addWidget(self.label_TitlePredict, 0, 0, 1, 1)

        self.gridLayout_TrainingRateAndModelName = QGridLayout()
        self.gridLayout_TrainingRateAndModelName.setObjectName(u"gridLayout_TrainingRateAndModelName")
        self.label_SetModelName = QLabel(self.stackedWidgetTraining)
        self.label_SetModelName.setObjectName(u"label_SetModelName")

        self.gridLayout_TrainingRateAndModelName.addWidget(self.label_SetModelName, 1, 1, 1, 1)

        self.lineEdit_SetModelName = QLineEdit(self.stackedWidgetTraining)
        self.lineEdit_SetModelName.setObjectName(u"lineEdit_SetModelName")
        self.lineEdit_SetModelName.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_TrainingRateAndModelName.addWidget(self.lineEdit_SetModelName, 1, 2, 1, 1)

        self.label_TrainingRate = QLabel(self.stackedWidgetTraining)
        self.label_TrainingRate.setObjectName(u"label_TrainingRate")

        self.gridLayout_TrainingRateAndModelName.addWidget(self.label_TrainingRate, 0, 1, 1, 1)

        self.label_Percentage = QLabel(self.stackedWidgetTraining)
        self.label_Percentage.setObjectName(u"label_Percentage")

        self.gridLayout_TrainingRateAndModelName.addWidget(self.label_Percentage, 0, 3, 1, 1)

        self.lineEdit_TrainingRate = QLineEdit(self.stackedWidgetTraining)
        self.lineEdit_TrainingRate.setObjectName(u"lineEdit_TrainingRate")
        self.lineEdit_TrainingRate.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_TrainingRateAndModelName.addWidget(self.lineEdit_TrainingRate, 0, 2, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_TrainingRateAndModelName, 1, 1, 1, 1)

        self.horizontalLayout_LoadModel = QHBoxLayout()
        self.horizontalLayout_LoadModel.setObjectName(u"horizontalLayout_LoadModel")
        self.label_ModelName = QLabel(self.stackedWidgetTraining)
        self.label_ModelName.setObjectName(u"label_ModelName")

        self.horizontalLayout_LoadModel.addWidget(self.label_ModelName)

        self.lineEdit_ModelName = QLineEdit(self.stackedWidgetTraining)
        self.lineEdit_ModelName.setObjectName(u"lineEdit_ModelName")
        self.lineEdit_ModelName.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.horizontalLayout_LoadModel.addWidget(self.lineEdit_ModelName)

        self.pushButton_LoadModel = QPushButton(self.stackedWidgetTraining)
        self.pushButton_LoadModel.setObjectName(u"pushButton_LoadModel")
        self.pushButton_LoadModel.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 40px;")

        self.horizontalLayout_LoadModel.addWidget(self.pushButton_LoadModel)


        self.gridLayout_33.addLayout(self.horizontalLayout_LoadModel, 4, 0, 1, 1)

        self.pushButton_TrainSaveModel = QPushButton(self.stackedWidgetTraining)
        self.pushButton_TrainSaveModel.setObjectName(u"pushButton_TrainSaveModel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_TrainSaveModel.sizePolicy().hasHeightForWidth())
        self.pushButton_TrainSaveModel.setSizePolicy(sizePolicy1)
        self.pushButton_TrainSaveModel.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 40px;")

        self.gridLayout_33.addWidget(self.pushButton_TrainSaveModel, 2, 1, 1, 1)

        self.groupBoxCoefficient = QGroupBox(self.stackedWidgetTraining)
        self.groupBoxCoefficient.setObjectName(u"groupBoxCoefficient")
        self.gridLayout_27 = QGridLayout(self.groupBoxCoefficient)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_Metric = QGridLayout()
        self.gridLayout_Metric.setObjectName(u"gridLayout_Metric")
        self.label_RMSE = QLabel(self.groupBoxCoefficient)
        self.label_RMSE.setObjectName(u"label_RMSE")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_RMSE.sizePolicy().hasHeightForWidth())
        self.label_RMSE.setSizePolicy(sizePolicy2)

        self.gridLayout_Metric.addWidget(self.label_RMSE, 2, 0, 1, 1)

        self.label_MAE = QLabel(self.groupBoxCoefficient)
        self.label_MAE.setObjectName(u"label_MAE")

        self.gridLayout_Metric.addWidget(self.label_MAE, 0, 0, 1, 1)

        self.label_MSE = QLabel(self.groupBoxCoefficient)
        self.label_MSE.setObjectName(u"label_MSE")

        self.gridLayout_Metric.addWidget(self.label_MSE, 1, 0, 1, 1)

        self.lineEdit_RMSE = QLineEdit(self.groupBoxCoefficient)
        self.lineEdit_RMSE.setObjectName(u"lineEdit_RMSE")
        self.lineEdit_RMSE.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_Metric.addWidget(self.lineEdit_RMSE, 2, 1, 1, 2)

        self.lineEdit_MSE = QLineEdit(self.groupBoxCoefficient)
        self.lineEdit_MSE.setObjectName(u"lineEdit_MSE")
        self.lineEdit_MSE.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_Metric.addWidget(self.lineEdit_MSE, 1, 1, 1, 2)

        self.lineEdit_MAE = QLineEdit(self.groupBoxCoefficient)
        self.lineEdit_MAE.setObjectName(u"lineEdit_MAE")
        self.lineEdit_MAE.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_Metric.addWidget(self.lineEdit_MAE, 0, 1, 1, 2)


        self.gridLayout_27.addLayout(self.gridLayout_Metric, 1, 0, 1, 1)

        self.tableView_Coefficient = QTableView(self.groupBoxCoefficient)
        self.tableView_Coefficient.setObjectName(u"tableView_Coefficient")
        self.tableView_Coefficient.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_27.addWidget(self.tableView_Coefficient, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.groupBoxCoefficient, 3, 1, 1, 1)

        self.groupBox_UseDefaultModel = QGroupBox(self.stackedWidgetTraining)
        self.groupBox_UseDefaultModel.setObjectName(u"groupBox_UseDefaultModel")
        font5 = QFont()
        font5.setFamilies([u"Lato Black"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.groupBox_UseDefaultModel.setFont(font5)
        self.gridLayout_31 = QGridLayout(self.groupBox_UseDefaultModel)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBoxInput = QGroupBox(self.groupBox_UseDefaultModel)
        self.groupBoxInput.setObjectName(u"groupBoxInput")
        font6 = QFont()
        font6.setFamilies([u"Lato Black"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.groupBoxInput.setFont(font6)
        self.groupBoxInput.setStyleSheet(u"")
        self.gridLayout_29 = QGridLayout(self.groupBoxInput)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_StaffAndSalesOutlet_2 = QGridLayout()
        self.gridLayout_StaffAndSalesOutlet_2.setObjectName(u"gridLayout_StaffAndSalesOutlet_2")
        self.label_SalesOutlet = QLabel(self.groupBoxInput)
        self.label_SalesOutlet.setObjectName(u"label_SalesOutlet")

        self.gridLayout_StaffAndSalesOutlet_2.addWidget(self.label_SalesOutlet, 1, 0, 1, 1)

        self.label_Staff = QLabel(self.groupBoxInput)
        self.label_Staff.setObjectName(u"label_Staff")

        self.gridLayout_StaffAndSalesOutlet_2.addWidget(self.label_Staff, 0, 0, 1, 1)

        self.comboBox_SalesOutletID = QComboBox(self.groupBoxInput)
        self.comboBox_SalesOutletID.addItem("")
        self.comboBox_SalesOutletID.addItem("")
        self.comboBox_SalesOutletID.addItem("")
        self.comboBox_SalesOutletID.setObjectName(u"comboBox_SalesOutletID")
        self.comboBox_SalesOutletID.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 20px;")

        self.gridLayout_StaffAndSalesOutlet_2.addWidget(self.comboBox_SalesOutletID, 1, 1, 1, 1)

        self.lineEdit_Staff = QLineEdit(self.groupBoxInput)
        self.lineEdit_Staff.setObjectName(u"lineEdit_Staff")
        self.lineEdit_Staff.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 20px;")

        self.gridLayout_StaffAndSalesOutlet_2.addWidget(self.lineEdit_Staff, 0, 1, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_StaffAndSalesOutlet_2, 0, 0, 1, 1)

        self.pushButton_Predict = QPushButton(self.groupBoxInput)
        self.pushButton_Predict.setObjectName(u"pushButton_Predict")
        self.pushButton_Predict.setStyleSheet(u"font: 87 8pt \"Lato Black\";\n"
"border-radius : 5px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 40px;")

        self.gridLayout_29.addWidget(self.pushButton_Predict, 0, 1, 1, 1)

        self.gridLayout_ProductFeatures = QGridLayout()
        self.gridLayout_ProductFeatures.setObjectName(u"gridLayout_ProductFeatures")
        self.lineEdit_ProductCategory = QLineEdit(self.groupBoxInput)
        self.lineEdit_ProductCategory.setObjectName(u"lineEdit_ProductCategory")
        self.lineEdit_ProductCategory.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 20px;")

        self.gridLayout_ProductFeatures.addWidget(self.lineEdit_ProductCategory, 1, 1, 1, 2)

        self.label_ProductId = QLabel(self.groupBoxInput)
        self.label_ProductId.setObjectName(u"label_ProductId")

        self.gridLayout_ProductFeatures.addWidget(self.label_ProductId, 0, 0, 1, 1)

        self.lineEdit_ProductId = QLineEdit(self.groupBoxInput)
        self.lineEdit_ProductId.setObjectName(u"lineEdit_ProductId")
        self.lineEdit_ProductId.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 20px;")

        self.gridLayout_ProductFeatures.addWidget(self.lineEdit_ProductId, 0, 1, 1, 2)

        self.label_ProductCategory = QLabel(self.groupBoxInput)
        self.label_ProductCategory.setObjectName(u"label_ProductCategory")

        self.gridLayout_ProductFeatures.addWidget(self.label_ProductCategory, 1, 0, 1, 1)

        self.lineEdit_Price = QLineEdit(self.groupBoxInput)
        self.lineEdit_Price.setObjectName(u"lineEdit_Price")
        self.lineEdit_Price.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 20px;")

        self.gridLayout_ProductFeatures.addWidget(self.lineEdit_Price, 2, 1, 2, 2)

        self.label_Price = QLabel(self.groupBoxInput)
        self.label_Price.setObjectName(u"label_Price")
        sizePolicy2.setHeightForWidth(self.label_Price.sizePolicy().hasHeightForWidth())
        self.label_Price.setSizePolicy(sizePolicy2)

        self.gridLayout_ProductFeatures.addWidget(self.label_Price, 2, 0, 2, 1)

        self.checkBox_NewProduct = QCheckBox(self.groupBoxInput)
        self.checkBox_NewProduct.setObjectName(u"checkBox_NewProduct")

        self.gridLayout_ProductFeatures.addWidget(self.checkBox_NewProduct, 1, 3, 1, 1)

        self.checkBox_TaxExempt = QCheckBox(self.groupBoxInput)
        self.checkBox_TaxExempt.setObjectName(u"checkBox_TaxExempt")

        self.gridLayout_ProductFeatures.addWidget(self.checkBox_TaxExempt, 2, 3, 1, 1)

        self.checkBox_Promotion = QCheckBox(self.groupBoxInput)
        self.checkBox_Promotion.setObjectName(u"checkBox_Promotion")

        self.gridLayout_ProductFeatures.addWidget(self.checkBox_Promotion, 0, 3, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_ProductFeatures, 1, 0, 1, 2)

        self.pushButton_Clear = QPushButton(self.groupBoxInput)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy3)
        self.pushButton_Clear.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 40px;")

        self.gridLayout_29.addWidget(self.pushButton_Clear, 2, 0, 1, 2)


        self.gridLayout_31.addWidget(self.groupBoxInput, 0, 0, 1, 1)

        self.groupBoxOutput = QGroupBox(self.groupBox_UseDefaultModel)
        self.groupBoxOutput.setObjectName(u"groupBoxOutput")
        self.groupBoxOutput.setFont(font6)
        self.groupBoxOutput.setStyleSheet(u"")
        self.gridLayout_30 = QGridLayout(self.groupBoxOutput)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalLayout_QuantityWillBeSold = QHBoxLayout()
        self.horizontalLayout_QuantityWillBeSold.setObjectName(u"horizontalLayout_QuantityWillBeSold")
        self.label_QuantityWillBeSold = QLabel(self.groupBoxOutput)
        self.label_QuantityWillBeSold.setObjectName(u"label_QuantityWillBeSold")

        self.horizontalLayout_QuantityWillBeSold.addWidget(self.label_QuantityWillBeSold)

        self.lineEdit_QuantityWillBeSold = QLineEdit(self.groupBoxOutput)
        self.lineEdit_QuantityWillBeSold.setObjectName(u"lineEdit_QuantityWillBeSold")
        self.lineEdit_QuantityWillBeSold.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.horizontalLayout_QuantityWillBeSold.addWidget(self.lineEdit_QuantityWillBeSold)


        self.gridLayout_30.addLayout(self.horizontalLayout_QuantityWillBeSold, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBoxOutput, 0, 1, 1, 1)


        self.gridLayout_33.addWidget(self.groupBox_UseDefaultModel, 5, 0, 1, 2)

        self.groupBox_DataToTrain = QGroupBox(self.stackedWidgetTraining)
        self.groupBox_DataToTrain.setObjectName(u"groupBox_DataToTrain")
        font7 = QFont()
        font7.setFamilies([u"Lato Black"])
        font7.setBold(True)
        self.groupBox_DataToTrain.setFont(font7)
        self.groupBox_DataToTrain.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")
        self.gridLayout_32 = QGridLayout(self.groupBox_DataToTrain)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_DataToTrain = QGridLayout()
        self.gridLayout_DataToTrain.setObjectName(u"gridLayout_DataToTrain")
        self.checkBox_train_new_product_yn = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_new_product_yn.setObjectName(u"checkBox_train_new_product_yn")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_new_product_yn, 0, 2, 1, 1)

        self.checkBox_train_sales_outlet_id = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_sales_outlet_id.setObjectName(u"checkBox_train_sales_outlet_id")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_sales_outlet_id, 0, 3, 1, 1)

        self.checkBox_train_current_retail_price = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_current_retail_price.setObjectName(u"checkBox_train_current_retail_price")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_current_retail_price, 0, 1, 1, 1)

        self.checkBox_train_promo_yn = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_promo_yn.setObjectName(u"checkBox_train_promo_yn")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_promo_yn, 1, 1, 1, 1)

        self.checkBox_train_product_id = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_product_id.setObjectName(u"checkBox_train_product_id")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_product_id, 0, 0, 1, 1)

        self.checkBox_train_product_category = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_product_category.setObjectName(u"checkBox_train_product_category")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_product_category, 1, 0, 1, 1)

        self.checkBox_train_tax_exempt_yn = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_tax_exempt_yn.setObjectName(u"checkBox_train_tax_exempt_yn")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_tax_exempt_yn, 1, 2, 1, 1)

        self.checkBox_train_staff_id = QCheckBox(self.groupBox_DataToTrain)
        self.checkBox_train_staff_id.setObjectName(u"checkBox_train_staff_id")

        self.gridLayout_DataToTrain.addWidget(self.checkBox_train_staff_id, 1, 3, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_DataToTrain, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.groupBox_DataToTrain, 1, 0, 1, 1)

        self.widget_ML_Chart = QWidget(self.stackedWidgetTraining)
        self.widget_ML_Chart.setObjectName(u"widget_ML_Chart")
        self.widget_ML_Chart.setStyleSheet(u"#widget_ML_Chart{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(45, 45, 45);\n"
"border-radius : 10px;\n"
"}")
        self.gridLayout_15 = QGridLayout(self.widget_ML_Chart)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_ChartActualVsPredicted = QVBoxLayout()
        self.verticalLayout_ChartActualVsPredicted.setObjectName(u"verticalLayout_ChartActualVsPredicted")

        self.gridLayout_15.addLayout(self.verticalLayout_ChartActualVsPredicted, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.widget_ML_Chart, 2, 0, 2, 1)

        self.stackedWidget.addWidget(self.stackedWidgetTraining)
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName(u"stackedWidgetPage4")
        self.gridLayout_2 = QGridLayout(self.stackedWidgetPage4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.stackedWidgetPage4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_11 = QGridLayout(self.widget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        font8 = QFont()
        font8.setFamilies([u"Lato"])
        font8.setPointSize(8)
        font8.setBold(False)
        font8.setItalic(False)
        self.widget_2.setFont(font8)
        self.widget_2.setStyleSheet(u"font: 8pt \"Lato\";\n"
"color: rgb(47, 47, 47);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius : 20px;")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(7)
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 27)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 87 12pt \"Lato Black\";")

        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_6.addWidget(self.label_27)

        self.lineEdit_8 = QLineEdit(self.widget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.horizontalLayout_6.addWidget(self.lineEdit_8)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_7.addWidget(self.label_28)

        self.lineEdit_9 = QLineEdit(self.widget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.horizontalLayout_7.addWidget(self.lineEdit_9)


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.widget_2, 4, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(132)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.pushButtonCreate = QPushButton(self.widget)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")
        self.pushButtonCreate.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 50px;")

        self.horizontalLayout_4.addWidget(self.pushButtonCreate)

        self.pushButtonUpdate = QPushButton(self.widget)
        self.pushButtonUpdate.setObjectName(u"pushButtonUpdate")
        self.pushButtonUpdate.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 50px;")

        self.horizontalLayout_4.addWidget(self.pushButtonUpdate)

        self.pushButtonDelete = QPushButton(self.widget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 10px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 50px;")

        self.horizontalLayout_4.addWidget(self.pushButtonDelete)


        self.gridLayout_11.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)

        self.pushButtonSearch = QPushButton(self.widget)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setStyleSheet(u"font: 87 10pt \"Lato Black\";\n"
"border-radius : 5px;\n"
"background-color: rgb(191, 95, 0);\n"
"height : 30px;")

        self.gridLayout_11.addWidget(self.pushButtonSearch, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 8pt \"Lato\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_29)

        self.lineEdit_10 = QLineEdit(self.widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"\n"
"font: 8pt \"Lato\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.horizontalLayout_5.addWidget(self.lineEdit_10)


        self.gridLayout_11.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0);\n"
"border-radius : 20px;")
        self.gridLayout_3 = QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.widget1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.widget1)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 3, 1, 1)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_20 = QLabel(self.widget1)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 3, 1, 1)

        self.label_18 = QLabel(self.widget1)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_21 = QLabel(self.widget1)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 3, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_7, 3, 3, 1, 1)

        self.label_26 = QLabel(self.widget1)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 4, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy4)
        self.lineEdit_11.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255,0.7);\n"
"border-radius : 5px;\n"
"height : 30px;")

        self.gridLayout_3.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 87 12pt \"Lato Black\";")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 2)


        self.gridLayout_11.addWidget(self.widget1, 2, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage4)

        self.gridLayout_7.addWidget(self.stackedWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1204, 26))
        self.menuSystems = QMenu(self.menubar)
        self.menuSystems.setObjectName(u"menuSystems")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSystems.menuAction())
        self.menuSystems.addAction(self.actionConnect_to_Database)
        self.menuSystems.addAction(self.actionExport_CSV)

        self.retranslateUi(MainWindow)
        self.pushButton_Dashboard.toggled.connect(self.widget_sale_cus_Inv.hide)
        self.pushButton_Dashboard.toggled.connect(self.widget_sale_cus_Inv.setHidden)
        self.pushButton_Menu_2.toggled.connect(self.widget_NameIcon.setHidden)
        self.pushButton_Menu_2.toggled.connect(self.widget_onlyIcon.setVisible)
        self.pushButton_Logut.toggled.connect(MainWindow.close)
        self.pushButton_9.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect_to_Database.setText(QCoreApplication.translate("MainWindow", u"Connect to Database", None))
        self.actionImport_CSV.setText(QCoreApplication.translate("MainWindow", u"Import CSV", None))
        self.actionExport_CSV.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.label_Bamos_ic_2.setText("")
        self.label_Bamos.setText(QCoreApplication.translate("MainWindow", u"Bamos", None))
        self.pushButton_Data.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButton_Sales.setText(QCoreApplication.translate("MainWindow", u"  Sales  ", None))
        self.pushButton_Customer.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.pushButton_Inventory.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.pushButton_Dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_Training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.pushButton_Setting.setText(QCoreApplication.translate("MainWindow", u"  Setting", None))
        self.pushButton_Logut.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_bamos_icon_1.setText("")
        self.pushButton_Data_ic.setText("")
        self.pushButton_Dashboard_ic.setText("")
        self.pushButton_Training_ic.setText("")
        self.pushButton_Setting_ic.setText("")
        self.pushButton_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u" Bamos Coffee Management", None))
        self.pushButton_Menu_2.setText("")
        self.pushButton_Profile_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nguy\u1ec5n  Th\u00e0nh Lu\u00e2n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Connect Database              ", None))
        self.pushButtonConnectDatabase.setText(QCoreApplication.translate("MainWindow", u" Connect Database ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Choose Table                           ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Write your querry here:", None))
        self.pushButtonExecuteQuerry.setText(QCoreApplication.translate("MainWindow", u"  Execute Querry  ", None))
        self.pushButtonFetchMore.setText(QCoreApplication.translate("MainWindow", u"Fetch More ...", None))
        self.labelTitleMRR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MRR</span></p></body></html>", None))
        self.labelMRR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MRR</span></p></body></html>", None))
        self.labelTitleNumberofSales.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SALES</span></p></body></html>", None))
        self.labelNumberofSales.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SALES</span></p></body></html>", None))
        self.labelTitleNewCustomer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">New Customer</span></p></body></html>", None))
        self.labelNewCustomer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">New Customer</span></p></body></html>", None))
        self.labelTitleChurnRate.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Churn Rate</span></p></body></html>", None))
        self.labelChurnRate.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Churn Rate</span></p></body></html>", None))
        self.labelTitleTotalPurchase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TOTAL PURCHASE</span></p></body></html>", None))
        self.labelTotalPurchase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TOTAL PURCHASE</span></p></body></html>", None))
        self.labelTitleTotalSale.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TOTAL SALE</span></p></body></html>", None))
        self.labelTotalSale.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TOTAL SALE</span></p></body></html>", None))
        self.label_TitlePredict.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#aa5500;\">Predict Employee Sales Ability</span></p></body></html>", None))
        self.label_SetModelName.setText(QCoreApplication.translate("MainWindow", u"Set Model Name:", None))
        self.label_TrainingRate.setText(QCoreApplication.translate("MainWindow", u"Training Rate:    ", None))
        self.label_Percentage.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_ModelName.setText(QCoreApplication.translate("MainWindow", u"Model Name", None))
        self.pushButton_LoadModel.setText(QCoreApplication.translate("MainWindow", u"  Load Mode  ", None))
        self.pushButton_TrainSaveModel.setText(QCoreApplication.translate("MainWindow", u"Train and Save Model", None))
        self.groupBoxCoefficient.setTitle(QCoreApplication.translate("MainWindow", u"Coefficient", None))
        self.label_RMSE.setText(QCoreApplication.translate("MainWindow", u"RMSE:", None))
        self.label_MAE.setText(QCoreApplication.translate("MainWindow", u"MAE:", None))
        self.label_MSE.setText(QCoreApplication.translate("MainWindow", u"MSE:", None))
        self.groupBox_UseDefaultModel.setTitle(QCoreApplication.translate("MainWindow", u"Use Default Model", None))
        self.groupBoxInput.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_SalesOutlet.setText(QCoreApplication.translate("MainWindow", u"Sales Outlet:", None))
        self.label_Staff.setText(QCoreApplication.translate("MainWindow", u"Staff ID:                       ", None))
        self.comboBox_SalesOutletID.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_SalesOutletID.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_SalesOutletID.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))

        self.pushButton_Predict.setText(QCoreApplication.translate("MainWindow", u"  Predict  ", None))
        self.label_ProductId.setText(QCoreApplication.translate("MainWindow", u"Product ID:", None))
        self.label_ProductCategory.setText(QCoreApplication.translate("MainWindow", u"Product Category:", None))
        self.label_Price.setText(QCoreApplication.translate("MainWindow", u"Current Retail Price      :", None))
        self.checkBox_NewProduct.setText(QCoreApplication.translate("MainWindow", u"New Product", None))
        self.checkBox_TaxExempt.setText(QCoreApplication.translate("MainWindow", u"Tax Exempt", None))
        self.checkBox_Promotion.setText(QCoreApplication.translate("MainWindow", u"Promotion", None))
        self.pushButton_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBoxOutput.setTitle(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.label_QuantityWillBeSold.setText(QCoreApplication.translate("MainWindow", u"Quantity will be sold:   ", None))
        self.groupBox_DataToTrain.setTitle(QCoreApplication.translate("MainWindow", u"Data to Train:", None))
        self.checkBox_train_new_product_yn.setText(QCoreApplication.translate("MainWindow", u"new_product_yn", None))
        self.checkBox_train_sales_outlet_id.setText(QCoreApplication.translate("MainWindow", u"sales_outlet_id", None))
        self.checkBox_train_current_retail_price.setText(QCoreApplication.translate("MainWindow", u"current_retail_price", None))
        self.checkBox_train_promo_yn.setText(QCoreApplication.translate("MainWindow", u"promo_yn", None))
        self.checkBox_train_product_id.setText(QCoreApplication.translate("MainWindow", u"product_id", None))
        self.checkBox_train_product_category.setText(QCoreApplication.translate("MainWindow", u"product_category", None))
        self.checkBox_train_tax_exempt_yn.setText(QCoreApplication.translate("MainWindow", u"tax_exempt_yn", None))
        self.checkBox_train_staff_id.setText(QCoreApplication.translate("MainWindow", u"staff_id", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Account Information", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"User name:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButtonSearch.setText(QCoreApplication.translate("MainWindow", u"   Search  ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ID staffs:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Gmail:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Starts Day", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Positions:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Location:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.menuSystems.setTitle(QCoreApplication.translate("MainWindow", u"Systems", None))
    # retranslateUi


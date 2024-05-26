# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabaseConnections.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 340)
        icon = QIcon()
        icon.addFile(u"../0. Icon/ic_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 341, 271))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 321, 241))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelServer = QLabel(self.gridLayoutWidget)
        self.labelServer.setObjectName(u"labelServer")

        self.gridLayout.addWidget(self.labelServer, 0, 0, 1, 1)

        self.pushButtonConnect = QPushButton(self.gridLayoutWidget)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        icon1 = QIcon()
        icon1.addFile(u"../0. Icon/ic_connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonConnect.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButtonConnect, 5, 1, 1, 1)

        self.labelPort = QLabel(self.gridLayoutWidget)
        self.labelPort.setObjectName(u"labelPort")

        self.gridLayout.addWidget(self.labelPort, 1, 0, 1, 1)

        self.labelDatabase = QLabel(self.gridLayoutWidget)
        self.labelDatabase.setObjectName(u"labelDatabase")

        self.gridLayout.addWidget(self.labelDatabase, 2, 0, 1, 1)

        self.labelUser = QLabel(self.gridLayoutWidget)
        self.labelUser.setObjectName(u"labelUser")

        self.gridLayout.addWidget(self.labelUser, 3, 0, 1, 1)

        self.labelPassword = QLabel(self.gridLayoutWidget)
        self.labelPassword.setObjectName(u"labelPassword")

        self.gridLayout.addWidget(self.labelPassword, 4, 0, 1, 1)

        self.pushButtonExit = QPushButton(self.gridLayoutWidget)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        icon2 = QIcon()
        icon2.addFile(u"../0. Icon/ic_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonExit.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButtonExit, 5, 2, 1, 1)

        self.lineEditPassword = QLineEdit(self.gridLayoutWidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditPassword.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEditPassword, 4, 1, 1, 2)

        self.lineEditUser = QLineEdit(self.gridLayoutWidget)
        self.lineEditUser.setObjectName(u"lineEditUser")

        self.gridLayout.addWidget(self.lineEditUser, 3, 1, 1, 2)

        self.lineEditDatabase = QLineEdit(self.gridLayoutWidget)
        self.lineEditDatabase.setObjectName(u"lineEditDatabase")

        self.gridLayout.addWidget(self.lineEditDatabase, 2, 1, 1, 2)

        self.lineEditPort = QLineEdit(self.gridLayoutWidget)
        self.lineEditPort.setObjectName(u"lineEditPort")

        self.gridLayout.addWidget(self.lineEditPort, 1, 1, 1, 2)

        self.lineEditSever = QLineEdit(self.gridLayoutWidget)
        self.lineEditSever.setObjectName(u"lineEditSever")
        self.lineEditSever.setAutoFillBackground(False)
        self.lineEditSever.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditSever, 0, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 377, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BMS", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Connections Settings:", None))
        self.labelServer.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labelPort.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.labelDatabase.setText(QCoreApplication.translate("MainWindow", u"Database:", None))
        self.labelUser.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lineEditPassword.setText(QCoreApplication.translate("MainWindow", u"luannt_1005", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your password here...", None))
        self.lineEditUser.setText(QCoreApplication.translate("MainWindow", u"root", None))
        self.lineEditUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your user name here...", None))
        self.lineEditDatabase.setText(QCoreApplication.translate("MainWindow", u"final_project", None))
        self.lineEditDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your database name here...", None))
        self.lineEditPort.setText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.lineEditPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your port here...", None))
        self.lineEditSever.setText(QCoreApplication.translate("MainWindow", u"localhost", u"DJDSJKDSJKDS"))
        self.lineEditSever.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter your server here...", None))
    # retranslateUi


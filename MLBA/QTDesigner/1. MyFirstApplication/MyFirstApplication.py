# Form implementation generated from reading ui file 'MyFirstApplication.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 796)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.myTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.myTitle.setGeometry(QtCore.QRect(70, 10, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myTitle.setFont(font)
        self.myTitle.setObjectName("myTitle")
        self.clickMe = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clickMe.setGeometry(QtCore.QRect(110, 150, 171, 41))
        self.clickMe.setObjectName("clickMe")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clickMe.clicked.connect(self.myTitle.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.myTitle.setText(_translate("MainWindow", "https://tranduythanh.com/"))
        self.clickMe.setText(_translate("MainWindow", "Click Me To Clear Title"))
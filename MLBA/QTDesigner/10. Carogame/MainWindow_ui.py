# Form implementation generated from reading ui file 'd:\study\university\nam3\ki2\machinelearning\K214160990\Carogame\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 766)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditRows = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditRows.setObjectName("lineEditRows")
        self.horizontalLayout.addWidget(self.lineEditRows)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditColumn = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditColumn.setObjectName("lineEditColumn")
        self.horizontalLayout.addWidget(self.lineEditColumn)
        self.pushButtonDrawCaro = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDrawCaro.setObjectName("pushButtonDrawCaro")
        self.horizontalLayout.addWidget(self.pushButtonDrawCaro)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 914, 652))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayoutCaro = QtWidgets.QGridLayout()
        self.gridLayoutCaro.setSpacing(0)
        self.gridLayoutCaro.setObjectName("gridLayoutCaro")
        self.verticalLayout_3.addLayout(self.gridLayoutCaro)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tran Duy Thanh"))
        self.label.setText(_translate("MainWindow", "Number Of Rows:"))
        self.lineEditRows.setText(_translate("MainWindow", "50"))
        self.label_2.setText(_translate("MainWindow", "Number Of Columns:"))
        self.lineEditColumn.setText(_translate("MainWindow", "50"))
        self.pushButtonDrawCaro.setText(_translate("MainWindow", "Draw Caro"))

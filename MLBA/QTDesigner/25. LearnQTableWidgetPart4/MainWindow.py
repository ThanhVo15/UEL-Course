# Form implementation generated from reading ui file 'D:\Đại học\Năm 3\Kì 2\Học máy trong phân tích kinh doanh\Thực hành code\PyQt6\LearnQTableWidgetPart4\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 591, 161))
        self.groupBox.setStyleSheet("BACKGROUND-COLOR: #FAFAD2")
        self.groupBox.setObjectName("groupBox")
        self.tableWidgetProduct = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidgetProduct.setGeometry(QtCore.QRect(10, 20, 571, 131))
        self.tableWidgetProduct.setObjectName("tableWidgetProduct")
        self.tableWidgetProduct.setColumnCount(0)
        self.tableWidgetProduct.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 591, 151))
        self.groupBox_2.setStyleSheet("BACKGROUND-COLOR: #C6E2FF\n"
"    ")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEditProductCode = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditProductCode.setGeometry(QtCore.QRect(100, 30, 481, 20))
        self.lineEditProductCode.setObjectName("lineEditProductCode")
        self.lineEditProductName = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditProductName.setGeometry(QtCore.QRect(100, 70, 481, 20))
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.lineEditUnitPrice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditUnitPrice.setGeometry(QtCore.QRect(100, 110, 481, 20))
        self.lineEditUnitPrice.setObjectName("lineEditUnitPrice")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 390, 591, 81))
        self.groupBox_3.setStyleSheet("BACKGROUND-COLOR: #FAF0E6")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonNew = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonNew.setGeometry(QtCore.QRect(50, 20, 101, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Đại học\\Năm 3\\Kì 2\\Học máy trong phân tích kinh doanh\\Thực hành code\\PyQt6\\LearnQTableWidgetPart4\\images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNew.setIcon(icon)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSave.setGeometry(QtCore.QRect(260, 20, 101, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Đại học\\Năm 3\\Kì 2\\Học máy trong phân tích kinh doanh\\Thực hành code\\PyQt6\\LearnQTableWidgetPart4\\images/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave.setIcon(icon1)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonRemove.setGeometry(QtCore.QRect(460, 20, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\Đại học\\Năm 3\\Kì 2\\Học máy trong phân tích kinh doanh\\Thực hành code\\PyQt6\\LearnQTableWidgetPart4\\images/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRemove.setIcon(icon2)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 591, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "List Products:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Product Detail:"))
        self.label.setText(_translate("MainWindow", "Product Code:"))
        self.label_2.setText(_translate("MainWindow", "Product Name:"))
        self.label_3.setText(_translate("MainWindow", "Unit Price:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Action"))
        self.pushButtonNew.setText(_translate("MainWindow", "New"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Product - SQLite</span></p></body></html>"))
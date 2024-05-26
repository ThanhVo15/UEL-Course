# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import testqrc_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(808, 632)
        Form.setStyleSheet(u"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 681, 571))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color:rgba(85, 98, 112, 255);\n"
"	color:rgba(255, 255, 255, 200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(255, 107, 107, 255);\n"
"	background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color:rgba(255, 107, 107, 255);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-image: url(:/newPrefix/Login_screen.png);\n"
"border-top-left-radius : 30px;\n"
"border-bottom-left-radius : 30px")

        self.verticalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stackedWidget_Login = QStackedWidget(self.widget)
        self.stackedWidget_Login.setObjectName(u"stackedWidget_Login")
        self.stackedWidget_Login.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget_Login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius : 30px;\n"
"border-bottom-right-radius : 30px")
        self.stackedWidgetSignIn = QWidget()
        self.stackedWidgetSignIn.setObjectName(u"stackedWidgetSignIn")
        self.stackedWidgetSignIn.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);")
        self.label_3 = QLabel(self.stackedWidgetSignIn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 60, 161, 41))
        font = QFont()
        font.setFamilies([u"Lato Black"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEditUsername = QLineEdit(self.stackedWidgetSignIn)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setGeometry(QRect(20, 160, 251, 31))
        font1 = QFont()
        font1.setPointSize(9)
        self.lineEditUsername.setFont(font1)
        self.lineEditUsername.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditPass = QLineEdit(self.stackedWidgetSignIn)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setGeometry(QRect(20, 230, 251, 31))
        self.lineEditPass.setFont(font1)
        self.lineEditPass.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditPass.setEchoMode(QLineEdit.Password)
        self.pushButtonSignInBig = QPushButton(self.stackedWidgetSignIn)
        self.pushButtonSignInBig.setObjectName(u"pushButtonSignInBig")
        self.pushButtonSignInBig.setGeometry(QRect(20, 310, 251, 41))
        font2 = QFont()
        font2.setFamilies([u"Lato Black"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButtonSignInBig.setFont(font2)
        self.pushButtonSignInBig.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(170, 149, 132);\n"
"	border-radius : 5px; \n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     /* M\u00e0u n\u1ec1n khi di chu\u1ed9t qua */\n"
"	background-color: rgb(170, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     /* M\u00e0u n\u1ec1n khi n\u00fat \u0111\u01b0\u1ee3c nh\u1ea5n */\n"
"	background-color: rgb(170, 149, 132);\n"
"}")
        self.layoutWidget = QWidget(self.stackedWidgetSignIn)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(51, 401, 193, 18))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Lato"])
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")

        self.horizontalLayout.addWidget(self.label_4)

        self.pushButtonSignUpSmall = QPushButton(self.layoutWidget)
        self.pushButtonSignUpSmall.setObjectName(u"pushButtonSignUpSmall")
        font4 = QFont()
        font4.setFamilies([u"Lato"])
        font4.setPointSize(8)
        font4.setBold(True)
        self.pushButtonSignUpSmall.setFont(font4)
        self.pushButtonSignUpSmall.setStyleSheet(u"color: rgb(170, 72, 2);")

        self.horizontalLayout.addWidget(self.pushButtonSignUpSmall)

        self.stackedWidget_Login.addWidget(self.stackedWidgetSignIn)
        self.stackedWidgetSignUp = QWidget()
        self.stackedWidgetSignUp.setObjectName(u"stackedWidgetSignUp")
        self.lineEditNewUsername = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditNewUsername.setObjectName(u"lineEditNewUsername")
        self.lineEditNewUsername.setGeometry(QRect(20, 270, 251, 31))
        self.lineEditNewUsername.setFont(font1)
        self.lineEditNewUsername.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditNewPass = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditNewPass.setObjectName(u"lineEditNewPass")
        self.lineEditNewPass.setGeometry(QRect(20, 320, 251, 31))
        self.lineEditNewPass.setFont(font1)
        self.lineEditNewPass.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditNewPass.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.stackedWidgetSignUp)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 10, 211, 41))
        font5 = QFont()
        font5.setFamilies([u"Lato Black"])
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.pushButtonSignUpBig = QPushButton(self.stackedWidgetSignUp)
        self.pushButtonSignUpBig.setObjectName(u"pushButtonSignUpBig")
        self.pushButtonSignUpBig.setGeometry(QRect(30, 430, 251, 41))
        self.pushButtonSignUpBig.setFont(font2)
        self.pushButtonSignUpBig.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(170, 149, 132);\n"
"	border-radius : 5px; \n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     /* M\u00e0u n\u1ec1n khi di chu\u1ed9t qua */\n"
"	background-color: rgb(170, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     /* M\u00e0u n\u1ec1n khi n\u00fat \u0111\u01b0\u1ee3c nh\u1ea5n */\n"
"	background-color: rgb(170, 149, 132);\n"
"}")
        self.layoutWidget_2 = QWidget(self.stackedWidgetSignUp)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(50, 490, 181, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamilies([u"Lato"])
        font6.setPointSize(8)
        font6.setBold(False)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:rgba(0, 0, 0, 200);")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.pushButtonSignInSmall = QPushButton(self.layoutWidget_2)
        self.pushButtonSignInSmall.setObjectName(u"pushButtonSignInSmall")
        self.pushButtonSignInSmall.setFont(font4)
        self.pushButtonSignInSmall.setStyleSheet(u"color: rgb(170, 72, 2);")

        self.horizontalLayout_2.addWidget(self.pushButtonSignInSmall)

        self.lineEditFirstName = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")
        self.lineEditFirstName.setGeometry(QRect(20, 70, 251, 31))
        self.lineEditFirstName.setFont(font1)
        self.lineEditFirstName.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditConfirmPass = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditConfirmPass.setObjectName(u"lineEditConfirmPass")
        self.lineEditConfirmPass.setGeometry(QRect(20, 370, 251, 31))
        self.lineEditConfirmPass.setFont(font1)
        self.lineEditConfirmPass.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditConfirmPass.setEchoMode(QLineEdit.Password)
        self.lineEditPhoneNumber = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditPhoneNumber.setObjectName(u"lineEditPhoneNumber")
        self.lineEditPhoneNumber.setGeometry(QRect(20, 170, 251, 31))
        self.lineEditPhoneNumber.setFont(font1)
        self.lineEditPhoneNumber.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditEmail = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(20, 220, 251, 31))
        self.lineEditEmail.setFont(font1)
        self.lineEditEmail.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.lineEditLastName = QLineEdit(self.stackedWidgetSignUp)
        self.lineEditLastName.setObjectName(u"lineEditLastName")
        self.lineEditLastName.setGeometry(QRect(20, 120, 251, 31))
        self.lineEditLastName.setFont(font1)
        self.lineEditLastName.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.stackedWidget_Login.addWidget(self.stackedWidgetSignUp)

        self.gridLayout_3.addWidget(self.stackedWidget_Login, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget_Login.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Bamos Group", None))
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("Form", u" User Name", None))
        self.lineEditPass.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
        self.pushButtonSignInBig.setText(QCoreApplication.translate("Form", u"Log  In", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"You don't have account ?", None))
        self.pushButtonSignUpSmall.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.lineEditNewUsername.setPlaceholderText(QCoreApplication.translate("Form", u"  UserName", None))
        self.lineEditNewPass.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Create your account", None))
        self.pushButtonSignUpBig.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Already have account ?", None))
        self.pushButtonSignInSmall.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.lineEditFirstName.setPlaceholderText(QCoreApplication.translate("Form", u"  First Name", None))
        self.lineEditConfirmPass.setPlaceholderText(QCoreApplication.translate("Form", u"  Confirm Password", None))
        self.lineEditPhoneNumber.setPlaceholderText(QCoreApplication.translate("Form", u"  Phone Number", None))
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("Form", u"  Email", None))
        self.lineEditLastName.setPlaceholderText(QCoreApplication.translate("Form", u"  Last Name", None))
    # retranslateUi


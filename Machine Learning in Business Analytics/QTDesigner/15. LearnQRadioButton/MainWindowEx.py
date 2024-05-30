import json

from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

class MainWindowEX(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.getInformation)
    def getInformation(self):
        fullName=self.lineEditFullName.text()
        email=self.lineEditEmail.text()
        gender="Woman"
        if not self.radioButtonMan.isChecked():
            gender=self.radioButtonMan.text()
        city=self.lineEditFullName_2.text()
        country = self.lineEditEmail_2.text()
        degree="Bachelor"
        if self.radioButtonWoman_2.isChecked():
            degree=self.radioButtonWoman_2.text()
        elif self.radioButtonMan_2.isChecked():
            degree=self.radioButtonMan_2.text()
        elif self.radioButtonMan_3.isChecked():
            degree=self.radioButtonMan_3.text()
        information={"FullName":fullName,
                     "Email":email,
                     "Gender":gender,
                     "City":city,
                     "Country": country,
                     "Degree":degree
                     }
        self.msgBox=QMessageBox()
        self.msgBox.setWindowTitle("Information")
        self.msgBox.setText(json.dumps(information, ensure_ascii=False))
        self.msgBox.show()
    def show(self):
        self.MainWindow.show()
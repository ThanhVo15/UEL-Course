from Employee import Employee
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonclose.clicked.connect(self.processClose)
        self.pushButtonConfirm.clicked.connect(self.processConfirmation)
    def processConfirmation(self):
        name=self.lineEdit.text()
        gender="Man"
        if self.checkBoxMan.isChecked():
            gender="Man"
        if self.checkBoxWoman_2.isChecked():
            gender="Woman"
        city=self.comboBox.currentText()
        emp=Employee(name,gender,city)
        self.plainTextEdit.setPlainText(str(emp))
    def processClose(self):
        self.MainWindow.close()
    def show(self):
        self.MainWindow.show()
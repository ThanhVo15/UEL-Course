import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from Employee import Employee
from MainWindow import Ui_MainWindow
import os.path

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dataset=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.listWidget.itemSelectionChanged.connect(self.processItemSelectionChanged)
        self.pushButtonDelete.clicked.connect(self.processDelete)
        self.pushButtonClose.clicked.connect(self.processClose)
        self.readEmployeeFromJson()
    def show(self):
        self.MainWindow.show()
    def processNew(self):
        self.lineEditName.setText("")
        self.lineEditEmail.setText("")
        self.lineEditName.setFocus()

    def processSave(self):
        insertEmployee = Employee(self.lineEditName.text(), self.lineEditEmail.text(),
                                  self.radioButtonWoman.isChecked())
        isDuplicated = False
        updatingItemIndex = -1

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if insertEmployee.email.lower() == data.email.lower():
                isDuplicated = True
                updatingItemIndex = i
                break

        item = QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole, insertEmployee)
        item.setText(str(insertEmployee))
        item.setCheckState(Qt.CheckState.Unchecked)
        iconPath = r"D:\GitHub\UEL-Course\MLBA\QTDesigner\18. LearnQListWidgetEmployee\image\ic_woman.png" if self.radioButtonWoman.isChecked() else r"D:\GitHub\UEL-Course\MLBA\QTDesigner\18. LearnQListWidgetEmployee\image\ic_man.png"
        item.setIcon(QIcon(iconPath))

        if isDuplicated and updatingItemIndex != -1:
            self.listWidget.takeItem(updatingItemIndex)
            self.listWidget.insertItem(updatingItemIndex, item)
        elif not isDuplicated:
            self.listWidget.addItem(item)

        self.writeEmployeeToJson()
    def processItemSelectionChanged(self):
        current_row=self.listWidget.currentRow()
        if current_row<0:
            return
        item=self.listWidget.item(current_row)
        emp=item.data(Qt.ItemDataRole.UserRole)
        self.lineEditName.setText(emp.name)
        self.lineEditEmail.setText(emp.email)
        if emp.gender==True:
            self.radioButtonWoman.setChecked(True)
        else:
            self.radioButtonMan.setChecked(True)
    def processDelete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidget.count()-1,-1,-1):
            item=self.listWidget.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                current_item = self.listWidget.takeItem(index)
                del current_item
        self.processNew()
        self.writeEmployeeToJson()
    def processClose(self):
        msg = QMessageBox()
        msg.setText(f"Are you sure you want to exit ?")
        msg.setWindowTitle("Exit Confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Yes:
           self.MainWindow.close()

    def writeEmployeeToJson(self):
        dataset = [emp.to_dict() for emp in self.dataset]  # Chuyển đổi mỗi Employee thành dict
        jsonString = json.dumps(dataset)
        with open("database.json", "w") as jsonFile:
            jsonFile.write(jsonString)
    def readEmployeeFromJson(self):
        if os.path.isfile("database.json") ==False:
            return
        file = open('database.json', "r")
        # Reading from file
        self.dataset = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            if emp.gender==True:
                item.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\18. LearnQListWidgetEmployee\image\ic_woman.png"))
            else:
                item.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\18. LearnQListWidgetEmployee\image\ic_man.png"))
            self.listWidget.addItem(item)
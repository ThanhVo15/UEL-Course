from PyQt6.QtWidgets import QFileDialog, QMessageBox
from Employee import Employee
from EmployeeModel import EmployeeModel
from FileFactory import FileFactory
from MainWindow import Ui_MainWindow
from PyQt6.QtCore import QCoreApplication

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.employees=[]
        self.selectedEmployee=None
        self.fileFactory=FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.model=EmployeeModel(self.employees)
        self.listView.setModel(self.model)

        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        #self.listViewEmployee.clicked.connect(self.processClicked)
        self.listView.selectionModel().selectionChanged.connect(self.processSelection)
        self.pushButtonDelete.clicked.connect(self.processDelete)
        self.actionExport_to_JSon.triggered.connect(self.processExportJson)
        self.actionImport_from_JSon.triggered.connect(self.processImportJson)
        self.actionExir.triggered.connect(self.processExit)
    def processNew(self):
        self.lineEditID.setText("")
        self.lineEditName.setText("")
        self.lineEditAge.setText("")
        self.lineEditID.setFocus()
        self.selectedEmployee=None
    def processSave(self):
        id=self.lineEditID.text()
        name=self.lineEditName.text()
        age=int(self.lineEditAge.text())
        emp=Employee(id,name,age)
        if self.selectedEmployee==None:
            self.employees.append(emp)
            self.selectedEmployee=emp
        else:
            index=self.employees.index(self.selectedEmployee)
            self.selectedEmployee=emp
            self.employees[index]=self.selectedEmployee
        self.model.layoutChanged.emit()
    def processSelection(self):
        indexes=self.listView.selectedIndexes()
        if indexes:
            row=indexes[0].row()
            emp=self.employees[row]
            self.lineEditID.setText(str(emp.id))
            self.lineEditName.setText(emp.name)
            self.lineEditAge.setText(str(emp.age))
            self.selectedEmployee=emp
    def processDelete(self):
        dlg = QMessageBox(self.MainWindow)
        if self.selectedEmployee == None:
            dlg.setWindowTitle("Deleteing error")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setText("You have to select a Product to delete")
            dlg.exec()
            return
        dlg.setWindowTitle("Confirmation Deleting")
        dlg.setText("Are you sure you want to delete?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            self.employees.remove(self.selectedEmployee)
            self.model.layoutChanged.emit()
            self.selectedEmployee = None
            self.processNew()
    def processExportJson(self):
        # setup for QFileDialog
        filters = "Dataset (*.json);;All files(*)"
        filename, selected_filter = QFileDialog.getSaveFileName(
            self.MainWindow,
            filter=filters,
        )
        self.fileFactory.writeData(filename,self.employees)
    def processImportJson(self):
        # setup for QFileDialog
        filters = "Dataset (*.json);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        arr=self.fileFactory.readData(filename,Employee)

        self.employees.clear()

        for i in range(len(arr)):
            self.employees.append(arr[i])
        self.model.layoutChanged.emit()
    def processExit(self):
        QCoreApplication.instance().quit()
    def show(self):
        self.MainWindow.show()
from Employee import Employee
from EmployeeModel import EmployeeModel
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        employees = []
        employees.append(Employee(1, "Thanh", 21, "Man"))
        employees.append(Employee(2, "Minh", 22, "Female"))
        employees.append(Employee(3, "Hieu Hien", 24, "Male"))
        self.model = EmployeeModel(employees)
        self.listView.setModel(self.model)
    def show(self):
        self.MainWindow.show()

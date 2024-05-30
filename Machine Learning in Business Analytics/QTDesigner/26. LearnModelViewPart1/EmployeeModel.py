from PyQt6.QtCore import QAbstractListModel, Qt

class EmployeeModel(QAbstractListModel):
    def __init__(self, employees = None):
        super().__init__()
        self.employees = employees
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            emp = self.employees[index.row()]
            return str(emp)
    def rowCount(self,index):
        return len(self.employees)

import typing

from PyQt6 import QtGui
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex
from PyQt6.QtGui import QImage


class EmployeeModel(QAbstractListModel):
    def __init__(self,employees=None):
        super().__init__()
        self.employees=employees
    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        emp = self.employees[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(emp)
        if role==Qt.ItemDataRole.DecorationRole:
            if emp.age<18:
                return QImage(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\27. LearnModelViewPart2\image\ic_notvalid.png")
            else:
                return QImage(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\27. LearnModelViewPart2\image\ic_valid.png")
        if role==Qt.ItemDataRole.ForegroundRole:
            if emp.age < 18:
                return QtGui.QColor(Qt.GlobalColor.red)
        if role==Qt.ItemDataRole.BackgroundRole:
            if emp.age < 18:
                return QtGui.QColor(Qt.GlobalColor.yellow)
    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.employees)
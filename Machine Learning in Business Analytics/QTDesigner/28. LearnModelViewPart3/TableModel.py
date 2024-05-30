from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self, data,columns):
        super().__init__()
        self.data = data
        self.columns=columns

    def data(self, index, role):
        value=self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role==Qt.ItemDataRole.BackgroundRole:
            if index.column()==1 and value=="":
               return QtGui.QColor(Qt.GlobalColor.yellow)
        if role==Qt.ItemDataRole.ForegroundRole:
            if index.column() == 2 and value<100:
                return QtGui.QColor(Qt.GlobalColor.red)
    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.columns)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.columns[section])
            if orientation==Qt.Orientation.Vertical:
                return  str(section+1)
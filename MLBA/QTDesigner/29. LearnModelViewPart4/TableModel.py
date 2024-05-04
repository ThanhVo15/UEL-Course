from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, data,columns):
        super().__init__()
        self.data = data
        self.columns=columns

    def data(self, index, role):
        value = self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role==Qt.ItemDataRole.EditRole:
            return value
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 1 and value == "":
                return QtGui.QColor(Qt.GlobalColor.yellow)
        if role == Qt.ItemDataRole.ForegroundRole:
            if index.column() == 2 and  value!="" and float(value) < 100:
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

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled

        return super().flags(index) | Qt.ItemFlag.ItemIsEditable  # add editable flag.

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # Set the value into the frame.
            self.data[index.row()][index.column()] = value
            return True
        return False

    def insertRows(self, row, rows=1, index=QModelIndex()):
        print("Inserting at row: %s" % row)
        self.beginInsertRows(QModelIndex(), row, row + rows - 1)
        self.data.insert(row,["","",""])
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        print("Removing at row: %s" % row)
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        #self.data = self.data[:row] + self.data[row + rows:]
        del self.data[row]
        self.endRemoveRows()
        return True
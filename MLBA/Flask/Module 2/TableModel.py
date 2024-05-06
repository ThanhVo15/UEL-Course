from PyQt6.QtCore import QAbstractTableModel, Qt

class TableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self._data = data
        self._columns = columns

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._columns)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._columns[section]
            if orientation == Qt.Orientation.Vertical:
                return str(section + 1)
        return None

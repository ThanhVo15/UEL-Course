from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu, QFileDialog, QLineEdit, QPushButton, QTabWidget
from PyQt6.QtGui import QIcon, QColor
from PyQt6 import QtCore
from PyQt6.QtCore import QModelIndex, Qt, QAbstractTableModel, pyqtSlot
from Test.MainWindow import Ui_MainWindow
from Test.DatabaseConnectionsEx import DatabaseConnectEx
from functools import partial
from enum import Enum
import mysql.connector
import csv
from ConnectionsScreen.Connectors import Connector
from Test.TabSaleEx import TabSaleEx

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class InsertBehavior(Enum):
    INSERT_FIRST = 0
    INSERT_LAST = 1
    INSERT_ABOVE = 2
    INSERT_BELOW = 3

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)
        self.databaseConnectEx = DatabaseConnectEx(self)
        self.connector = Connector()
        self.tabsale = TabSaleEx(self)
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.pushButtonConnectDatabase.clicked.connect(self.openDatabaseConnectUI)
        self.actionConnect_to_Database.triggered.connect(self.openDatabaseConnectUI)
        self.actionExport_CSV.triggered.connect(self.exportToCSV)

        self.comboBoxChooseTable.currentIndexChanged.connect(self.tableSelectionChanged)
        self.pushButtonExecuteQuerry.clicked.connect(self.executeQuery)

        self.pushButtonFetchMore.clicked.connect(self.processFetchMore)  # Kết nối nút Fetch More

        self.tableViewShow.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableViewShow.customContextMenuRequested.connect(self.onCustomContextMenuRequested)

        self.tabWidget.currentChanged.connect(self.onTabChanged)

    def onTabChanged(self, index):
        if self.tabWidget.tabText(index) == "Sale":
            self.tabsale.updateSale()

    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()

    def updateLineEdit(self, database_name):
        self.lineEdit.setText(f"SQL_Workbench/{database_name}")

    def updateComboBox(self, tables):
        self.comboBoxChooseTable.clear()
        self.comboBoxChooseTable.addItems(tables)
        self.comboBoxChooseTable.setCurrentIndex(0)

    def tableSelectionChanged(self):
        selected_table = self.comboBoxChooseTable.currentText()
        if selected_table:
            self.databaseConnectEx.showTableData(selected_table)
            self.lineEditquery.setText(f"SELECT * FROM {selected_table};")  # Cập nhật query mặc định

    def executeQuery(self):
        query = self.lineEditquery.text()
        try:
            df = self.databaseConnectEx.connector.queryDataset(query)
            if df is not None and not df.empty:
                model = TableModel(df.values.tolist(), df.columns.tolist())
                self.tableViewShow.setModel(model)
            else:
                raise Exception("Query returned no data")
        except mysql.connector.Error as err:
            self.showErrorDialog("Query Error", f"Invalid query syntax or execution error:\n{str(err)}")
        except Exception as e:
            self.showErrorDialog("Query Error", str(e))

    def showErrorDialog(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def onCustomContextMenuRequested(self, pos):
        index = self.tableViewShow.indexAt(pos)
        menu = QMenu()
        if index.isValid():
            insertFirst = menu.addAction("Insert &First")
            insertFirst.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert top.png"))
            insertLast = menu.addAction("Insert &Last")
            insertLast.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert last.png"))
            insertAbove = menu.addAction("Insert &Above")
            insertAbove.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert above.png"))
            insertBelow = menu.addAction("Insert &Below")
            insertBelow.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert below.png"))
            removeSelected = menu.addAction("Remove selected row")
            removeSelected.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_delete.png"))

            menu.addAction(insertFirst)
            menu.addAction(insertLast)
            menu.addAction(insertAbove)
            menu.addAction(insertBelow)
            menu.addSeparator()
            menu.addAction(removeSelected)

            insertFirst.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_FIRST))
            insertLast.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_LAST))
            insertAbove.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_ABOVE))
            insertBelow.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_BELOW))
            removeSelected.triggered.connect(self.processDelete)
            menu.exec(self.tableViewShow.viewport().mapToGlobal(pos))
        else:
            insertNew = menu.addAction("Insert New Record")
            insertNew.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_new.png"))
            insertNew.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_FIRST))
            menu.addAction(insertNew)
            menu.exec(self.tableViewShow.viewport().mapToGlobal(pos))

    def processInsert(self, behavior=InsertBehavior.INSERT_FIRST):
        indexes = self.tableViewShow.selectionModel().selectedIndexes()
        if behavior == InsertBehavior.INSERT_FIRST:
            row = 0
        elif behavior == InsertBehavior.INSERT_LAST:
            row = self.tableViewShow.model().rowCount(QModelIndex())
        else:
            if indexes:
                index = indexes[0]
                row = index.row()
                if behavior == InsertBehavior.INSERT_ABOVE:
                    row = max(row, 0)
                else:
                    size = self.tableViewShow.model().rowCount(QModelIndex())
                    row = min(row + 1, size)
        self.tableViewShow.model().insertRows(row, 1, QModelIndex())

    def processDelete(self):
        indexes = self.tableViewShow.selectionModel().selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            self.tableViewShow.model().removeRows(row, 1, QModelIndex())

    def processFetchMore(self):
        model = self.tableViewShow.model()
        if hasattr(model, 'canFetchMore') and model.canFetchMore(QModelIndex()):
            model.fetchMore(QModelIndex())
        else:
            msg = QMessageBox()
            msg.setText("No more records to fetch")
            msg.exec()

    def exportToCSV(self):
        model = self.tableViewShow.model()
        if model is None:
            self.showErrorDialog("Export Error", "No data available to export")
            return

        # Get the path to save the file
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if not filePath:
            return

        # Save the data to the CSV file
        try:
            with open(filePath, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                headers = [model.headerData(i, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole) for i in range(model.columnCount(QModelIndex()))]
                writer.writerow(headers)
                # Write data
                for row in range(model.rowCount(QModelIndex())):
                    rowData = [model.data(model.index(row, col), Qt.ItemDataRole.DisplayRole) for col in range(model.columnCount(QModelIndex()))]
                    writer.writerow(rowData)
            QMessageBox.information(self, "Export Successful", f"Data successfully exported to {filePath}")
        except Exception as e:
            self.showErrorDialog("Export Error", f"Failed to export data: {str(e)}")


    def show(self):
        self.MainWindow.show()

class TableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self.data = data
        self.columns = columns
        self.batch_size = 10  # số lượng dữ liệu sẽ fetch thêm mỗi lần
        self.fetched_rows = self.batch_size

    def data(self, index, role):
        value = self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            return value
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 1 and value == "":
                return QColor(Qt.GlobalColor.yellow)
        if role == Qt.ItemDataRole.ForegroundRole:
            if index.column() == 2 and value != "" and float(value) < 100:
                return QColor(Qt.GlobalColor.red)

    def rowCount(self, index):
        return min(self.fetched_rows, len(self.data))

    def columnCount(self, index):
        return len(self.columns)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(section + 1)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled

        return super().flags(index) | Qt.ItemFlag.ItemIsEditable  # add editable flag.

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # Set the value into the frame.
            self.data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def insertRows(self, row, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), row, row + rows - 1)
        for _ in range(rows):
            self.data.insert(row, [""] * self.columnCount(index))
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        del self.data[row:row + rows]
        self.endRemoveRows()
        return True

    def canFetchMore(self, index):
        return self.fetched_rows < len(self.data)

    def fetchMore(self, index):
        remaining_rows = len(self.data) - self.fetched_rows
        fetch_rows = min(remaining_rows, self.batch_size)
        self.beginInsertRows(QModelIndex(), self.fetched_rows, self.fetched_rows + fetch_rows - 1)
        self.fetched_rows += fetch_rows
        self.endInsertRows()



from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QMainWindow
from Connectors import Connector
from DatabaseConnections import Ui_MainWindow
import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem

class DatabaseConnectEx(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatabaseConnectEx, self).__init__(parent)
        self.setupUi(self)
        self.parent_window = parent

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.mainWindow = MainWindow
        self.pushButtonConnect.clicked.connect(self.processConnectDatabase)
        self.pushButtonExit.clicked.connect(self.processExit)

    def processConnectDatabase(self):
        try:
            self.connector = Connector()
            self.connector.server = self.lineEditSever.text()
            self.connector.port = int(self.lineEditPort.text())
            self.connector.database = self.lineEditDatabase.text()
            self.connector.username = self.lineEditUser.text()
            self.connector.password = self.lineEditPassword.text()

            if self.connector.connect():
                self.msg = QMessageBox()
                self.msg.setText(f"Connect to Database: {self.connector.database} Successful!")
                self.msg.setWindowTitle("Info")
                self.msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                self.msg.buttonClicked.connect(self.onMessageBoxClosed)
                self.msg.exec()
                if self.parent_window:
                    self.parent_window.updateLineEdit(self.connector.database)
                tables = self.connector.getTablesName()
                if tables:
                    self.parent_window.updateComboBox(tables)
                    self.parent_window.comboBoxChooseTable.setCurrentIndex(0)
                    self.showTableData(tables[0])
            else:
                raise Exception("Failed to connect to the database")

        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setText(f"Failed to connect to database: {str(e)}")
            self.msg.setWindowTitle("Info")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msg.exec()

    def showTableData(self, table_name):
        df = self.connector.queryDataset(f"SELECT * FROM {table_name}")
        if df is not None:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(df.columns)
            for row in df.itertuples(index=False):
                items = [QStandardItem(str(field)) for field in row]
                model.appendRow(items)
            if self.parent_window:
                self.parent_window.tableViewShow.setModel(model)

    def onMessageBoxClosed(self, button):
        self.mainWindow.close()

    def processExit(self):
        self.mainWindow.close()

    def show(self):
        self.mainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.mainWindow.show()

from PyQt6.QtWidgets import QApplication, QMainWindow
from .MainWindow import Ui_MainWindow
from Test.DatabaseConnectionsEx import DatabaseConnectEx

class MainWindowEx(QMainWindow, Ui_MainWindow):  # Kế thừa từ QMainWindow và Ui_MainWindow
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)
        self.databaseConnectEx = DatabaseConnectEx(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.pushButtonConnectDatabase.clicked.connect(self.openDatabaseConnectUI)
        self.actionConnect_to_Database.triggered.connect(self.openDatabaseConnectUI)

        self.comboBoxChooseTable.currentIndexChanged.connect(self.tableSelectionChanged)

    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()

    def updateLineEdit(self, database_name):
        self.lineEdit.setText(f"SQL_Workbench/{database_name}")

    def updateComboBox(self, tables):  # Thay đổi highlight
        self.comboBoxChooseTable.clear()
        self.comboBoxChooseTable.addItems(tables)
        self.comboBoxChooseTable.setCurrentIndex(0)  # Chọn bảng đầu tiên sau khi cập nhật

    def tableSelectionChanged(self):  # Thay đổi highlight
        selected_table = self.comboBoxChooseTable.currentText()
        if selected_table:
            self.databaseConnectEx.showTableData(selected_table)

    def show(self):
        self.MainWindow.show()

import traceback
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow

from ConnectionsScreen.Connectors import Connector
from DatabaseConnections import Ui_mainWindow

class DatabaseConnectEx(Ui_mainWindow):
    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
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

            self.connector.connect()

            self.msg = QMessageBox()
            self.msg.setText(f"Connect to Database: {self.connector.database} Successful!")
            self.msg.setWindowTitle("Info")
            self.msg.exec()

            #if self.parent() is not None:
             #   self.parent().checkEnableWidget(True)
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setText(f"Failed to connect to database: {str(e)}")
            self.msg.setWindowTitle("Info")
            self.msg.exec()

    def processExit(self):
        self.mainWindow.close()

    def show(self):
        self.mainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.mainWindow.show()

def show(self):
    self.show()


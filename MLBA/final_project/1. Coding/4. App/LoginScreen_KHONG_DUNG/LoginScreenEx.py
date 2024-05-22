from PyQt6.QtWidgets import QMainWindow, QMessageBox
from .LoginScreen import Ui_MainWindow
import mysql.connector

class LoginScreenEx(QMainWindow, Ui_MainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setupUi(self)
        self.stacked_widget = stacked_widget
        self.pushButtonLogIn.clicked.connect(self.login)
        self.pushButtonCreateAccount.clicked.connect(self.show_create_account)

    def login(self):
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Obama123',
            database='final_project'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM staff WHERE first_name=%s AND last_name=%s", (username, password))
        if cursor.fetchone():
            self.stacked_widget.setCurrentIndex(3)
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
        cursor.close()
        conn.close()

    def show_create_account(self):
        self.stacked_widget.setCurrentIndex(1)

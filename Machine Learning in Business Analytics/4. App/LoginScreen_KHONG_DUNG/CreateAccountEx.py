from PyQt6.QtWidgets import QMainWindow, QMessageBox
from .CreateAccount import Ui_MainWindow
import mysql.connector

class CreateAccountEx(QMainWindow, Ui_MainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setupUi(self)
        self.stacked_widget = stacked_widget
        self.pushButtonCreateAccount.clicked.connect(self.create_account)
        self.pushButtonLogIn.clicked.connect(self.show_login)

    def create_account(self):
        first_name = self.lineEditFirstName.text()
        last_name = self.lineEditLastName.text()
        position = self.comboBoxPositions.currentText()
        start_date = self.dateEditStartDate.text()
        location = self.comboBoxPositions_2.currentText()

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Obama123',
            database='final_project'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM staffs WHERE first_name=%s AND last_name=%s", (first_name, last_name))
        if cursor.fetchone():
            QMessageBox.warning(self, "Error", "Account already exists. Please login.")
            self.stacked_widget.setCurrentIndex(2)
        else:
            cursor.execute("INSERT INTO staffs (first_name, last_name, position, start_date, location) VALUES (%s, %s, %s, %s, %s)",
                           (first_name, last_name, position, start_date, location))
            conn.commit()
            QMessageBox.information(self, "Success", "Account created successfully. Please login.")
            self.stacked_widget.setCurrentIndex(2)
        cursor.close()
        conn.close()
    def show_login(self):
        self.stacked_widget.setCurrentIndex(2)


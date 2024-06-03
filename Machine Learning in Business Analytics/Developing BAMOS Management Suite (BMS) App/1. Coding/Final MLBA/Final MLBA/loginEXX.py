
from Connectors import Connector
from login_ui import Ui_Form
import numpy as np
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QWidget
import re
from MainWindowEx import MainWindowEx
from MainWindow_ui import Ui_MainWindow
class MainWindow(Ui_Form):

    def __init__(self):
        super().__init__()
        self.connector = Connector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSignInBig.clicked.connect(self.SignIn_to_MainPage)  # nút đăng nhập để vào trang màn hình chính
        self.pushButtonSignUpBig.clicked.connect(self.SignUp_account)      # nút đăng kí tài khoản mới

        self.pushButtonSignInSmall.clicked.connect(self.switch_to_SignInPage) # nút chuyển sang trang đănng nhập
        self.pushButtonSignUpSmall.clicked.connect(self.switch_to_SignUpPage) # nút chuyển sang trang đănng kí
        


    def switch_to_SignInPage(self): # hàm chuyển sang trang đănng nhập
        self.stackedWidget_Login.setCurrentIndex(0)
    def switch_to_SignUpPage(self):# hàm chuyển sang trang đănng nhập
        self.stackedWidget_Login.setCurrentIndex(1)  
      
    def connectDatabase(self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "final_project"
        self.connector.username = "root"
        self.connector.password = "luannt_1005"
        self.connector.connect()


    def SignIn_to_MainPage(self): # hàm đăng nhập
        username = self.lineEditUsername.text()
        password = self.lineEditPass.text()

        if not username or not password:
            QMessageBox.warning(self.MainWindow, "Login Failed", "Username and password cannot be empty!")
            return
        

        self.connectDatabase()
        username_pass_sql = f"SELECT * FROM staffs WHERE user_name = '{username}' and password_acc ='{password}' "
        result = self.connector.queryDataset(username_pass_sql)
        if not result.empty:
            # QMessageBox.information(self.MainWindow, "Login success", "You have successfully logged in")
            window = QMainWindow()
            self.chartUi = MainWindowEx()
            self.chartUi.setupUi(window)
            self.chartUi.show()
            # self.RenameLabel = Ui_MainWindow()
            # self.RenameLabel.label_8.setText('vaicalon')
            self.MainWindow.close()
            
        else:
            QMessageBox.warning(self.MainWindow, "Login Failed", "Invalid username or password!")
    
    def is_password_strong(self, password):
        if (len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password)):
            return True
        return False

    def SignUp_account(self): # hàm đăng kí tài khoản mới
        first_name = self.lineEditFirstName.text()
        last_name = self.lineEditLastName.text()
        phone_number = self.lineEditPhoneNumber.text()
        email = self.lineEditEmail.text()
        username = self.lineEditNewUsername.text()
        password = self.lineEditNewPass.text()
        confirm_password = self.lineEditConfirmPass.text()

        if not first_name or not last_name or not phone_number or not email or not username or not password or not confirm_password:
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "All fields must be filled!")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Invalid email format!")
            return

        if not phone_number.isdigit() or len(phone_number) != 10:
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Phone number must be 10 digits!")
            return

        if not self.is_password_strong(password):
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Password is not strong enough! Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one digit.")
            
            return

        if password != confirm_password:
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Passwords do not match!")
            return

        self.connectDatabase()

        username_check_sql = "SELECT * FROM staffs WHERE user_name = %s"
        email_check_sql = "SELECT * FROM staffs WHERE email = %s"

        result = self.connector.queryDataset(username_check_sql, (username,))
        if not result.empty:
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Username already exists! Please choose another one.")
            return

        result = self.connector.queryDataset(email_check_sql, (email,))
        if not result.empty:
            QMessageBox.warning(self.MainWindow, "Sign Up Failed", "Email already exists! Please use another email.")
            return

        insert_user_sql = """
            INSERT INTO staffs (first_name, last_name, position, start_day, location, user_name, password_acc, phone, email)
            VALUES (%s, %s, %s, CURDATE(), %s, %s, %s, %s, %s)
        """
        self.connector.executeNonQuery(insert_user_sql, (first_name, last_name, 'Null', 'Null', username, password, phone_number, email))
        QMessageBox.information(self.MainWindow, "Sign Up Success", "Account has been successfully created!")
            

    def show(self):
        self.MainWindow.show()



    







    
   




    






  



    



    def show(self):
        self.MainWindow.show()



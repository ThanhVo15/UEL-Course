import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QStackedWidget

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Homepage!")
        layout.addWidget(label)
        self.setLayout(layout)

class LoginScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password input
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        create_account_button = QPushButton("Create Account", self)
        create_account_button.clicked.connect(self.show_create_account)
        layout.addWidget(create_account_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Simple validation logic (replace with real authentication)
        if username == "admin" and password == "password":
            self.stacked_widget.setCurrentIndex(2)
        else:
            error_label = QLabel("Invalid username or password", self)
            self.layout().addWidget(error_label)

    def show_create_account(self):
        self.stacked_widget.setCurrentIndex(1)

class CreateAccountScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("New Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("New Password")
        layout.addWidget(self.password_input)

        create_button = QPushButton("Create Account", self)
        create_button.clicked.connect(self.create_account)
        layout.addWidget(create_button)

        back_button = QPushButton("Back to Login", self)
        back_button.clicked.connect(self.show_login)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def create_account(self):
        # Implement your create account logic here
        self.stacked_widget.setCurrentIndex(0)

    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_screen = LoginScreen(self.stacked_widget)
        self.create_account_screen = CreateAccountScreen(self.stacked_widget)
        self.home_screen = HomeScreen()

        self.stacked_widget.addWidget(self.login_screen)          # Index 0
        self.stacked_widget.addWidget(self.create_account_screen) # Index 1
        self.stacked_widget.addWidget(self.home_screen)           # Index 2

        self.stacked_widget.setCurrentIndex(0)

def main():
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

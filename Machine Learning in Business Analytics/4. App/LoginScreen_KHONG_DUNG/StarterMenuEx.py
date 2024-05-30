from PyQt6.QtWidgets import QMainWindow
from .StarterMenu import Ui_MainWindow

class StarterMenuEx(QMainWindow, Ui_MainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setupUi(self)
        self.stacked_widget = stacked_widget
        self.pushButtonCreateAccount.clicked.connect(self.show_create_account)
        self.pushButtonLogin.clicked.connect(self.show_login)

    def show_create_account(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_login(self):
        self.stacked_widget.setCurrentIndex(2)

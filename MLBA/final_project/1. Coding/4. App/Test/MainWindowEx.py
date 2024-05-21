from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from LoginScreen.StarterMenuEx import StarterMenuEx
from LoginScreen.CreateAccountEx import CreateAccountEx
from LoginScreen.LoginScreenEx import LoginScreenEx
from .MainWindow import Ui_MainWindow

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.starter_menu = StarterMenuEx(self.stacked_widget)
        self.create_account = CreateAccountEx(self.stacked_widget)
        self.login_screen = LoginScreenEx(self.stacked_widget)
        self.MainWindow = MainWindow(self.stacked_widget)

        self.stacked_widget.addWidget(self.starter_menu)  # Index 0
        self.stacked_widget.addWidget(self.create_account)  # Index 1
        self.stacked_widget.addWidget(self.login_screen)  # Index 2

        self.stacked_widget.addWidget(self)  # Index 3

        self.stacked_widget.setCurrentIndex(0)  # Show Starter Menu initially

        self.adjust_size_to_current_widget()

        self.stacked_widget.currentChanged.connect(self.adjust_size_to_current_widget)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()
    def adjust_size_to_current_widget(self):
        current_widget = self.stacked_widget.currentWidget()
        self.setFixedSize(current_widget.sizeHint())
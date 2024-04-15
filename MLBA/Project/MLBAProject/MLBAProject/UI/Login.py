from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 640)  # Set the window size as per the aspect ratio of the image

        # Set window icon - you'll need to add the path to your icon here
        icon = QIcon("path_to_icon.png")
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.labelGreeting = QLabel("Hello\nWelcome To Little Drop, where\nyou manage your daily tasks",
                                    self.centralwidget)
        self.labelGreeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.labelGreeting)

        # Add the Login Button
        self.buttonLogin = QPushButton("Login", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonLogin)

        # Add the Sign Up Button
        self.buttonSignUp = QPushButton("Sign Up", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonSignUp)

        # Add the social media sign up options label
        self.labelSocialSignUp = QLabel("Sign up using", self.centralwidget)
        self.labelSocialSignUp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.labelSocialSignUp)

        # Optionally add buttons for social media sign up
        self.buttonFacebook = QPushButton("Facebook", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonFacebook)

        self.buttonGoogle = QPushButton("Google+", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonGoogle)

        self.buttonLinkedIn = QPushButton("LinkedIn", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonLinkedIn)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Little Drop"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from MyQMainWindow import Ui_MainWindow
from SecondWindow import SecondWindow


class MyQMainWindowExt(Ui_MainWindow):
    #override setupUi
    #just define attribute MainWindow for reuse in later
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.secondWindow=None
    #define methods for assigning Signals and Slots
    def processSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonVisitBlog.clicked.connect(self.openMyBlog)
        self.pushButtonSendName.clicked.connect(self.openSecondWindow)
    #define slot exit window
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass#do nothing
    def openMyBlog(self):
        import webbrowser
        webbrowser.open('https://www.facebook.com/httt.uel/posts/pfbid0VqDsbD7YtetApSc9YSXQbK91DJ624pkFzqEjSj6DXRazvLV3xmsXJnw67xbxbjYUl')
    def openSecondWindow(self):
        if self.secondWindow==None or self.qmainWindow.isVisible()==False:
            self.qmainWindow = QMainWindow()
            self.secondWindow=SecondWindow(self)
            self.secondWindow.setupUi(self.qmainWindow)
            self.qmainWindow.show()
    def changeRedColor(self):
        self.MainWindow.setStyleSheet("background-color: red;")
    def changeYellowColor(self):
        self.MainWindow.setStyleSheet("background-color: yellow;")
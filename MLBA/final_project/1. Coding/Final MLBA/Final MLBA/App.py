import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindowEx import MainWindowEx
app = QApplication([])
myWindow = MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()





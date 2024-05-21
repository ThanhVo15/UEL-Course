from PySide6.QtWidgets import QApplication, QMainWindow
from MainwindowEx import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
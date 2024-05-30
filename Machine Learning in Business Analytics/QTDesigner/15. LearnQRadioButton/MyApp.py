from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEx import MainWindowEX

app=QApplication([])
myWindow=MainWindowEX()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
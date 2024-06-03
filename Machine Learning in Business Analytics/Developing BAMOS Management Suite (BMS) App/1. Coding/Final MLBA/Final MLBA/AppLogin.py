from loginEXX import MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

app=QApplication([])
myWindow=MainWindow()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
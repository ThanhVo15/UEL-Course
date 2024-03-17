from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType(r'D:\GitHub\UEL-Course\MLBA\Buổi 8\HelloWorldDialog.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

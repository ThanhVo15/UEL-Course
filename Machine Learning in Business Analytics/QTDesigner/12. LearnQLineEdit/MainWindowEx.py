from PyQt6.QtWidgets import QCompleter
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        cities = ["Hà Nội", "Huế", "Đà Nẵng", "Đà Lạt", "Hồ Chí Minh", "Cần Thơ", "Kon Tum"]
        completer = QCompleter(cities)
        self.CityProvinceLineEdit.setCompleter(completer)
    def show(self):
        self.MainWindow.show()
from MainWindow import Ui_MainWindow
from TableModel import TableModel


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        data = [["p1", "Coca", 100],
                ["p2", "Pepsi", 50],
                ["p3", "Sting", 300],
                ["p4", "Aqua", 70],
                ["p5", "Redbull", 200],
                ["p6", "", 120]]
        columns = ["ID", "Name", "Price"]
        self.model = TableModel(data, columns)
        self.tableViewProduct.setModel(self.model)
    def show(self):
        self.MainWindow.show()
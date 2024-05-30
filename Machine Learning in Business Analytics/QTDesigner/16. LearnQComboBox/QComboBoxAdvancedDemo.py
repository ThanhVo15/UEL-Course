import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from Category import Category

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tran Duy Thanh')
        self.setMinimumWidth(300)

        # create a vertical layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a Category:', self)

        # create a combobox
        self.cboCategory = QComboBox(self)

        laptop_icon = QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\16. LearnQComboBox\image\ic_computer.png")
        laptop_model = Category(100, "Laptop")
        self.cboCategory.addItem(laptop_icon, laptop_model.name, laptop_model)

        phone_icon = QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\16. LearnQComboBox\image\ic_phone.png")
        phone_model = Category(200, "Phone")
        self.cboCategory.addItem(phone_icon, phone_model.name, phone_model)

        smart_icon = QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\16. LearnQComboBox\image\ic_smart_watch.png")
        smart_model = Category(300, "Smart Watch")
        self.cboCategory.addItem(smart_icon, smart_model.name, smart_model)

        self.cboCategory.activated.connect(self.processSelectedComboBox)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cboCategory)
        layout.addWidget(self.result_label)

        self.show()

    def processSelectedComboBox(self, index):
        data = self.cboCategory.itemData(index)
        self.result_label.setText(f'You selected items = {data}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

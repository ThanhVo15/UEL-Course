import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Vo Minh Thanh')
        self.setMinimumWidth(300)

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a Category:', self)

        # create a combobox
        self.cboCategory = QComboBox(self)
        self.cboCategory.addItem('Laptop')
        self.cboCategory.addItem('Phone & Tablet')
        self.cboCategory.addItem('Smart Watch')
        self.cboCategory.insertItem(1,"Head Phone")

        self.cboCategory.insertItems(2,["Mouse","Mouse Pad"])
        self.cboCategory.addItems(["Game & Stream","Monitor"])

        self.cboCategory.activated.connect(self.processSelectedComboBox)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cboCategory)
        layout.addWidget(self.result_label)

        self.show()

    def processSelectedComboBox(self):
        index=self.cboCategory.currentIndex()
        text=self.cboCategory.currentText()
        self.result_label.setText(
            f'You selected index= {index}, text={text}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.previous=''
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonDrawCaro.clicked.connect(self.processDrawCaro)
    def processDrawCaro(self):
        row=int(self.lineEditRows.text())
        column=int(self.lineEditColumn.text())
        for i in  range(row):
            self.gridLayoutCaro.setRowStretch(i,1)
            for j in range(column):
                self.gridLayoutCaro.setColumnStretch(j,1)
                btn= QPushButton()
                btn.setFixedWidth(50)
                btn.setFixedHeight(50)
                btn.sizePolicy().setHorizontalStretch(1)
                btn.sizePolicy().setVerticalStretch(1)
                self.gridLayoutCaro.addWidget(btn, i, j,
                         alignment=Qt.AlignmentFlag.AlignVertical_Mask|Qt.AlignmentFlag.AlignHorizontal_Mask)
                btn.clicked.connect(partial(self.processClicked, btn))
    def processClicked(self,btn):
        if len(btn.text()) > 0:
            return
        if self.previous=="X":
            self.previous="O"
        else:
            self.previous = "X"
        if len(btn.text())==0:
            btn.setText(self.previous)
        else:
            btn.setText(self.previous)
    def show(self):
        self.MainWindow.show()
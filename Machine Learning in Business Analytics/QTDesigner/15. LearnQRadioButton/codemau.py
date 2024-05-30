from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QRadioButton
from PyQt6.QtWidgets import QButtonGroup

app = QApplication([])

w = QWidget()
w.setWindowTitle("Trần Duy Thanh - QRadioButton")
w.resize(300, 150)

radRed = QRadioButton("Red",w)
radRed.move(20, 20)

radGreen = QRadioButton("Green",w)
radGreen.move(20, 40)

radBlue = QRadioButton("Blue",w)
radBlue.move(20, 60)

color_group = QButtonGroup(w)
color_group.addButton(radRed)
color_group.addButton(radGreen)
color_group.addButton(radBlue)

def changeBackgroundToRed(value):
    if value==True:
        w.setStyleSheet("background-color:red;");
def changeBackgroundToGreen(value):
    if value == True:
        w.setStyleSheet("background-color:green;")
def changeBackgroundToBlue(value):
    if value == True:
        w.setStyleSheet("background-color:blue;")
radRed.clicked.connect(changeBackgroundToRed)
radGreen.clicked.connect(changeBackgroundToGreen)
radBlue.clicked.connect(changeBackgroundToBlue)

w.show()

app.exec()
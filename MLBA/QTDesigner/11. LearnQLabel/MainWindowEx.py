from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QMovie
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.changeTextpushButton.clicked.connect(self.processChangeText)
        self.fontSizepushButton.clicked.connect(self.processChangeFontSize)
        self.alignCenterpushButton.clicked.connect(self.processAlignCenter)
        self.alignLeftpushButton.clicked.connect(self.processAlignLeft)
        self.alignRightpushButton.clicked.connect(self.processAlignRight)
        self.showPNGpushButton.clicked.connect(self.processChangePNG)
        self.showGIFpushButton.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.Titlelabel.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0782;\">Vo Minh Thanh Dep Trai</span></p></body></html>")
    def processChangeFontSize(self):
        font = self.Titlelabel.font()
        font.setPointSize(20)
        font.setItalic(True)
        font.setBold(True)
        font.setFamily("cambria")
        self.Titlelabel.setFont(font)
    def processAlignLeft(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        pixmap = QPixmap(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\11. LearnQLabel\images\darshan-raval.gif")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
    def processChangeGIF(self):
        movie = QMovie(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\11. LearnQLabel\images\darshan-raval.gif")
        self.label_2.setMovie(movie)
        self.label_2.setScaledContents(True)
        movie.start()




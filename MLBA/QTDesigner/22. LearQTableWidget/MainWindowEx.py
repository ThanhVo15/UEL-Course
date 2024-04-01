from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.tableWidgetSong.itemSelectionChanged.connect(self.processSelectedItem)
        self.pushButtonClose.clicked.connect(self.processClose)
    def processSelectedItem(self):
        row=self.tableWidgetSong.currentRow()
        songId=self.tableWidgetSong.item(row,0)
        songName=self.tableWidgetSong.item(row,1)
        singer=self.tableWidgetSong.item(row,2)
        self.lineEditSongID.setText(songId.text())
        self.lineEditSongName.setText(songName.text())
        self.lineEditSinger.setText(singer.text())
    def processClose(self):
        self.MainWindow.close()
    def show(self):
        self.MainWindow.show()
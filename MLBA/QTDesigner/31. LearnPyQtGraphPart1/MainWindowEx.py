from MainWindow import Ui_MainWindow
#Step 1: import pyqtgraph
import pyqtgraph as pg

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        #Step 2: call pg.PlotWidget()
        self.graphWidget = pg.PlotWidget()
        #Step 3: Create plot data
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
        temperature = [20, 21, 20, 32, 33, 31, 29,31, 32, 35,37, 45]
        #Step 4: call plot method
        self.graphWidget.plot(hour, temperature)
        #Step 5: add graphWidget into Layout:
        self.myLayout.addWidget(self.graphWidget)
    def show(self):
        self.MainWindow.show()
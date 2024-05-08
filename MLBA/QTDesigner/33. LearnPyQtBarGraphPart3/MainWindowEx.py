from MainWindow import Ui_MainWindow
#Step 1: import pyqtgraph
import pyqtgraph as pg

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.setupBarGraph()
    def setupBarGraph(self):
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setTitle("Lucy Company", color = "r", size = "15pt", bold = True, italic = True)
        self.graphWidget.setBackground("w")

        labelStyle = {"color": "green", "font-size": "18px"}
        labelBrandstyle = {"color": "blue", "font-size": "18px"}
        self.graphWidget.setLabel("left", "Revenue (VND)", **labelStyle)
        self.graphWidget.setLabel("bottom", "Quarter (time)", **labelStyle)
        self.graphWidget.setLabel("top", "Revenue Report", **labelStyle)
        self.graphWidget.setLabel("right", "Vo Minh Thanh Coding", **labelBrandstyle)
        self.graphWidget.showGrid(x = True, y = True)

        width = 0.3

        quarter = [1,2,3,4]
        revenue = [100,200,300,250]

        self.bargraphItem = pg.BarGraphItem(x = quarter, height = revenue, width = width, brush = "b", name = "ABC Revenue")
        self.legend = self.graphWidget.addLegend()
        self.graphWidget.addItem(self.bargraphItem)
        self.myLayout.addWidget(self.graphWidget)
    def show(self):
        self.MainWindow.show()
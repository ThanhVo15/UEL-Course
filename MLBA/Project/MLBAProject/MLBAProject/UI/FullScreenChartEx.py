from UI.ChartHandle import ChartHandle
from UI.FullScreenChart import Ui_MainWindow

from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class FullScreenChartEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupPlot()
        self.chartHandle = ChartHandle()
    def show(self):
        self.MainWindow.show()
    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        # adding tool bar to the layout
        self.verticalLayoutPlot.addWidget(self.toolbar)
        # adding canvas to the layout
        self.verticalLayoutPlot.addWidget(self.canvas)

from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QColorDialog, QMainWindow

from MainWindow import Ui_MainWindow
import numpy as np
import pyqtgraph as pg

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupBarGraph()
        self.xlab = ["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"]
        self.autoTick(self.graphWidget, self.xlab)
        self.autolabel([self.bargraphItem])

    def autoTick(self, graphWidget, xlab):
        ticks = []
        for i, item in enumerate(xlab):
            ticks.append((i + 1, item))
        ticks = [ticks]
        ax = graphWidget.getAxis('bottom')
        ax.setTicks(ticks)

    def autolabel(self, barItems):
        # attach some text labels
        for barItem in barItems:
            xs, heights = barItem.getData()
            for i in range(len(heights)):
                height = heights[i]
                x = xs[i]
                clr = barItem.opts["brush"]
                text = pg.TextItem(str(height), color=clr)
                text.setParentItem(barItem)
                text.setX(x)
                text.setY(height)
                text.setAnchor((QPointF(0.5, 0.75)))
    def setupBarGraph(self):
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setTitle("Revenue Report", color = "b", size = "15pt", bold = True, italic = True)
        self.graphWidget.setBackground('w')

        labelStyle = {"color":'green', "font-size": "15px"}
        labelBrandStyle = {"color": "purple", "font-size": "15px"}
        self.graphWidget.setLabel("right", "Vo Minh Thanh Coding", **labelBrandStyle)
        self.graphWidget.setLabel("left", "Revenue (VND)", **labelStyle)
        self.graphWidget.setLabel("bottom", "Quarter (Time)", **labelStyle)
        self.graphWidget.showGrid(x = True, y = True)

        quarter = np.array([1,2,3,4])
        revenue = [100, 200,300,250]

        self.bargraphItem = pg.BarGraphItem(x = quarter, height = revenue, width = 0.3, brush = "b", name = "ABC Revenue")
        self.legend = self.graphWidget.addLegend()

        self.graphWidget.addItem(self.bargraphItem)
        self.myLayout.addWidget(self.graphWidget)

        self.checkBoxBackgroundGrid.stateChanged.connect(self.processChangeGrid)
        self.checkBoxLegend.stateChanged.connect(self.processChangeLegend)
        self.pushButtonChartBackground.clicked.connect(self.processChangeChartBackground)
        self.pushButtonBarColor.clicked.connect(self.processChangeBarColor)
        self.pushButtonClose.clicked.connect(self.processClose)

    def processChangeGrid(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.graphWidget.showGrid(x = True, y = True)
        else:
            self.graphWidget.showGrid(x = False, y = False)

    def processChangeLegend(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.legend.show()
        else:
            self.legend.hide()

    def processChangeChartBackground(self):
        dialog = QColorDialog()
        if dialog.exec():
            color = dialog.currentColor()
            self.graphWidget.setBackground(color.name())
            del dialog

    def processChangeBarColor(self):
        dialog = QColorDialog()
        if dialog.exec():
            color = dialog.currentColor()
            self.bargraphItem.opts["brush"] = color.name()
            self.bargraphItem._updateColors(self.bargraphItem.opts)
            del dialog

    def processClose(self):
        self.MainWindow.close()

    def show(self):
        self.MainWindow.show()
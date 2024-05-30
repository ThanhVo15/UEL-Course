from MainWindow import Ui_MainWindow
#Step 1: import pyqtgraph
import pyqtgraph as pg
from PyQt6.QtCore import Qt

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        #Step 2: call pg.PlotWidget()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setTitle("Temperature per hour", color="blue", size="20pt", bold=True, italic=True)
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour(H)", **styles)
        styles_top_right = {"color": "green", "font-size": "15px"}
        self.graphWidget.setLabel("top", "Learn PyQtGraph", **styles_top_right)
        self.graphWidget.setLabel("right", "vominhthanh", **styles_top_right)
        self.graphWidget.setBackground("w")
        self.graphWidget.showGrid(x = True, y = True)

        #Step 3: Create plot data
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
        temperature = [20, 21, 20, 32, 33, 31, 29,31, 32, 35,37, 45]
        temperature2 = [25, 18, 30, 10, 47, 29, 26, 32, 35, 45, 40, 42]
        #Step 4: call plot method
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=Qt.PenStyle.DashLine)
        pen2 = pg.mkPen(color=(0, 0, 255), width=5, style=Qt.PenStyle.SolidLine)
        symbolPen = pg.mkPen(color=(196, 196, 196), width=2)
        symbolPen2 = pg.mkPen(color=(255, 255, 0), width=2)
        self.graphWidget.setXRange(1,8,padding=0)
        self.graphWidget.setYRange(10,80, padding = 0)
        self.graphWidget.addLegend()
        plot1 = self.graphWidget.plot(hour, temperature,name = "Sensor X", pen = pen, symbol = 'o', symbolSize = 10, symbolBrush= ('b'))
        plot2 = self.graphWidget.plot(hour, temperature2, name="Sensor Y",
                              pen=pen2,
                              symbol='d',
                              symbolSize=8,
                              symbolBrush=('r'),
                              symbolPen=symbolPen2)
        plot1.setData(hour, temperature)
        plot2.setData(hour, temperature2)
        #Step 5: add graphWidget into Layout:
        self.myLayout.addWidget(self.graphWidget)

    def show(self):
        self.MainWindow.show()
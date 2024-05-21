import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtCharts import QtCharts


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ứng dụng với biểu đồ PyQt6")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Tạo Biểu Đồ", self)
        self.button.clicked.connect(self.create_chart)
        self.layout.addWidget(self.button)

        self.chart_view = QtCharts.QChartView()
        self.layout.addWidget(self.chart_view)

    def create_chart(self):
        series = QtCharts.QBarSeries()
        data = [("A", random.randint(1, 10)), ("B", random.randint(1, 10)), ("C", random.randint(1, 10)),
                ("D", random.randint(1, 10)), ("E", random.randint(1, 10))]

        for label, value in data:
            barset = QtCharts.QBarSet(label)
            barset.append(value)
            series.append(barset)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Biểu đồ cột")
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)

        categories = [label for label, _ in data]
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, QtCharts.QtAlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        chart.addAxis(axis_y, QtCharts.QtAlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        self.chart_view.setChart(chart)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

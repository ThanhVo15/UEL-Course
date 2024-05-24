# TabSaleEx.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
import pyqtgraph as pg
import pandas as pd
from Test.MainWindow import Ui_MainWindow

class TabSaleEx(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TabSaleEx, self).__init__(parent)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.parent = MainWindow
        # Sử dụng các thành phần giao diện từ MainWindow
        self.layout = self.parent.verticalLayouttest

        # Đảm bảo là layout không rỗng trước khi thêm
        if self.layout:
            self.labelMRR = self.parent.labelMRR
            self.labelNumberOfSales = self.parent.labelMRR_2
            self.plotWidget = self.parent.plotWidget
        # Pyqtgraph PlotWidget
        self.plotWidget = pg.PlotWidget()
        self.layout.addWidget(self.plotWidget)

        # self.setLayout(self.layout)

    def updateSale(self):
        # Truy vấn MRR
        df_mrr = self.parent.databaseConnectEx.connector.queryDataset(
            "SELECT SUM(line_item_amount) AS total_sales FROM sales;")
        if not df_mrr.empty:
            self.labelMRR.setText(f"Monthly Recurring Revenue: {df_mrr.iloc[0]['total_sales']}")

        # Truy vấn số lượng bán hàng
        df_number_of_sales = self.parent.databaseConnectEx.connector.queryDataset(
            "SELECT COUNT(order_id) AS number_of_sales FROM sales;")
        if not df_number_of_sales.empty:
            self.labelMRR_2.setText(f"Total Number of Sales: {df_number_of_sales.iloc[0]['number_of_sales']}")

        # Truy vấn dữ liệu và vẽ biểu đồ
        df_sales_by_date = self.parent.databaseConnectEx.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN dates d ON s.transaction_date = d.transaction_date
            GROUP BY d.Dates_ID
            ORDER BY d.Dates_ID;
        """)
        if not df_sales_by_date.empty:
            self.plotLineChart(df_sales_by_date)

    def plotLineChart(self, df):
        self.plotWidget.clear()
        self.plotWidget.plot(df['Dates_ID'], df['total_line_item_amount'], pen=pg.mkPen(color='b', width=2), symbol='o')
        self.plotWidget.setTitle("Total Sales by Date")
        self.plotWidget.setLabel('left', 'Total Line Item Amount')
        self.plotWidget.setLabel('bottom', 'Date ID')
        self.plotWidget.showGrid(x=True, y=True)

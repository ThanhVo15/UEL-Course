import pyqtgraph as pg
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

class TabSaleEx(QWidget):
    def __init__(self, database_connect_ex, parent_layout):
        super().__init__()
        self.database_connect_ex = database_connect_ex
        self.graphWidget = pg.PlotWidget()
        self.labelMRR = QLabel("MRR")
        self.labelMRR_2 = QLabel("Number of Sales")
        self.setupUI(parent_layout)

    def setupUI(self, layout):
        layout.addWidget(self.labelMRR)
        layout.addWidget(self.labelMRR_2)
        layout.addWidget(self.graphWidget)

    def updateSale(self):
        print("Updating sale information...")
        # Query MRR
        df_mrr = self.database_connect_ex.connector.queryDataset(
            "SELECT SUM(line_item_amount) AS total_sales FROM sales;")
        if not df_mrr.empty:
            self.labelMRR.setText(f"Total Sales (MRR): {df_mrr.iloc[0]['total_sales']}")
            print(f"Total Sales (MRR): {df_mrr.iloc[0]['total_sales']}")

        # Query number of sales
        df_number_of_sales = self.database_connect_ex.connector.queryDataset(
            "SELECT COUNT(order_id) AS number_of_sales FROM sales;")
        if not df_number_of_sales.empty:
            self.labelMRR_2.setText(f"Number of Sales: {df_number_of_sales.iloc[0]['number_of_sales']}")
            print(f"Number of Sales: {df_number_of_sales.iloc[0]['number_of_sales']}")

        # Query data and plot the chart
        df_sales_by_date = self.database_connect_ex.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN dates d ON s.transaction_date = d.transaction_date
            GROUP BY d.Dates_ID
            ORDER BY d.Dates_ID;
        """)
        if not df_sales_by_date.empty:
            print(f"Sales by Date Data: {df_sales_by_date}")
            self.plotLineChart(df_sales_by_date)
        else:
            print("No data fetched for sales by date.")

    def plotLineChart(self, df):
        print("Plotting line chart...")
        self.graphWidget.clear()  # Clear the plot to avoid duplicates

        # Configure the graph
        self.graphWidget.setTitle("Total Sales by Date", color="r", size="15pt", bold=True, italic=True)
        self.graphWidget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        self.graphWidget.setLabel("left", "Total Line Item Amount", **labelStyle)
        self.graphWidget.setLabel("bottom", "Date ID", **labelStyle)
        self.graphWidget.showGrid(x=True, y=True)

        # Plot the line graph
        print(f"Dates_ID: {df['Dates_ID'].tolist()}, Total_Line_Item_Amount: {df['total_line_item_amount'].tolist()}")
        self.linegraph = self.graphWidget.plot(df['Dates_ID'].tolist(), df['total_line_item_amount'].tolist(), pen=pg.mkPen(color='b', width=2), symbol='o')
        print("Line chart plotted.")

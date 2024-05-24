
    def updateSale(self):
        # Truy vấn MRR
        df_mrr = self.databaseConnectEx.connector.queryDataset(
            "SELECT SUM(line_item_amount) AS total_sales FROM sales;")
        if not df_mrr.empty:
            self.labelMRR.setText(f"{df_mrr.iloc[0]['total_sales']}")

        # Truy vấn số lượng bán hàng
        df_number_of_sales = self.databaseConnectEx.connector.queryDataset(
            "SELECT COUNT(order_id) AS number_of_sales FROM sales;")
        if not df_number_of_sales.empty:
            self.labelMRR_2.setText(f"{df_number_of_sales.iloc[0]['number_of_sales']}")

        # Truy vấn dữ liệu và vẽ biểu đồ
        df_sales_by_date = self.databaseConnectEx.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN dates d ON s.transaction_date = d.transaction_date
            GROUP BY d.Dates_ID
            ORDER BY d.Dates_ID;
        """)
        if not df_sales_by_date.empty:
            self.plotLineChart(df_sales_by_date)

    def plotLineChart(self, df):
        self.graphWidget.clear()

        # Configure the graph
        self.graphWidget.setTitle("Total Sales by Date", color="r", size="15pt", bold=True, italic=True)
        self.graphWidget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        self.graphWidget.setLabel("left", "Total Line Item Amount", **labelStyle)
        self.graphWidget.setLabel("bottom", "Date ID", **labelStyle)
        self.graphWidget.showGrid(x=True, y=True)

        # Plot the line graph
        self.linegraph = self.graphWidget.plot(df['Dates_ID'], df['total_line_item_amount'], pen=pg.mkPen(color='b', width=2), symbol='o')

        # Add the plot to the graph widget
        self.graphWidget.addItem(self.linegraph)

        # Add the graph widget to the layout
        self.verticalLayouttest.addWidget(self.graphWidget)
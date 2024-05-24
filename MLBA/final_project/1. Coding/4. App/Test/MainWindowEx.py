from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu, QFileDialog, QLineEdit, QPushButton, QTabWidget
from PyQt6.QtGui import QIcon, QColor
from PyQt6 import QtCore
from PyQt6.QtCore import QModelIndex, Qt, QAbstractTableModel, pyqtSlot
from Test.MainWindow import Ui_MainWindow
from Test.DatabaseConnectionsEx import DatabaseConnectEx
from functools import partial
from enum import Enum
import mysql.connector
import csv
from ConnectionsScreen.Connectors import Connector
import pyqtgraph as pg
import pandas as pd

class TableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self.data = data
        self.columns = columns
        self.batch_size = 10  # số lượng dữ liệu sẽ fetch thêm mỗi lần
        self.fetched_rows = self.batch_size

    def data(self, index, role):
        value = self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            return value
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 1 and value == "":
                return QColor(Qt.GlobalColor.yellow)
        if role == Qt.ItemDataRole.ForegroundRole:
            if index.column() == 2 and value != "" and float(value) < 100:
                return QColor(Qt.GlobalColor.red)

    def rowCount(self, index):
        return min(self.fetched_rows, len(self.data))

    def columnCount(self, index):
        return len(self.columns)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(section + 1)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled

        return super().flags(index) | Qt.ItemFlag.ItemIsEditable  # add editable flag.

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # Set the value into the frame.
            self.data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def insertRows(self, row, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), row, row + rows - 1)
        for _ in range(rows):
            self.data.insert(row, [""] * self.columnCount(index))
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        del self.data[row:row + rows]
        self.endRemoveRows()
        return True

    def canFetchMore(self, index):
        return self.fetched_rows < len(self.data)

    def fetchMore(self, index):
        remaining_rows = len(self.data) - self.fetched_rows
        fetch_rows = min(remaining_rows, self.batch_size)
        self.beginInsertRows(QModelIndex(), self.fetched_rows, self.fetched_rows + fetch_rows - 1)
        self.fetched_rows += fetch_rows
        self.endInsertRows()

class InsertBehavior(Enum):
    INSERT_FIRST = 0
    INSERT_LAST = 1
    INSERT_ABOVE = 2
    INSERT_BELOW = 3

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)
        self.databaseConnectEx = DatabaseConnectEx(self)
        self.connector = Connector()
        self.graphWidget = pg.PlotWidget()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.pushButtonConnectDatabase.clicked.connect(self.openDatabaseConnectUI)
        self.actionConnect_to_Database.triggered.connect(self.openDatabaseConnectUI)
        self.actionExport_CSV.triggered.connect(self.exportToCSV)

        self.comboBoxChooseTable.currentIndexChanged.connect(self.tableSelectionChanged)
        self.pushButtonExecuteQuerry.clicked.connect(self.executeQuery)

        self.pushButtonFetchMore.clicked.connect(self.processFetchMore)  # Kết nối nút Fetch More

        self.tableViewShow.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableViewShow.customContextMenuRequested.connect(self.onCustomContextMenuRequested)

        self.tabWidget.currentChanged.connect(self.onTabChanged)

    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()

    def updateLineEdit(self, database_name):
        self.lineEdit.setText(f"SQL_Workbench/{database_name}")

    def updateComboBox(self, tables):
        self.comboBoxChooseTable.clear()
        self.comboBoxChooseTable.addItems(tables)
        self.comboBoxChooseTable.setCurrentIndex(0)

    def tableSelectionChanged(self):
        selected_table = self.comboBoxChooseTable.currentText()
        if selected_table:
            self.databaseConnectEx.showTableData(selected_table)
            self.lineEditquery.setText(f"SELECT * FROM {selected_table};")  # Cập nhật query mặc định

    def executeQuery(self):
        query = self.lineEditquery.text()
        try:
            df = self.databaseConnectEx.connector.queryDataset(query)
            if df is not None and not df.empty:
                model = TableModel(df.values.tolist(), df.columns.tolist())
                self.tableViewShow.setModel(model)
            else:
                raise Exception("Query returned no data")
        except mysql.connector.Error as err:
            self.showErrorDialog("Query Error", f"Invalid query syntax or execution error:\n{str(err)}")
        except Exception as e:
            self.showErrorDialog("Query Error", str(e))

    def showErrorDialog(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def onCustomContextMenuRequested(self, pos):
        index = self.tableViewShow.indexAt(pos)
        menu = QMenu()
        if index.isValid():
            insertFirst = menu.addAction("Insert &First")
            insertFirst.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert top.png"))
            insertLast = menu.addAction("Insert &Last")
            insertLast.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert last.png"))
            insertAbove = menu.addAction("Insert &Above")
            insertAbove.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert above.png"))
            insertBelow = menu.addAction("Insert &Below")
            insertBelow.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_insert below.png"))
            removeSelected = menu.addAction("Remove selected row")
            removeSelected.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_delete.png"))

            menu.addAction(insertFirst)
            menu.addAction(insertLast)
            menu.addAction(insertAbove)
            menu.addAction(insertBelow)
            menu.addSeparator()
            menu.addAction(removeSelected)

            insertFirst.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_FIRST))
            insertLast.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_LAST))
            insertAbove.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_ABOVE))
            insertBelow.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_BELOW))
            removeSelected.triggered.connect(self.processDelete)
            menu.exec(self.tableViewShow.viewport().mapToGlobal(pos))
        else:
            insertNew = menu.addAction("Insert New Record")
            insertNew.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\0. Icon\ic_new.png"))
            insertNew.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_FIRST))
            menu.addAction(insertNew)
            menu.exec(self.tableViewShow.viewport().mapToGlobal(pos))

    def processInsert(self, behavior=InsertBehavior.INSERT_FIRST):
        indexes = self.tableViewShow.selectionModel().selectedIndexes()
        if behavior == InsertBehavior.INSERT_FIRST:
            row = 0
        elif behavior == InsertBehavior.INSERT_LAST:
            row = self.tableViewShow.model().rowCount(QModelIndex())
        else:
            if indexes:
                index = indexes[0]
                row = index.row()
                if behavior == InsertBehavior.INSERT_ABOVE:
                    row = max(row, 0)
                else:
                    size = self.tableViewShow.model().rowCount(QModelIndex())
                    row = min(row + 1, size)
        self.tableViewShow.model().insertRows(row, 1, QModelIndex())

    def processDelete(self):
        indexes = self.tableViewShow.selectionModel().selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            self.tableViewShow.model().removeRows(row, 1, QModelIndex())

    def processFetchMore(self):
        model = self.tableViewShow.model()
        if hasattr(model, 'canFetchMore') and model.canFetchMore(QModelIndex()):
            model.fetchMore(QModelIndex())
        else:
            msg = QMessageBox()
            msg.setText("No more records to fetch")
            msg.exec()

    def exportToCSV(self):
        model = self.tableViewShow.model()
        if model is None:
            self.showErrorDialog("Export Error", "No data available to export")
            return

        # Get the path to save the file
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if not filePath:
            return

        # Save the data to the CSV file
        try:
            with open(filePath, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                headers = [model.headerData(i, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole) for i in range(model.columnCount(QModelIndex()))]
                writer.writerow(headers)
                # Write data
                for row in range(model.rowCount(QModelIndex())):
                    rowData = [model.data(model.index(row, col), Qt.ItemDataRole.DisplayRole) for col in range(model.columnCount(QModelIndex()))]
                    writer.writerow(rowData)
            QMessageBox.information(self, "Export Successful", f"Data successfully exported to {filePath}")
        except Exception as e:
            self.showErrorDialog("Export Error", f"Failed to export data: {str(e)}")







    # Dashboard

    ## Navigation Bar
    def onTabChanged(self, index):
        if self.tabWidget.tabText(index) == "Sale":
            self.updateSale()
        if self.tabWidget.tabText(index) == "Customer":
            self.updateCustomer()
        if self.tabWidget.tabText(index) == "Inventory":
            self.updateInventory()

    ## Tab Sale
    def updateSale(self):
        # Truy vấn MRR
        df_mrr = self.databaseConnectEx.connector.queryDataset(
            "SELECT SUM(line_item_amount) AS total_sales FROM sales;"
        )
        if not df_mrr.empty:
            total_sales = df_mrr.iloc[0]['total_sales']
            formatted_total_sales = f"{total_sales:,.2f}"  # Format with commas and two decimal places
            self.labelMRR.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_total_sales}</span>")

        # Truy vấn số lượng bán hàng
        df_number_of_sales = self.databaseConnectEx.connector.queryDataset(
            "SELECT COUNT(order_id) AS number_of_sales FROM sales;"
        )
        if not df_number_of_sales.empty:
            number_of_sales = df_number_of_sales.iloc[0]['number_of_sales']
            formatted_number_of_sales = f"{number_of_sales:,}"  # Format with commas
            self.labelNumberofSales.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_number_of_sales}</span>")

        # Fetch data for Total Sales by Dates
        df_sales_by_date = self.databaseConnectEx.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN dates d ON s.transaction_date = d.transaction_date
            GROUP BY d.Dates_ID
            ORDER BY d.Dates_ID;
        """)
        if not df_sales_by_date.empty:
            self.chartverticalLayoutTotalSalesbyDates(df_sales_by_date)
        else:
            print("No data available for Total Sales by Dates.")

        # verticalLayoutSalesGrowthRateByPartOfTheDays
        df_verticalLayoutSalesGrowthRateByPartOfTheDays = self.databaseConnectEx.connector.queryDataset("""
            SELECT s.transaction_date, t.part_of_day, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN transaction_times t ON t.transaction_time = s.transaction_time
            GROUP BY s.transaction_date, t.part_of_day
            ORDER BY s.transaction_date,
            FIELD(t.part_of_day, 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night');
        """)
        if not df_verticalLayoutSalesGrowthRateByPartOfTheDays.empty:
            self.chartverticalLayoutSalesGrowthRateByPartOfTheDays(df_verticalLayoutSalesGrowthRateByPartOfTheDays)

        # verticalLayoutDrinkHereOrGo
        df_verticalLayoutDrinkHereOrGo = self.databaseConnectEx.connector.queryDataset("""
            SELECT s.sales_outlet_id, SUM(s.line_item_amount) AS total_amount,
                SUM(s.quantity) AS total_quantity,
                s.instore_yn
            FROM sales s
            JOIN dates d ON d.transaction_date = s.transaction_date
            GROUP BY s.sales_outlet_id, s.instore_yn, d.Dates_ID
            ORDER BY d.Dates_ID;
        """)
        if not df_verticalLayoutDrinkHereOrGo.empty:
            self.verticalLayoutDrinkHereOrGo(df_verticalLayoutDrinkHereOrGo)

        # verticalLayoutSalesGrowthRatebyWeek
        df_verticalLayoutSalesGrowthRatebyWeek = self.databaseConnectEx.connector.queryDataset("""
            WITH weekly_sales AS (
                SELECT d.Week_ID AS week, SUM(s.line_item_amount) AS total_line_item_amount
                FROM sales s
                JOIN dates d ON s.transaction_date = d.transaction_date
                WHERE d.Week_ID NOT IN (18)  -- Exclude week 18
                GROUP BY d.Week_ID
            )
            SELECT week, total_line_item_amount,
                COALESCE(
                    (total_line_item_amount - LAG(total_line_item_amount) OVER (ORDER BY week)) / LAG(total_line_item_amount) OVER (ORDER BY week) * 100,
                    0
                ) AS sales_growth_rate
            FROM weekly_sales
            ORDER BY week;
        """)
        if not df_verticalLayoutSalesGrowthRatebyWeek.empty:
            self.verticalLayoutSalesGrowthRatebyWeek(df_verticalLayoutSalesGrowthRatebyWeek)

        # verticalLayoutFromWhichStore
        df_verticalLayoutFromWhichStore = self.databaseConnectEx.connector.queryDataset("""
            SELECT s.sales_outlet_id, SUM(s.line_item_amount) AS total_amount, SUM(s.quantity) as total_quantity
            FROM sales s
            GROUP BY s.sales_outlet_id
            ORDER BY FIELD(s.sales_outlet_id, '3', '5', '8');
        """)
        if not df_verticalLayoutFromWhichStore.empty:
            self.verticalLayoutFromWhichStore(df_verticalLayoutFromWhichStore)

    def chartverticalLayoutTotalSalesbyDates(self, df):
        self.graphWidget.clear()

        # Configure the graph
        self.graphWidget.setTitle("Total Sales by Date", color="r", size="15pt", bold=True, italic=True)
        self.graphWidget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        self.graphWidget.setLabel("left", "Total Line Item Amount", **labelStyle)
        self.graphWidget.setLabel("bottom", "Date ID", **labelStyle)
        self.graphWidget.showGrid(x=True, y=True)

        # Plot the line graph
        self.linegraph = self.graphWidget.plot(
            df['Dates_ID'], df['total_line_item_amount'],
            pen=pg.mkPen(color='b', width=2), symbol='o'
        )

        # Add the plot to the graph widget
        self.graphWidget.addItem(self.linegraph)

        # Add the graph widget to the layout
        self.verticalLayoutTotalSalesbyDates.addWidget(self.graphWidget)

    def chartverticalLayoutSalesGrowthRateByPartOfTheDays(self, df):
        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Sales Growth Rate by Part of the Days", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Line Item Amount", **labelStyle)
        plot_widget.setLabel("bottom", "Date", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Convert transaction_date to datetime for sorting
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])

        # Sort the dataframe by date
        df.sort_values('transaction_date', inplace=True)

        # Define parts of the day in order
        parts_of_day = ['Morning', 'Afternoon', 'Evening', 'Night', 'Late Night']

        # Generate a color map for the parts of the day
        color_map = {
            'Morning': 'r',
            'Afternoon': 'g',
            'Evening': 'b',
            'Night': 'c',
            'Late Night': 'm'
        }

        # Plot each part of the day
        for part in parts_of_day:
            part_df = df[df['part_of_day'] == part]
            if not part_df.empty:
                plot_widget.plot(part_df['transaction_date'].values, part_df['total_line_item_amount'].values,
                                 pen=pg.mkPen(color=color_map[part], width=2), symbol='o', symbolBrush=color_map[part],
                                 name=part)

        # Add legend
        plot_widget.addLegend()

        # Add the plot widget to the layout
        self.verticalLayoutSalesGrowthRateByPartOfTheDays.addWidget(plot_widget)





    ## Tab Customer
    def updateCustomer(self):
        # Truy vấn labelNewCustomer
        df_labelNewCustomer = self.databaseConnectEx.connector.queryDataset("""
            SELECT COUNT(DISTINCT c.customer_id) AS new_customers
            FROM customer c
            JOIN sales s ON c.customer_since = s.transaction_date;
        """)
        if not df_labelNewCustomer.empty:
            new_customers = df_labelNewCustomer.iloc[0]['new_customers']
            formatted_new_customers = f"{new_customers:,}"  # Format with commas
            self.labelNewCustomer.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_new_customers}</span>")

        # Truy vấn labelChurnRate
        df_labelChurnRate = self.databaseConnectEx.connector.queryDataset("""
            SELECT (inactive_data.inactive_customers / total_data.total_customers) * 100 AS churn_rate
            FROM (
                SELECT COUNT(DISTINCT c.customer_id) AS inactive_customers
                FROM customer c
                LEFT JOIN sales s ON c.customer_id = s.customer_id AND s.transaction_date BETWEEN '2019-04-01' AND '2019-04-30'
                WHERE s.customer_id IS NULL AND c.customer_since <= '2019-03-31'
            ) AS inactive_data,
            (SELECT COUNT(*) AS total_customers FROM customer WHERE customer_since <= '2019-03-31') AS total_data;
        """)
        if not df_labelChurnRate.empty:
            churn_rate = df_labelChurnRate.iloc[0]['churn_rate']
            formatted_churn_rate = f"{churn_rate:.2f}%"  # Format with two decimal places and percent sign
            self.labelChurnRate.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_churn_rate}</span>")

        # verticalLayoutPurchasebyGender
        df_verticalLayoutPurchasebyGender = self.databaseConnectEx.connector.queryDataset("""
            SELECT c.gender, COUNT(DISTINCT s.customer_id) AS purchase_count
            FROM customer c
            JOIN sales s ON c.customer_id = s.customer_id
            GROUP BY c.gender;
        """)
        if not df_verticalLayoutPurchasebyGender.empty:
            self.verticalLayoutPurchasebyGender(df_verticalLayoutPurchasebyGender)

        # verticalLayoutPurchasebyAgeGroup
        df_verticalLayoutPurchasebyAgeGroup = self.databaseConnectEx.connector.queryDataset("""
            SELECT 
                CASE 
                    WHEN YEAR(s.transaction_date) - c.birth_year < 20 THEN '<20'
                    WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 20 AND 29 THEN '20-29'
                    WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 30 AND 39 THEN '30-39'
                    WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 40 AND 49 THEN '40-49'
                    ELSE '50+'
                END AS age_group,
                SUM(s.line_item_amount) AS total_revenue
            FROM customer c
            JOIN sales s ON c.customer_id = s.customer_id
            GROUP BY age_group;
        """)
        if not df_verticalLayoutPurchasebyAgeGroup.empty:
            self.verticalLayoutPurchasebyAgeGroup(df_verticalLayoutPurchasebyAgeGroup)

        # verticalLayoutPurchasebyGenderandbyProductCategory
        df_verticalLayoutPurchasebyGenderandbyProductCategory = self.databaseConnectEx.connector.queryDataset("""
            SELECT c.gender, p.product_category, COUNT(s.line_item_amount) AS purchase_count
            FROM customer c
            JOIN sales s ON c.customer_id = s.customer_id
            JOIN product p ON s.product_id = p.product_id
            GROUP BY c.gender, p.product_category;
        """)
        if not df_verticalLayoutPurchasebyGenderandbyProductCategory.empty:
            self.verticalLayoutPurchasebyGenderandbyProductCategory(
                df_verticalLayoutPurchasebyGenderandbyProductCategory)

        # verticalLayoutRFM
        df_verticalLayoutRFM = self.databaseConnectEx.connector.queryDataset("""
            WITH rfm AS (
                SELECT c.customer_id, MAX(s.transaction_date) AS last_purchase_date, COUNT(s.line_item_id) AS frequency,
                    SUM(s.line_item_amount) AS monetary_value, DATEDIFF('2019-05-01', MAX(s.transaction_date)) AS recency, c.gender
                FROM customer c
                JOIN sales s ON c.customer_id = s.customer_id
                GROUP BY c.customer_id
            )
            SELECT customer_id, recency, frequency, monetary_value, gender
            FROM rfm;
        """)
        if not df_verticalLayoutRFM.empty:
            self.verticalLayoutRFM(df_verticalLayoutRFM)






    ## Tab Inventory
    def updateInventory(self):
        # Truy vấn labelTotalPurchase
        df_labelTotalPurchase = self.databaseConnectEx.connector.queryDataset("""
            SELECT SUM(pi.quantity_sold * p.current_wholesale_price) as total_amount_purchase
            FROM pastry_inventory pi
            JOIN product p ON p.product_id = pi.product_id;
        """)
        if not df_labelTotalPurchase.empty:
            total_amount_purchase = df_labelTotalPurchase.iloc[0]['total_amount_purchase']
            formatted_total_amount_purchase = f"{total_amount_purchase:,.2f}"  # Format with commas and two decimal places
            self.labelTotalPurchase.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_total_amount_purchase}</span>")

        # Truy vấn labelTotalSale
        df_labelTotalSale = self.databaseConnectEx.connector.queryDataset("""
            SELECT SUM(pi.quantity_sold * p.current_retail_price) as total_amount_sale
            FROM pastry_inventory pi
            JOIN product p ON p.product_id = pi.product_id;
        """)
        if not df_labelTotalSale.empty:
            total_amount_sale = df_labelTotalSale.iloc[0]['total_amount_sale']
            formatted_total_amount_sale = f"{total_amount_sale:,.2f}"  # Format with commas and two decimal places
            self.labelTotalSale.setText(
                f"<b></b><br><span style='font-size:18px; color:red; font-weight:bold'>{formatted_total_amount_sale}</span>")

        # verticalLayoutQuantitySold
        df_verticalLayoutQuantitySold = self.databaseConnectEx.connector.queryDataset("""
            SELECT d.Month_ID, pi.sales_outlet_id, pi.product_id, SUM(pi.quantity_sold) AS Total_quantity_sold
            FROM pastry_inventory pi
            JOIN dates d ON pi.transaction_date = d.transaction_date
            GROUP BY pi.product_id, d.Month_ID, pi.sales_outlet_id
            ORDER BY d.Month_ID;
        """)
        if not df_verticalLayoutQuantitySold.empty:
            self.verticalLayoutQuantitySold(df_verticalLayoutQuantitySold)

        # verticalLayoutPercentWaste
        df_verticalLayoutPercentWaste = self.databaseConnectEx.connector.queryDataset("""
            SELECT pi.sales_outlet_id, pi.product_id, SUM(pi.quantity_sold)/COUNT(d.Dates_ID) AS Total_Percen_Waste
            FROM pastry_inventory pi
            JOIN dates d ON pi.transaction_date = d.transaction_date
            GROUP BY pi.product_id, d.Month_ID, pi.sales_outlet_id
            ORDER BY d.Month_ID;
        """)
        if not df_verticalLayoutPercentWaste.empty:
            self.verticalLayoutPercentWaste(df_verticalLayoutPercentWaste)

        # verticalLayoutTotalInventorySoldByDay
        df_verticalLayoutTotalInventorySoldByDay = self.databaseConnectEx.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(pi.quantity_sold) as total_quantity_sold, pi.sales_outlet_id
            FROM pastry_inventory pi
            JOIN dates d ON d.transaction_date = pi.transaction_date
            GROUP BY d.Dates_ID, pi.sales_outlet_id
            ORDER BY d.Dates_ID;
        """)
        if not df_verticalLayoutTotalInventorySoldByDay.empty:
            self.verticalLayoutTotalInventorySoldByDay(df_verticalLayoutTotalInventorySoldByDay)

        # verticalLayoutSaleTarget
        df_verticalLayoutSaleTarget = self.databaseConnectEx.connector.queryDataset("""
            SELECT pi.sales_outlet_id, st.total_goal, SUM(pi.quantity_sold) AS total_quantity_sold,
                (SUM(pi.quantity_sold)/st.total_goal)*100 as percent
            FROM pastry_inventory pi
            JOIN product pr ON pi.product_id = pr.product_id
            JOIN sales_targets st ON pi.sales_outlet_id = st.sales_outlet_id
            GROUP BY pi.sales_outlet_id, st.total_goal;
        """)
        if not df_verticalLayoutSaleTarget.empty:
            self.verticalLayoutSaleTarget(df_verticalLayoutSaleTarget)

    def show(self):
        self.MainWindow.show()





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
import pyqtgraph.opengl as gl
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

    def clear(self):
        self.axes.clear()

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
            SELECT d.Dates_ID, t.part_of_day, SUM(s.line_item_amount) AS total_line_item_amount
            FROM sales s
            JOIN transaction_times t ON t.transaction_time = s.transaction_time
            JOIN dates d ON d.transaction_date = s.transaction_date
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
            self.chartverticalLayoutDrinkHereOrGo(df_verticalLayoutDrinkHereOrGo)

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
            self.chartverticalLayoutSalesGrowthRatebyWeek(df_verticalLayoutSalesGrowthRatebyWeek)

        # verticalLayoutFromWhichStore
        df_verticalLayoutFromWhichStore = self.databaseConnectEx.connector.queryDataset("""
            SELECT s.sales_outlet_id, SUM(s.line_item_amount) AS total_amount, SUM(s.quantity) as total_quantity
            FROM sales s
            GROUP BY s.sales_outlet_id
            ORDER BY FIELD(s.sales_outlet_id, '3', '5', '8');
        """)
        if not df_verticalLayoutFromWhichStore.empty:
            self.chartverticalLayoutFromWhichStore(df_verticalLayoutFromWhichStore)

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
        plot_widget.setTitle("Sales Growth Rate by Part of the Day", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Line Item Amount", **labelStyle)
        plot_widget.setLabel("bottom", "Date ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        parts_of_day = df['part_of_day'].unique()
        colors = ['b', 'g', 'r', 'c', 'm']  # Different colors for different parts of the day

        # Add a legend to the plot
        legend = plot_widget.addLegend()

        # Add plots for each part of the day
        for i, part in enumerate(parts_of_day):
            part_df = df[df['part_of_day'] == part]
            plot = plot_widget.plot(part_df['Dates_ID'].values, part_df['total_line_item_amount'].values,
                                    pen=pg.mkPen(color=colors[i % len(colors)], width=2), symbol='o', name=part)

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutSalesGrowthRateByPartOfTheDays.count())):
            self.verticalLayoutSalesGrowthRateByPartOfTheDays.itemAt(i).widget().setParent(None)

        self.verticalLayoutSalesGrowthRateByPartOfTheDays.addWidget(plot_widget)

    def chartverticalLayoutDrinkHereOrGo(self, df):
        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Sales: Drink Here or Go", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Amount", **labelStyle)
        plot_widget.setLabel("bottom", "Sales Outlet ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract unique sales outlets and in-store flags
        sales_outlets = df['sales_outlet_id'].unique()
        instore_flags = df['instore_yn'].unique()

        # Set bar width and positions
        bar_width = 0.3
        x = np.arange(len(sales_outlets))

        # Dictionary to store bars for the legend
        bars = {}

        for i, instore in enumerate(instore_flags):
            instore_df = df[df['instore_yn'] == instore]
            bar_data = [
                instore_df[instore_df['sales_outlet_id'] == outlet]['total_amount'].values[0] if outlet in instore_df[
                    'sales_outlet_id'].values else 0 for outlet in sales_outlets]
            bar = pg.BarGraphItem(x=x + i * bar_width, height=bar_data, width=bar_width,
                                  brush=('b' if instore == 1 else 'r'))
            plot_widget.addItem(bar)
            bars["In-store" if instore == 1 else "Take-away"] = bar

            # Add text items to show the total amount on top of each bar
            for j, value in enumerate(bar_data):
                text = pg.TextItem(text=f"{value}", anchor=(0.5, -0.5), color='k', border='w', fill=pg.mkBrush('w'))
                text.setPos(x[j] + i * bar_width + bar_width / 2, value)
                plot_widget.addItem(text)

        # Add a legend
        legend = plot_widget.addLegend()
        for name, bar in bars.items():
            legend.addItem(bar, name)

        # Set x-axis ticks to show sales outlet IDs
        x_ticks = [(i, str(sales_outlet)) for i, sales_outlet in enumerate(sales_outlets)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutDrinkHereOrGo.count())):
            self.verticalLayoutDrinkHereOrGo.itemAt(i).widget().setParent(None)

        self.verticalLayoutDrinkHereOrGo.addWidget(plot_widget)

    def chartverticalLayoutSalesGrowthRatebyWeek(self, df):
        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Sales Growth Rate by Week", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Line Item Amount", **labelStyle)
        plot_widget.setLabel("bottom", "Week", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        weeks = df['week']
        total_line_item_amount = df['total_line_item_amount']
        sales_growth_rate = df['sales_growth_rate']

        # Create the bar chart for total_line_item_amount
        bar_width = 0.4
        bar_chart = pg.BarGraphItem(x=weeks, height=total_line_item_amount, width=bar_width, brush='b')

        # Add the bar chart to the plot
        plot_widget.addItem(bar_chart)

        # Create the line chart for sales_growth_rate
        line_chart = pg.PlotDataItem(weeks, total_line_item_amount * (1 + sales_growth_rate / 100),
                                     pen=pg.mkPen(color='r', width=2), symbol='o')

        # Add the line chart to the plot
        plot_widget.addItem(line_chart)

        # Add a legend
        legend = plot_widget.addLegend()
        legend.addItem(bar_chart, 'Total Line Item Amount')
        legend.addItem(line_chart, 'Sales Growth Rate')

        # Set x-axis ticks to show integer weeks
        plot_widget.getAxis('bottom').setTicks([[(int(week), str(int(week))) for week in weeks]])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutSalesGrowthRatebyWeek.count())):
            self.verticalLayoutSalesGrowthRatebyWeek.itemAt(i).widget().setParent(None)

        self.verticalLayoutSalesGrowthRatebyWeek.addWidget(plot_widget)

    def chartverticalLayoutFromWhichStore(self, df):
        # Ensure the data types are correct
        df['sales_outlet_id'] = df['sales_outlet_id'].astype(str)
        df['total_amount'] = df['total_amount'].astype(float)
        df['total_quantity'] = df['total_quantity'].astype(float)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Sales from Each Store", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total", **labelStyle)
        plot_widget.setLabel("bottom", "Sales Outlet ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        sales_outlets = df['sales_outlet_id']
        total_amount = df['total_amount']
        total_quantity = df['total_quantity']

        # Set bar width and positions
        bar_width = 0.3
        x = np.arange(len(sales_outlets))

        # Create the bar chart for total_amount
        amount_bar = pg.BarGraphItem(x=x - bar_width / 2, height=total_amount, width=bar_width, brush='b',
                                     name='Total Amount')

        # Create the bar chart for total_quantity
        quantity_bar = pg.BarGraphItem(x=x + bar_width / 2, height=total_quantity, width=bar_width, brush='g',
                                       name='Total Quantity')

        # Add the bar charts to the plot
        plot_widget.addItem(amount_bar)
        plot_widget.addItem(quantity_bar)

        # Add a legend
        legend = plot_widget.addLegend()
        legend.addItem(amount_bar, 'Total Amount')
        legend.addItem(quantity_bar, 'Total Quantity')

        # Set x-axis ticks to show sales outlet IDs
        x_ticks = [(i, sales_outlet) for i, sales_outlet in enumerate(sales_outlets)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutFromWhichStore.count())):
            self.verticalLayoutFromWhichStore.itemAt(i).widget().setParent(None)

        self.verticalLayoutFromWhichStore.addWidget(plot_widget)






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
            self.chartverticalLayoutPurchasebyGender(df_verticalLayoutPurchasebyGender)

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
            self.chartverticalLayoutPurchasebyAgeGroup(df_verticalLayoutPurchasebyAgeGroup)

        # verticalLayoutPurchasebyGenderandbyProductCategory
        df_verticalLayoutPurchasebyGenderandbyProductCategory = self.databaseConnectEx.connector.queryDataset("""
            SELECT c.gender, p.product_category, COUNT(s.line_item_amount) AS purchase_count
            FROM customer c
            JOIN sales s ON c.customer_id = s.customer_id
            JOIN product p ON s.product_id = p.product_id
            GROUP BY c.gender, p.product_category;
        """)
        if not df_verticalLayoutPurchasebyGenderandbyProductCategory.empty:
            self.chartverticalLayoutPurchasebyGenderandbyProductCategory(
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
            self.chartverticalLayoutRFM(df_verticalLayoutRFM)

    def chartverticalLayoutPurchasebyGender(self, df):
        # Ensure the data types are correct
        df['gender'] = df['gender'].astype(str)
        df['purchase_count'] = df['purchase_count'].astype(int)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Purchases by Gender", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Purchase Count", **labelStyle)
        plot_widget.setLabel("bottom", "Gender", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        genders = df['gender']
        purchase_count = df['purchase_count']

        # Set bar width and positions
        bar_width = 0.5
        x = np.arange(len(genders))

        # Create the bar chart for purchase_count
        bar_chart = pg.BarGraphItem(x=x, height=purchase_count, width=bar_width, brush='b')

        # Add the bar chart to the plot
        plot_widget.addItem(bar_chart)

        # Set x-axis ticks to show gender
        x_ticks = [(i, gender) for i, gender in enumerate(genders)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutPurchasebyGender.count())):
            self.verticalLayoutPurchasebyGender.itemAt(i).widget().setParent(None)

        self.verticalLayoutPurchasebyGender.addWidget(plot_widget)

    def chartverticalLayoutPurchasebyAgeGroup(self, df):
        # Ensure the data types are correct
        df['age_group'] = df['age_group'].astype(str)
        df['total_revenue'] = df['total_revenue'].astype(float)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Purchases by Age Group", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Revenue", **labelStyle)
        plot_widget.setLabel("bottom", "Age Group", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        age_groups = df['age_group']
        total_revenue = df['total_revenue']

        # Set bar width and positions
        bar_width = 0.5
        x = np.arange(len(age_groups))

        # Create the bar chart for total_revenue
        bar_chart = pg.BarGraphItem(x=x, height=total_revenue, width=bar_width, brush='b')

        # Add the bar chart to the plot
        plot_widget.addItem(bar_chart)

        # Set x-axis ticks to show age groups
        x_ticks = [(i, age_group) for i, age_group in enumerate(age_groups)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutPurchasebyAgeGroup.count())):
            self.verticalLayoutPurchasebyAgeGroup.itemAt(i).widget().setParent(None)

        self.verticalLayoutPurchasebyAgeGroup.addWidget(plot_widget)

    def chartverticalLayoutPurchasebyGenderandbyProductCategory(self, df):
        # Ensure the data types are correct
        df['gender'] = df['gender'].astype(str)
        df['product_category'] = df['product_category'].astype(str)
        df['purchase_count'] = df['purchase_count'].astype(int)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Purchases by Gender and Product Category", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Purchase Count", **labelStyle)
        plot_widget.setLabel("bottom", "Product Category", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        product_categories = df['product_category'].unique()
        genders = df['gender'].unique()

        # Set bar width and positions
        bar_width = 0.3
        x = np.arange(len(product_categories))

        # Dictionary to store bars for the legend
        bars = {}

        for i, gender in enumerate(genders):
            gender_df = df[df['gender'] == gender]
            bar_data = [gender_df[gender_df['product_category'] == category]['purchase_count'].values[0] if category in
                                                                                                            gender_df[
                                                                                                                'product_category'].values else 0
                        for category in product_categories]
            bar = pg.BarGraphItem(x=x + i * bar_width, height=bar_data, width=bar_width, brush=pg.intColor(i),
                                  name=gender)
            plot_widget.addItem(bar)
            bars[gender] = bar

        # Add a legend
        legend = plot_widget.addLegend()
        for name, bar in bars.items():
            legend.addItem(bar, name)

        # Set x-axis ticks to show product categories
        x_ticks = [(i, category) for i, category in enumerate(product_categories)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutPurchasebyGenderandbyProductCategory.count())):
            self.verticalLayoutPurchasebyGenderandbyProductCategory.itemAt(i).widget().setParent(None)

        self.verticalLayoutPurchasebyGenderandbyProductCategory.addWidget(plot_widget)

    def chartverticalLayoutRFM(self, df):
        # Ensure the data types are correct
        df['recency'] = df['recency'].astype(float)
        df['frequency'] = df['frequency'].astype(float)
        df['monetary_value'] = df['monetary_value'].astype(float)

        # Standardize the data
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(df[['recency', 'frequency', 'monetary_value']])

        # Elbow method to find the optimal number of clusters
        sse = []
        k_range = range(1, 11)
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(rfm_scaled)
            sse.append(kmeans.inertia_)

        # Determine the optimal number of clusters using the elbow method
        optimal_k = 3  # You can choose the optimal number of clusters based on the elbow curve
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(rfm_scaled)

        # Create a new GLViewWidget for 3D plotting
        view = gl.GLViewWidget()
        view.opts['distance'] = 40
        view.setWindowTitle('3D RFM Clustering')
        view.setGeometry(0, 110, 1280, 720)

        # Add grid to the view
        grid = gl.GLGridItem()
        view.addItem(grid)

        # Prepare data for 3D scatter plot
        colors = np.array([pg.glColor(c) for c in df['Cluster']])
        scatter_data = np.array([df['recency'], df['frequency'], df['monetary_value']]).T

        # Create a scatter plot item
        scatter_plot = gl.GLScatterPlotItem(pos=scatter_data, size=5, color=colors, pxMode=True)
        view.addItem(scatter_plot)

        # Add axis labels
        axis = gl.GLAxisItem()
        axis.setSize(x=10, y=10, z=10)
        view.addItem(axis)

        # Clear the previous plot and add the new 3D view widget to the layout
        for i in reversed(range(self.verticalLayoutRFM.count())):
            self.verticalLayoutRFM.itemAt(i).widget().setParent(None)

        self.verticalLayoutRFM.addWidget(view)
        view.show()



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
            self.chartverticalLayoutQuantitySold(df_verticalLayoutQuantitySold)

        # verticalLayoutPercentWaste
        df_verticalLayoutPercentWaste = self.databaseConnectEx.connector.queryDataset("""
            SELECT pi.sales_outlet_id, pi.product_id, SUM(pi.quantity_sold)/COUNT(d.Dates_ID) AS Total_Percen_Waste
            FROM pastry_inventory pi
            JOIN dates d ON pi.transaction_date = d.transaction_date
            GROUP BY pi.product_id, d.Month_ID, pi.sales_outlet_id
            ORDER BY d.Month_ID;
        """)
        if not df_verticalLayoutPercentWaste.empty:
            self.chartverticalLayoutPercentWaste(df_verticalLayoutPercentWaste)

        # verticalLayoutTotalInventorySoldByDay
        df_verticalLayoutTotalInventorySoldByDay = self.databaseConnectEx.connector.queryDataset("""
            SELECT d.Dates_ID, SUM(pi.quantity_sold) as total_quantity_sold, pi.sales_outlet_id
            FROM pastry_inventory pi
            JOIN dates d ON d.transaction_date = pi.transaction_date
            GROUP BY d.Dates_ID, pi.sales_outlet_id
            ORDER BY d.Dates_ID;
        """)
        if not df_verticalLayoutTotalInventorySoldByDay.empty:
            self.chartverticalLayoutTotalInventorySoldByDay(df_verticalLayoutTotalInventorySoldByDay)

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
            self.chartverticalLayoutSaleTarget(df_verticalLayoutSaleTarget)

    def chartverticalLayoutQuantitySold(self, df):
        # Ensure the data types are correct
        df['product_id'] = df['product_id'].astype(str)
        df['sales_outlet_id'] = df['sales_outlet_id'].astype(str)
        df['Total_quantity_sold'] = df['Total_quantity_sold'].astype(int)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Total Quantity Sold by Product ID", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Quantity Sold", **labelStyle)
        plot_widget.setLabel("bottom", "Product ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        products = df['product_id'].unique()
        outlets = df['sales_outlet_id'].unique()

        # Prepare the bar chart data
        bar_width = 0.5
        x = np.arange(len(products))

        # Initialize an array to hold the cumulative height of the bars
        cumulative_height = np.zeros(len(products))

        # Define a color palette
        color_palette = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        # Create the stacked bars
        bar_charts = []
        for i, outlet in enumerate(outlets):
            outlet_data = df[df['sales_outlet_id'] == outlet]
            total_quantity_sold = np.array(
                [outlet_data[outlet_data['product_id'] == product]['Total_quantity_sold'].sum() for product in
                 products])
            bar_chart = pg.BarGraphItem(x=x, height=total_quantity_sold, width=bar_width,
                                        brush=color_palette[i % len(color_palette)])
            plot_widget.addItem(bar_chart)
            cumulative_height += total_quantity_sold
            bar_charts.append((bar_chart, f'Sales Outlet {outlet}'))

        # Add a legend
        legend = plot_widget.addLegend()
        for bar_chart, outlet_label in bar_charts:
            legend.addItem(bar_chart, outlet_label)

        # Set x-axis ticks to show product IDs
        x_ticks = [(i, str(product)) for i, product in enumerate(products)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutQuantitySold.count())):
            self.verticalLayoutQuantitySold.itemAt(i).widget().setParent(None)

        self.verticalLayoutQuantitySold.addWidget(plot_widget)

    def chartverticalLayoutPercentWaste(self, df):
        # Ensure the data types are correct
        df['product_id'] = df['product_id'].astype(str)
        df['sales_outlet_id'] = df['sales_outlet_id'].astype(str)
        df['Total_Percen_Waste'] = df['Total_Percen_Waste'].astype(float)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Percent Waste by Product ID", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Percent Waste", **labelStyle)
        plot_widget.setLabel("bottom", "Product ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        products = df['product_id'].unique()
        outlets = df['sales_outlet_id'].unique()

        # Prepare the bar chart data
        bar_width = 0.5
        x = np.arange(len(products))

        # Initialize an array to hold the cumulative height of the bars
        cumulative_height = np.zeros(len(products))

        # Define a color palette
        color_palette = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        # Create the stacked bars
        bar_charts = []
        for i, outlet in enumerate(outlets):
            outlet_data = df[df['sales_outlet_id'] == outlet]
            total_percent_waste = np.array(
                [outlet_data[outlet_data['product_id'] == product]['Total_Percen_Waste'].mean() for product in
                 products])
            bar_chart = pg.BarGraphItem(x=x, height=total_percent_waste, width=bar_width,
                                        brush=color_palette[i % len(color_palette)])
            plot_widget.addItem(bar_chart)
            cumulative_height += total_percent_waste
            bar_charts.append((bar_chart, f'Sales Outlet {outlet}'))

        # Add a legend
        legend = plot_widget.addLegend()
        for bar_chart, outlet_label in bar_charts:
            legend.addItem(bar_chart, outlet_label)

        # Set x-axis ticks to show product IDs
        x_ticks = [(i, str(product)) for i, product in enumerate(products)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutPercentWaste.count())):
            self.verticalLayoutPercentWaste.itemAt(i).widget().setParent(None)

        self.verticalLayoutPercentWaste.addWidget(plot_widget)

    def chartverticalLayoutTotalInventorySoldByDay(self, df):
        # Ensure the data types are correct
        df['Dates_ID'] = df['Dates_ID'].astype(int)
        df['sales_outlet_id'] = df['sales_outlet_id'].astype(str)
        df['total_quantity_sold'] = df['total_quantity_sold'].astype(int)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Total Inventory Sold by Day", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Total Quantity Sold", **labelStyle)
        plot_widget.setLabel("bottom", "Dates ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        dates = df['Dates_ID'].unique()
        outlets = df['sales_outlet_id'].unique()

        # Define a color palette
        color_palette = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        # Create the line plots for each sales outlet
        for i, outlet in enumerate(outlets):
            outlet_data = df[df['sales_outlet_id'] == outlet]
            sorted_data = outlet_data.sort_values(by='Dates_ID')
            dates_sorted = sorted_data['Dates_ID'].values
            total_quantity_sold_sorted = sorted_data['total_quantity_sold'].values

            line = plot_widget.plot(dates_sorted, total_quantity_sold_sorted,
                                    pen=pg.mkPen(color_palette[i % len(color_palette)], width=2),
                                    name=f'Sales Outlet {outlet}')

        # Add a legend
        legend = plot_widget.addLegend()

        # Set x-axis ticks to show dates
        x_ticks = [(i, str(date)) for i, date in enumerate(dates)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutTotalInventorySoldByDay.count())):
            self.verticalLayoutTotalInventorySoldByDay.itemAt(i).widget().setParent(None)

        self.verticalLayoutTotalInventorySoldByDay.addWidget(plot_widget)

    def chartverticalLayoutSaleTarget(self, df):
        # Ensure the data types are correct
        df['sales_outlet_id'] = df['sales_outlet_id'].astype(str)
        df['total_goal'] = df['total_goal'].astype(float)
        df['total_quantity_sold'] = df['total_quantity_sold'].astype(float)
        df['percent'] = df['percent'].astype(float)

        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()

        # Configure the graph
        plot_widget.setTitle("Sales Target", color="r", size="15pt", bold=True, italic=True)
        plot_widget.setBackground('w')

        labelStyle = {"color": "green", "font-size": "18px"}
        plot_widget.setLabel("left", "Value", **labelStyle)
        plot_widget.setLabel("bottom", "Sales Outlet ID", **labelStyle)
        plot_widget.showGrid(x=True, y=True)

        # Extract the data
        outlets = df['sales_outlet_id'].unique()
        total_goals = df['total_goal']
        total_quantity_sold = df['total_quantity_sold']
        percent = df['percent']

        # Set bar width and positions
        bar_width = 0.3
        x = np.arange(len(outlets))

        # Create the bar charts
        goal_bar = pg.BarGraphItem(x=x - bar_width / 2, height=total_goals, width=bar_width, brush='b',
                                   name='Total Goal')
        sold_bar = pg.BarGraphItem(x=x + bar_width / 2, height=total_quantity_sold, width=bar_width, brush='g',
                                   name='Total Quantity Sold')

        # Add the bar charts to the plot
        plot_widget.addItem(goal_bar)
        plot_widget.addItem(sold_bar)

        # Add a legend
        legend = plot_widget.addLegend()
        legend.addItem(goal_bar, 'Total Goal')
        legend.addItem(sold_bar, 'Total Quantity Sold')

        # Set x-axis ticks to show sales outlet IDs
        x_ticks = [(i, outlet) for i, outlet in enumerate(outlets)]
        plot_widget.getAxis('bottom').setTicks([x_ticks])

        # Clear the previous plot and add the new plot widget to the layout
        for i in reversed(range(self.verticalLayoutSaleTarget.count())):
            self.verticalLayoutSaleTarget.itemAt(i).widget().setParent(None)

        self.verticalLayoutSaleTarget.addWidget(plot_widget)

    def show(self):
        self.MainWindow.show()





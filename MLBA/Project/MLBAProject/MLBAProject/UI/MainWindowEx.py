import random
from random import random
import plotly.graph_objects as go
import pandas as pd

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QDialog, QComboBox, QPushButton, QListWidgetItem, QMessageBox, QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QDialog, QComboBox, QPushButton, QCheckBox, \
    QListWidgetItem
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Connectors.Connector import Connector
from Models.PurchaseLinearRegression import PurchaseLinearRegression
from Models.PurchaseStatistic import PurchaseStatistic
from UI.ChartHandle import ChartHandle
from UI.DatabaseConnectEx import DatabaseConnectEx
from UI.FullScreenChartEx import FullScreenChartEx
from UI.MainWindow import Ui_MainWindow
import traceback


import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import random


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.purchaseLinearRegression = PurchaseLinearRegression()
        self.databaseConnectEx=DatabaseConnectEx()
        self.databaseConnectEx.parent=self
        self.chartHandle= ChartHandle()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.verticalLayoutFunctions.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setupPlot()

        self.actionConnection.triggered.connect(self.openDatabaseConnectUI)

        self.pushButtonPurchaseRatesByGender.clicked.connect(self.showPurchaseRatesByGender)
        self.pushButtonSalesFlucuationsByYearAndMonth.clicked.connect(self.showSalesFlucuationsByYearAndMonth)
        self.pushButtonPurchaseCountingByCategory.clicked.connect(self.showPurchaseCountingByCategory)
        self.pushButtonPurchaseRatesByAgeGroup.clicked.connect(self.showPurchaseRatesByAgeGroup)
        self.pushButtonPurchaseCountingByCategory.clicked.connect(self.showPurchaseCountingByCategory)
        self.pushButtonPurchaseValueByCategory.clicked.connect(self.showPurchaseValueByCategory)
        self.pushButtonPurchaseByCategoryAndGender.clicked.connect(self.showPurchaseByCategoryAndGender)
        self.pushButtonPaymentMethod.clicked.connect(self.showPaymentMethod)
        self.pushButtonPurchaseRatesByShoppingMall.clicked.connect(self.showPurchaseRatesByShoppingMall)
        self.pushButtonProductSpendingByGender.clicked.connect(self.showProductSpendingByGender)
        self.pushButtonPurchaseFrequenceByAge.clicked.connect(self.showShowPurchaseFrequenceByAge)
        self.pushButtonSalesFluctuationsByMonth.clicked.connect(self.showpushButtonSalesFluctuationsByMonth)
        self.pushButtonFullScreen.clicked.connect(self.showFullScreen)
        self.pushButtonTrainModel.clicked.connect(self.train_model)
        self.checkEnableWidget(False)

        self.comboBoxDataset.activated.connect(self.processSelectedComboBox)

    def show(self):
        self.MainWindow.show()
    def checkEnableWidget(self,flag=True):
        self.pushButtonPurchaseRatesByGender.setEnabled(flag)
        self.pushButtonPurchaseRatesByAgeGroup.setEnabled(flag)
        self.pushButtonPurchaseCountingByCategory.setEnabled(flag)
        self.pushButtonPurchaseValueByCategory.setEnabled(flag)
        self.pushButtonPurchaseByCategoryAndGender.setEnabled(flag)
        self.pushButtonPaymentMethod.setEnabled(flag)
        self.pushButtonPurchaseRatesByShoppingMall.setEnabled(flag)

        self.pushButtonProductSpendingByGender.setEnabled(flag)
        self.pushButtonPurchaseFrequenceByAge.setEnabled(flag)
        self.pushButtonSalesFluctuationsByMonth.setEnabled(flag)
        self.pushButtonSalesFlucuationsByYearAndMonth.setEnabled(flag)
        if flag==True:
            self.loadTablesName()

    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        self.pushButtonFullScreen=QPushButton(self.MainWindow)
        self.pushButtonFullScreen.setText("Full Screen")

        icon = QIcon()
        icon.addPixmap(
            QPixmap("E:\\Elearning\\QT Designer\\MLBAProject\\UI\\../Images/ic_fullscreen.png"),
            QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonFullScreen.setIcon(icon)
        self.pushButtonFullScreen.setIconSize(QSize(16,16))

        self.toolbar.addWidget(self.pushButtonFullScreen)

        graph_types = ["Line Graph", "Bar Chart", "Scatter Plot"]
        self.graph_type_combobox = QComboBox(self.MainWindow)
        self.graph_type_combobox.addItems(graph_types)
        self.graph_type_combobox.currentIndexChanged.connect(self._on_graph_type_selected)
        self.toolbar.addWidget(self.graph_type_combobox)

        # adding tool bar to the layout
        self.verticalLayoutPlot.addWidget(self.toolbar)
        # adding canvas to the layout
        self.verticalLayoutPlot.addWidget(self.canvas)

    def _on_graph_type_selected(self):
        # Create a new graph based on the selected type from the drop-down menu
        graph_type = self.graph_type_combobox.currentText()
        fig = self.canvas.figure
        n_plots = len(fig.get_axes())

        for ax in fig.get_axes():
            ax.remove()

        # Set the subplot grid to 1 row and 1 column
        n_new_rows, n_new_cols = 1, 1

        if graph_type == "Line Graph":
            new_ax = fig.add_subplot(n_new_rows, n_new_cols, 1)
            new_ax.plot([1, 2, 3], [4, 2, 6], color='blue')  # Set color to blue
            new_ax.set_title('Line Graph')

        elif graph_type == "Bar Chart":
            new_ax = fig.add_subplot(n_new_rows, n_new_cols, 1)
            bars = new_ax.bar(['A', 'B', 'C'], [3, 7, 2],
                              color=['red', 'green', 'blue'])  # Set colors to red, green, and blue
            new_ax.set_title('Bar Chart')

        elif graph_type == "Scatter Plot":
            new_ax = fig.add_subplot(n_new_rows, n_new_cols, 1)
            new_ax.scatter([1, 2, 3], [4, 2, 6], color='orange')  # Set color to orange
            new_ax.set_title('Scatter Plot')

        fig.canvas.draw()
    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()
    def showDataIntoTableWidget(self,df):
        self.tableWidgetStatistic.setRowCount(0)
        self.tableWidgetStatistic.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            self.tableWidgetStatistic.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            self.tableWidgetStatistic.insertRow(row)
            j=0
            for data in arr:
                self.tableWidgetStatistic.setItem(row, j, QTableWidgetItem(str(data)))
                j=j+1
            row = row + 1

    def showPurchaseCountingByCategory(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.purchaseLinearRegression.execPurchaseHistory()
        self.purchaseLinearRegression.processCategoryDistribution()
        print(self.purchaseLinearRegression.dfCategory)

        df = self.purchaseLinearRegression.dfCategory

        self.showDataIntoTableWidget(df)

        columnLabel = "category"
        columnStatistic = "count"
        title = "Categories Distribution"
        legend = False
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)
        self.chartHandle.visualizePieChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, legend)

    def showPurchaseRatesByGender(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.purchaseLinearRegression.execPurchaseHistory()
        self.purchaseLinearRegression.processGenderDistribution()
        print(self.purchaseLinearRegression.dfGender)

        df = self.purchaseLinearRegression.dfGender

        self.showDataIntoTableWidget(df)

        columnLabel = "gender"
        columnStatistic = "count"
        title = "Gender Distribution"
        legend = True
        self.chartHandle.visualizePieChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, legend)
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)

    def showSalesFlucuationsByYearAndMonth(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.purchaseLinearRegression.execPurchaseHistory()
        self.purchaseLinearRegression.processMonthlyAndYearSalesAmount()
        print(self.purchaseLinearRegression.dfMonthlyAndYearSalesAmount)
        df = self.purchaseLinearRegression.dfMonthlyAndYearSalesAmount
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeLinePlotChart(self.figure,self.canvas, self.purchaseLinearRegression.dfMonthlyAndYearSalesAmount, "month", "sales_amount",
                                    "Monthly Variation in Sales Amount Over Years", hue="year", xticks=True)
        #self.visualizeLinePlotChart(self.purchaseLinearRegression.dfMonthlyAndYearSalesAmount, "month", "sales_amount",
        #                            "Monthly Variation in Sales Amount Over Years", hue="year", xticks=True)
    def showPurchaseRatesByAgeGroup(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.purchaseLinearRegression.execPurchaseHistory()
        fromAge=int(self.lineEditFromAge.text())
        toAge=int(self.lineEditToAge.text())
        self.purchaseLinearRegression.processAgeDistribution(fromAge,toAge)
        print(self.purchaseLinearRegression.dfAges)

        df = self.purchaseLinearRegression.dfAges

        self.showDataIntoTableWidget(df)
        columnLabel= "age"
        columnStatistic ="count"
        title= "Age Distribution %s~%s"%(fromAge,toAge)
        hue = None
        self.chartHandle.visualizeLinePlotChart(self.figure,self.canvas,df, columnLabel, columnStatistic,title, hue)
        #self.visualizeLinePlotChart(df, columnLabel, columnStatistic,title, hue)
    def showPurchaseCountingByCategory(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processCategoryDistribution()
        self.showDataIntoTableWidget(df)
        columnLabel = "category"
        columnStatistic = "count"
        title = "Categories Distribution"
        legend = False
        hue=None
        self.chartHandle.visualizeLinePlotChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, hue)
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)
    def showPurchaseValueByCategory(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processCategorySpending()
        self.showDataIntoTableWidget(df)
        columnLabel = "category"
        columnStatistic = "price"
        title = "Distribution category and Spending"
        self.chartHandle.visualizeBarChart(self.figure,self.canvas,df,columnLabel,columnStatistic,title)
        #self.visualizeBarChart(df,columnLabel,columnStatistic,title)
    def showPurchaseByCategoryAndGender(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processGenderAndCategoryCounter()
        self.showDataIntoTableWidget(df)
        df=self.purchaseLinearRegression.df
        columnLabel = "category"
        columnStatistic = "count"
        hue="gender"
        title = "Distribution gender and category"
        self.chartHandle.visualizeMultiBarChart(self.figure,self.canvas,df, columnLabel, columnStatistic,hue, title)
        #self.visualizeMultiBarChart(df, columnLabel, columnStatistic,hue, title)
    def showPaymentMethod(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processPaymentMethod()
        self.showDataIntoTableWidget(df)
        columnLabel = "payment_method"
        columnStatistic = "count"
        title = "Payment Distribution"
        legend = False
        self.chartHandle.visualizePieChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, legend)
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)
    def showPurchaseRatesByShoppingMall(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processShoppingMall()
        self.showDataIntoTableWidget(df)
        columnLabel = "shopping_mall"
        columnStatistic = "count"
        title = "Shopping Mall Distribution"
        legend = False
        self.chartHandle.visualizePieChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, legend)
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)
    def showProductSpendingByGender(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processGenderCategorySpending()
        self.showDataIntoTableWidget(df)
        columnLabel = "category"
        columnStatistic = "price"
        hue="gender"
        title = "Male and Female category Total Price Spend"
        legend = False
        self.chartHandle.visualizeBarPlot(self.figure,self.canvas,df, columnLabel, columnStatistic,hue, title)
        #self.visualizeBarPlot(df, columnLabel, columnStatistic,hue, title)

    def showShowPurchaseFrequenceByAge(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()
        df = self.purchaseLinearRegression.processAgeOrderFrequence()
        self.showDataIntoTableWidget(df)
        columnLabel = "age"
        columnStatistic = "count"
        title = "Age VS Order Frequence"
        self.chartHandle.visualizeScatterPlot(self.figure,self.canvas,df, columnLabel,columnStatistic, title)
        #self.visualizeScatterPlot(df, columnLabel,columnStatistic, title)

    def showpushButtonSalesFluctuationsByMonth(self):
        # self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        # self.purchaseLinearRegression.execPurchaseHistory()

        df=self.purchaseLinearRegression.processMonthlySalesAmount()
        print(df)

        self.showDataIntoTableWidget(df)
        columnLabel = "month"
        columnStatistic = "sales_amount"
        title = "Monthly Variation in Sales Amount"
        hue = None
        self.chartHandle.visualizeLinePlotChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, hue)
        #self.visualizeLinePlotChart(df, columnLabel, columnStatistic, title, hue)
    def showFullScreen(self):
        window= QMainWindow()

        self.fullScreen=FullScreenChartEx()
        self.fullScreen.setupUi(window)
        self.fullScreen.figure = self.figure
        self.fullScreen.canvas.draw()
        self.fullScreen.show()
    def loadTablesName(self):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        tablesName=self.purchaseLinearRegression.connector.getTablesName()
        print(tablesName)
        self.comboBoxDataset.clear()
        for tableName in tablesName:
            self.comboBoxDataset.addItem(tableName)
    def processSelectedComboBox(self):
        index = self.comboBoxDataset.currentIndex()
        tableName = self.comboBoxDataset.currentText()
        self.loadDataForMachineLearningTab(tableName)
        pass
    def loadDataForMachineLearningTab(self,tableName):
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        self.df = self.purchaseLinearRegression.execPurchaseHistory(tableName)
        self.purchaseLinearRegression.connector = self.databaseConnectEx.connector
        df=self.purchaseLinearRegression.execPurchaseHistory(tableName)
        self.listWidgetIndependentVariables.clear()
        self.listWidgetDependentVariables.clear()
        # for i in reversed(range(self.scrollAreaIndependentVariables.count())):
        #     self.scrollAreaIndependentVariables.itemAt(i).widget().setParent(None)
        for column in df.columns:
            itemIndependent=QListWidgetItem(column)
            itemIndependent.setCheckState(Qt.CheckState.Unchecked)
            self.listWidgetIndependentVariables.addItem(itemIndependent)
            itemDependent=QListWidgetItem(column)
            itemDependent.setCheckState(Qt.CheckState.Unchecked)
            self.listWidgetDependentVariables.addItem(itemDependent)

    def get_selected_columns(list_widget):
        selected_columns = []

        for i in range(list_widget.count()):
            item = list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected_columns.append(item.text())

        return selected_columns

    def train_model(list_widget_inputs, list_widget_targets, line_edit_test_size, line_edit_random_state):
        selected_inputs = get_selected_columns(list_widget_inputs)
        selected_targets = get_selected_columns(list_widget_targets)

        if not selected_inputs or not selected_targets:
            QMessageBox.warning(None, "Warning", "Please select at least one input and one target column.")
            return

        input_text = ", ".join(selected_inputs)
        target_text = ", ".join(selected_targets) if selected_targets else "None"

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Are you sure you want to train the model with the following columns?")
        msgBox.setInformativeText("Inputs: {}\nTargets: {}".format(input_text, target_text))
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.StandardButton.Ok:
            training_service = PurchaseLinearRegression(databaseConnectEx.connector)

            test_size = float(line_edit_test_size.text()) / 100
            random_state = int(line_edit_random_state.text())

            training_service.process_train(columns_input=selected_inputs, column_target=selected_targets,
                                           test_size=test_size, random_state=random_state)
            result = training_service.evaluate()
            # setup_machine_learning_ui(selected_inputs, selected_targets)
            lineEditMAE.setText(str(round(result.MAE, 2)))
            lineEditMSE.setText(str(round(result.MSE, 2)))
            lineEditRMSE.setText(str(round(result.RMSE, 2)))
            lineEditR2SCORE.setText(str(round(result.R2_SCORE, 2)))


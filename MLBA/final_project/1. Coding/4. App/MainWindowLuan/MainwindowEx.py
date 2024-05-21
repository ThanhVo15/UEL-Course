from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

from Mainwindow_ui import Ui_MainWindow

import random
from random import random
import plotly.graph_objects as go

from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QDialog, QComboBox, QPushButton, QCheckBox, \
    QListWidgetItem
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import traceback


import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd
from ChartHandle import ChartHandle




class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.ChartHandle= ChartHandle()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow



        self.pushButton_Dashboard.clicked.connect(self.switch_to_DashboardPage)
        self.pushButton_Dashboard_ic.clicked.connect(self.switch_to_DashboardPage)

        self.pushButton_Training.clicked.connect(self.switch_to_TrainingPage)
        self.pushButton_Training_ic.clicked.connect(self.switch_to_TrainingPage)

        self.pushButton_Data.clicked.connect(self.switch_to_DataPage)
        self.pushButton_Data_ic.clicked.connect(self.switch_to_DataPage)

        self.pushButton_Setting.clicked.connect(self.switch_to_Settingpage)
        self.pushButton_Setting_ic.clicked.connect(self.switch_to_Settingpage)

        
        self.pushButton_sales.clicked.connect(self.switch_to_SalesPage)
        self.pushButton_Customer.clicked.connect(self.switch_to_CustomerPage)
        self.pushButton_Employee.clicked.connect(self.switch_to_EmployeePage)
        self.pushButton_Inventory.clicked.connect(self.switch_to_Inventory)


        self.pushButton_sales.clicked.connect(self.showPurchaseRatesByGender)

        self.setupPlot()


        
        

    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

      

        graph_types = ["Line Graph", "Bar Chart", "Scatter Plot"]
        self.graph_type_combobox = QComboBox(self.MainWindow)
        self.graph_type_combobox.addItems(graph_types)
        self.graph_type_combobox.currentIndexChanged.connect(self._on_graph_type_selected)
        self.toolbar.addWidget(self.graph_type_combobox)


        

        # adding tool bar to the layout
        self.layouts_plot.addWidget(self.toolbar)
        # adding canvas to the layout
        self.layouts_plot.addWidget(self.canvas)
    



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


    

    def showPurchaseRatesByGender(self):
        


        data = {
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'count': [20, 30, 25, 35, 15, 45, 22, 33, 18, 27]
}
        df = pd.DataFrame(data)


        columnLabel = "gender"
        columnStatistic = "count"
        title = "Gender Distribution"
        legend = True
        self.ChartHandle.visualizePieChart(self.figure,self.canvas,df, columnLabel, columnStatistic, title, legend)
        #self.visualizePieChart(df, columnLabel, columnStatistic, title, legend)








# Hàm đổi sang các trang dashboar, training, Datapage, Setting
    def switch_to_DashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_TrainingPage(self):
        self.stackedWidget.setCurrentIndex(1)   
    def switch_to_DataPage(self):
        self.stackedWidget.setCurrentIndex(2) 
    def switch_to_Settingpage(self):
        self.stackedWidget.setCurrentIndex(3)



# Hàm đổi sang các trang trong page dashboard
    def switch_to_SalesPage(self):
        self.stackedWidget_3.setCurrentIndex(0)
    def switch_to_CustomerPage(self):
        self.stackedWidget_3.setCurrentIndex(1)   
    def switch_to_EmployeePage(self):
        self.stackedWidget_3.setCurrentIndex(2) 
    def switch_to_Inventory(self):
        self.stackedWidget_3.setCurrentIndex(3)




    def show(self):
        self.MainWindow.show()

    

   
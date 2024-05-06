import json
from functools import partial

import pandas as pd
from PyQt6.QtCore import QModelIndex, Qt, QObject
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMenu, QFileDialog, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from MainWindow import Ui_MainWindow
from TableModel import TableModel
import os.path

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.data = {}
        self.columns = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                        'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address']

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonPickDataset.clicked.connect(self.processLoadModel)
        self.pushButtonViewDataset.clicked.connect(self.processViewDataset)

    def processLoadModel(self):
        filters = "CSV file (*.csv);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        # Get the selected file name and display it on the QLineEdit
        self.lineEditSelectDataset.setText(filename)

        # Read data from the CSV file into a pandas DataFrame
        df = pd.read_csv(filename)

        # Create a list of rows (list of lists) for TableModel
        data = df.values.tolist()
        columns = df.columns.tolist()

        # Create the TableModel
        self.model = TableModel(data, columns)

        # Set the TableModel to the TableView
        self.tableViewDataset.setModel(self.model)

    def show(self):
        self.MainWindow.show()

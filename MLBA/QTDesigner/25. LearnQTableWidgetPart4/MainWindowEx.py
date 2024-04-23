from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.databasePath = "database/MyDatabase.sqlite"
        self.selectedRecord=None
        self.selectedRow=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.connectDatabase()
        self.loadProduct()
        self.pushButtonNew.clicked.connect(self.processNew)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.processItemSelection)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonRemove.clicked.connect(self.processRemove)

    def connectDatabase(self):
        # create QSqlDatabase object
        self.db = QSqlDatabase("QSQLITE")
        # set the database selected path
        self.db.setDatabaseName(self.databasePath)
        # Open the SQLite database
        self.db.open()
        # Create QSqlTableModel object, and self.db is assigned
        self.model = QSqlTableModel(db=self.db)

    def loadProduct(self):
        # # select table name to invoke data
        # tableName = "Product"
        # self.model.setTable(tableName)
        # # active for selecting data
        # self.model.select()
        # # reset QTableWidget to 0 row
        # self.tableWidgetProduct.setRowCount(0)
        # # loop for insert new row:
        # for i in range(self.model.rowCount()):
        #     # insert new row:
        #     self.tableWidgetProduct.insertRow(i)
        #     # get a record with i index:
        #     record = self.model.record(i)
        #     itemId = QTableWidgetItem(str(record.value(0)))
        #     itemProductCode = QTableWidgetItem(str(record.value(1)))
        #     itemProductName = QTableWidgetItem(str(record.value(2)))
        #     itemUnitPrice = QTableWidgetItem(str(record.value(3)))
        #     self.tableWidgetProduct.setItem(i, 0, itemId)
        #     self.tableWidgetProduct.setItem(i, 1, itemProductCode)
        #     self.tableWidgetProduct.setItem(i, 2, itemProductName)
        #     self.tableWidgetProduct.setItem(i, 3, itemUnitPrice)

        # Get the current Table Name in QCombobox
        tableName = "Product"
        # Create QSqlTableModel object, and self.db is assigned
        self.model = QSqlTableModel(db=self.db)
        # select table name to invoke data
        self.model.setTable(tableName)
        # active for selecting data
        self.model.select()
        # reset QTableWidget to 0 row
        self.tableWidgetProduct.setRowCount(0)
        # get the column count for selected Table as automatic
        self.columns = self.model.record().count()
        # set columns count for QTableWidget
        self.tableWidgetProduct.setColumnCount(self.columns)
        # create labels array for Columns Headers
        labels = []
        for i in range(self.columns):
            # get column name:
            fieldName = self.model.record().fieldName(i)
            # store the column name
            labels.append(fieldName)
        # set the columns header with labels
        self.tableWidgetProduct.setHorizontalHeaderLabels(labels)
        # loop for insert new row:
        for i in range(self.model.rowCount()):
            # insert new row:
            self.tableWidgetProduct.insertRow(i)
            # get a record with i index:
            record = self.model.record(i)
            # loop column to get value for each cell:
            for j in range(self.columns):
                # create QTableWidgetItem object
                item = QTableWidgetItem(str(record.value(j)))
                # set value for each CELL:
                self.tableWidgetProduct.setItem(i, j, item)


    def processNew(self):
        self.lineEditProductCode.setText("")
        self.lineEditProductName.setText("")
        self.lineEditUnitPrice.setText("")
        self.lineEditProductCode.setFocus()
        self.selectedRecord=None
        self.selectedRow=None

    def processItemSelection(self):
        #Get current row index on the QTableWidget
        self.selectedRow=self.tableWidgetProduct.currentRow()
        if self.selectedRow==-1:
            return
        #call record(index) method from model
        self.selectedRecord=self.model.record(self.selectedRow)
        #Get detail information from QSqlRecord
        #id=self.selectedRecord.value(0)
        productCode=self.selectedRecord.value(1)
        productName=self.selectedRecord.value(2)
        unitPrice=self.selectedRecord.value(3)
        # show detail information into the QLineEdit
        self.lineEditProductCode.setText(productCode)
        self.lineEditProductName.setText(productName)
        self.lineEditUnitPrice.setText(str(unitPrice))

    def processSave(self):
        #Get lasted row
        row = self.model.rowCount()
        if self.selectedRecord==None:#if new product
            #Get the QSqlRecord from record(row)
            record=self.model.record(row)
            #assign the value for QSqlRecord
            #record.setValue(0, None)
            record.setValue(1,self.lineEditProductCode.text())
            record.setValue(2, self.lineEditProductName.text())
            record.setValue(3, float(self.lineEditUnitPrice.text()))
            #call the insertRecord for storing a new record into SQLite
            result=self.model.insertRecord(row,record)
            #if saving successful then result =True
            if result==True:
                #save the lasted record and reload products
                self.selectedRecord=record
                self.selectedRow=row
                self.loadProduct()
        else:#if updating the QSqlRecord
            # assign the value for QSqlRecord
            self.selectedRecord.setValue(1, self.lineEditProductCode.text())
            self.selectedRecord.setValue(2, self.lineEditProductName.text())
            self.selectedRecord.setValue(3, float(self.lineEditUnitPrice.text()))
            # call the updateRowInTable for updating selected record into SQLite
            result=self.model.updateRowInTable(self.selectedRow,self.selectedRecord)
            # if saving successful then result =True
            if result == True:
                #reload products
                self.loadProduct()
    def processRemove(self):
        dlg = QMessageBox(self.MainWindow)
        if self.selectedRecord == None:
            dlg.setWindowTitle("Deleteing error")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setText("You have to select a Product to delete")
            dlg.exec()
            return
        dlg.setWindowTitle("Confirmation Deleting")
        dlg.setText("Are you sure you want to delete?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            #call removeRow method to remove QSqlRecord from the SQLite
            result=self.model.removeRow(self.selectedRow)
            # if saving successful then result =True
            if result == True:
                # save the lasted record and reload products
                self.loadProduct()
                self.processNew()
    def show(self):
        self.MainWindow.show()
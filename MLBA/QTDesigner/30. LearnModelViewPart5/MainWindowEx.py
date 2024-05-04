import os.path

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.loadDatabase()
        self.lineEditFilter.textChanged.connect(self.processFilterName)
        self.pushButtonFilter.clicked.connect(self.processFilterColumns)
    def loadDatabase(self):
        baseDir=os.path.dirname(__file__)
        databasePath=os.path.join(baseDir,"Chinook_Sqlite.sqlite")
        self.db=QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(databasePath)
        self.db.open()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("Employee")
        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.tableView.setModel(self.model)
    def processFilterName(self,s):
        filter_str = 'LastName LIKE "%{}%" or FirstName LIKE "%{}%"'.format(s,s)
        self.model.setFilter(filter_str)
    def processFilterColumns(self):
        query = QSqlQuery("SELECT EmployeeId, FirstName, LastName FROM Employee ", db=self.db)
        self.model.setQuery(query)
    def show(self):
        self.MainWindow.show()
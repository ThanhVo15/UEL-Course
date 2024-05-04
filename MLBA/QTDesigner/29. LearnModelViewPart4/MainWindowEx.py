import json
from functools import partial

from PyQt6.QtCore import QModelIndex, Qt, QObject
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMenu, QFileDialog
from InsertBehavior import InsertBehavior
from MainWindow import Ui_MainWindow
from TableModel import TableModel

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.data = [["p1", "Coca", 100],
                ["p2", "Pepsi", 50],
                ["p3", "Sting", 300],
                ["p4", "Aqua", 70],
                ["p5", "Redbull", 200],
                ["p6", "", 120]]
        self.columns = ["ID", "Name", "Price"]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.model = TableModel(self.data, self.columns)
        self.tableView.setModel(self.model)

        self.tableView.selectionModel().selectionChanged.connect(self.processItemSelection)

        self.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.onCustomContextMenuRequested)

        self.tableView.verticalHeader().setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableView.verticalHeader().customContextMenuRequested.connect(self.onCustomContextMenuRequested)

        self.actionExport_to_JSon.triggered.connect(self.processExportJson)
        self.actionImport_from_Json.triggered.connect(self.processImportJson)
    def processItemSelection(self):
        index=self.tableView.currentIndex()
        if index.row()>-1:
            item=self.data[index.row()]
            self.lineEditID.setText(item[0])
            self.lineEditName.setText(item[1])
            self.lineEditUnitPrice.setText(str(item[2]))

    def onCustomContextMenuRequested(self, pos):
        index = self.tableView.indexAt(pos)
        menu = QMenu()
        if index.isValid():
            insertFirst = menu.addAction("Insert &First")
            insertFirst.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_insert top.png"))
            insertLast = menu.addAction("Insert &Last")
            insertLast.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_insert last.png"))
            insertAbove = menu.addAction("Insert &Above")
            insertAbove.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_insert last.png"))
            insertBelow = menu.addAction("Insert &Below")
            insertBelow.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_insert last.png"))
            removeSelected = menu.addAction("Remove selected row")
            removeSelected.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_delete.png"))

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
            menu.exec(self.tableView.viewport().mapToGlobal(pos))
            menu.close()
        else:
            insertNew = menu.addAction("Insert New Record")
            insertNew.setIcon(QIcon(r"D:\GitHub\UEL-Course\MLBA\QTDesigner\29. LearnModelViewPart4\images\ic_new.png"))
            menu.addAction(insertNew)
            insertNew.triggered.connect(partial(self.processInsert, InsertBehavior.INSERT_TOP))
            menu.exec(self.tableView.viewport().mapToGlobal(pos))
            menu.close()

    def processInsert(self,behavior=InsertBehavior.INSERT_TOP):
        indexes = self.tableView.selectionModel().selectedIndexes()
        if behavior==InsertBehavior.INSERT_TOP:
            row=0
        elif behavior==InsertBehavior.INSERT_LAST:
            row = self.tableView.model().rowCount(QModelIndex())+1
        else:
            if indexes:
                index=indexes[0]
                row=index.row()
                if behavior==InsertBehavior.INSERT_ABOVE:
                    row=max(row,0)
                else:
                    size = self.tableView.model().rowCount(QModelIndex())
                    row = min(row + 1, size)
        self.tableView.model().insertRows(row, 1, QModelIndex())
    def processDelete(self):
        indexes = self.tableView.selectionModel().selectedIndexes()
        if indexes:
                index=indexes[0]
                row = index.row()
                self.tableView.model().removeRows(row, 1, QModelIndex())

    def processExportJson(self):
        # setup for QFileDialog
        filters = "Dataset (*.json);;All files(*)"
        filename, selected_filter = QFileDialog.getSaveFileName(
            self.MainWindow,
            filter=filters,
        )
        #self.fileFactory.writeData(filename,self.model.data)
        with open(filename, 'w') as jf:
            jsonString = json.dumps(self.model.data)
            jsonFile = open(filename, "w")
            jsonFile.write(jsonString)
            jsonFile.close()
    def processImportJson(self):
        # setup for QFileDialog
        filters = "Dataset (*.json);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        with open(filename, 'r') as jf:
            lines = jf.readline()
            print(lines)
            self.data= json.loads(lines)
            self.model.data= self.data
        self.model.layoutChanged.emit()
    def show(self):
        self.MainWindow.show()
import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QListWidgetItem

from FileFactory import FileFactory
from MainWindow import Ui_MainWindow
from Tasks import Task
from Tasks import Tasks

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.tasks=Tasks()
        self.fileFactory = FileFactory()
        self.selectedTask=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        arrData= self.fileFactory.readData("database.json", Task)
        self.tasks.addAll(arrData)
        self.showTasksIntoQListWidget()
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonDelete.clicked.connect(self.processRemove)
        self.listWidget.itemSelectionChanged.connect(self.processItemSelection)
    def showTasksIntoQListWidget(self):
        self.listWidget.clear()
        for index in range(self.tasks.size()):
            task=self.tasks.item(index)
            item=QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, task)
            item.setText(str(task))
            item.setCheckState(Qt.CheckState.Unchecked)
            if task.isfinish==True:
                item.setIcon(QIcon("images/ic_finished.png"))
            else:
                item.setIcon(QIcon("images/ic_notfinished.png"))
            if isinstance(task.deadline,str):
                task.deadline= datetime.date.fromisoformat(task.deadline)
            if isinstance(task.deadlinetime,str):
                task.deadlinetime=datetime.time.fromisoformat(task.deadlinetime)
            self.listWidget.addItem(item)
    def processNew(self):
        self.lineEditTitle.setText("")
        self.lineEditContent.setText("")
        self.dateEditDeadline.setSpecialValueText(None)
        self.radioButtonFinished.setAutoExclusive(False)
        self.radioNotFinished.setAutoExclusive(False)
        self.radioButtonFinished.setChecked(False)
        self.radioNotFinished.setChecked(False)
        self.radioButtonFinished.setAutoExclusive(True)
        self.radioNotFinished.setAutoExclusive(True)
        self.selectedTask=None
        self.lineEditTitle.setFocus()
    def processSave(self):
        title=self.lineEditTitle.text()
        content=self.lineEditContent.toPlainText()
        date=self.dateEditDeadline.date().toPyDate()
        time=self.timeEditTimeDeadline.time().toPyTime()
        isFinished=self.radioButtonFinished.isChecked()
        task=Task(title,content,date,time,isFinished)
        if self.selectedTask==None:
            self.tasks.add(task)
        else:
            index=self.tasks.index(self.selectedTask)
            self.tasks.update(index,task)
        self.selectedTask = task
        self.showTasksIntoQListWidget()
        self.fileFactory.writeData("database.json",self.tasks.lists)
    def processRemove(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        size=self.listWidget.count()
        for index in range(size-1,-1,-1):
            item=self.listWidget.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                self.tasks.removeByIndex(index)
        self.selectedTask = None
        self.showTasksIntoQListWidget()
        self.fileFactory.writeData("database.json", self.tasks.lists)
    def processItemSelection(self):
        row=self.listWidget.currentRow()
        task=self.tasks.item(row)
        self.lineEditTitle.setText(task.title)
        self.lineEditContent.setText(task.content)
        self.dateEditDeadline.setDate(task.deadline)
        self.timeEditTimeDeadline.setTime(task.deadlinetime)
        if task.isfinish:
            self.radioButtonFinished.setChecked(True)
            self.radioNotFinished.setChecked(False)
        else:
            self.radioButtonFinished.setChecked(False)
            self.radioNotFinished.setChecked(True)
        self.selectedTask=task
    def show(self):
        self.MainWindow.show()
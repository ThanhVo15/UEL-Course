from MainWindowFirstDegreeEquation import Ui_MainWindow


class MainWindowFirstDegreeEquationEX(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.MainWindow.setWindowTitle("Tran Duy Thanh - Demo Layout Management")
        self.pushButtonExit.clicked.connect(self.process_exit)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonSolution.clicked.connect(self.process_solution)
    def process_solution(self):
        a = float(self.lineEditCoefficientA.text())
        b = float(self.lineEditCoefficientB.text())
        if a==0 and b ==0:
            self.lineEditsolution.setText("Infinities solutions")
        elif a==0 and b!=0:
            self.lineEditsolution.setText("No solution")
        else:
            self.lineEditsolution.setText("X="+str(-b/a))
    def process_clear(self):
        self.lineEditCoefficientA.setText("")
        self.lineEditCoefficientB.setText("")
        self.lineEditsolution.setText("")
        self.lineEditCoefficientA.setFocus()
    def process_exit(self):
        self.MainWindow.close()
    def show(self):
        self.MainWindow.show()
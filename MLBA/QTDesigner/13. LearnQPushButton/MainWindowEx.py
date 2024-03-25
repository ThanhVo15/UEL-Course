from MainWindow import Ui_BMICACULATOR


class MainWindowEx(Ui_BMICACULATOR):
    def __init__(self):
        pass
    def setupUi(self, BMICACULATOR):
        super().setupUi(BMICACULATOR)
        self.BMICACULATOR=BMICACULATOR
        self.CaculatepushButton.clicked.connect(self.calculateBMI)

    def calculateBMI(self):
        weight = float(self.lineEdit.text())
        height = float(self.lineEdit_2.text())
        height = height / 100
        BMI = weight / (height * height)
        BMI = round(BMI, 2)
        comment = ""
        style = ""

        if BMI < 16:
            comment = "Severe Thinness"
            style = "color: blue; font-weight: bold;"
        elif BMI < 17:
            comment = "Moderate Thinness"
            style = "color: cyan; font-weight: bold;"
        elif BMI < 18.5:
            comment = "Mild Thinness"
            style = "color: green; font-weight: bold;"
        elif BMI < 25:
            comment = "Normal"
            style = "color: black; font-weight: bold;"
        elif BMI < 30:
            comment = "Overweight"
            style = "color: orange; font-weight: bold;"
        elif BMI < 35:
            comment = "Obese Class I"
            style = "color: purple; font-weight: bold;"
        elif BMI < 40:
            comment = "Obese Class II"
            style = "color: red; font-weight: bold;"
        else:
            comment = "Obese Class III"
            style = "color: darkred; font-weight: bold;"


        self.label_9.setText(str(BMI))
        self.label_9.setStyleSheet(style)
        self.label_10.setText(comment)
        self.label_10.setStyleSheet(style)
    def show(self):
        self.BMICACULATOR.show()

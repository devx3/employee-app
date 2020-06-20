from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtWidgets import *
from database import Database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.salaryChartWidget = QtWidgets.QWidget(self.centralwidget)
        self.salaryChartWidget.setObjectName("salaryChartWidget")
        self.gridLayout_2.addWidget(self.salaryChartWidget, 0, 0, 1, 1)
        self.positionChartWidget = QtWidgets.QWidget(self.centralwidget)
        self.positionChartWidget.setObjectName("positionChartWidget")

        self.firstLayout  = QGridLayout(self.salaryChartWidget)
        self.secondLayout = QGridLayout(self.positionChartWidget)

        self.gridLayout_2.addWidget(self.positionChartWidget, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(678, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 30)
        self.gridLayout_2.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatórios"))
        self.backButton.setText(_translate("MainWindow", "Back"))

class ChartsWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu):
        super(ChartsWindow, self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()

        self.firstChart  = QChart()
        self.secondChart = QChart()
        self.firstSeries = QBarSeries()
        self.secondSeries = QPieSeries()

        self.load_first_series()
        self.load_second_series()

        self.firstChart.addSeries(self.firstSeries)
        self.firstChart.setTitle("Dados de Salário")

        self.secondChart.addSeries(self.secondSeries)
        self.secondChart.setTitle("Salários por Departamento")

        self.secondChartView = QChartView(self.secondChart)
        self.secondChartView.setRenderHint(QPainter.Antialiasing)


        self.firstChartView = QChartView(self.firstChart)
        self.firstChartView.setRenderHint(QPainter.Antialiasing)

        self.ui.firstLayout.addWidget(self.firstChartView)   
        self.ui.secondLayout.addWidget(self.secondChartView)   

        self.ui.backButton.clicked.connect(self.back_button_clicked)
    
    def load_first_series(self):
        result_list = self.db.get_salary_statistics()

        minBarSet = QBarSet("Menor Salário")
        avgBarSet = QBarSet("Média de Salário")
        maxBarSet = QBarSet("Maior Salário")

        minBarSet << result_list[0] 
        avgBarSet << result_list[1] 
        maxBarSet << result_list[2] 
        
        self.firstSeries.append(minBarSet)
        self.firstSeries.append(avgBarSet)
        self.firstSeries.append(maxBarSet)
    
    def load_second_series(self):
        result_list = self.db.get_total_department_salaries()

        for entry in result_list:
            self.secondSeries.append(entry[0], entry[1])

    def back_button_clicked(self):
        self.hide()
        self.mainMenu.show()
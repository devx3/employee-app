from PyQt5 import QtCore, QtGui, QtWidgets
from manage_employees import EmployeesWindow
from charts import ChartsWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 300)
        MainWindow.setMinimumSize(QtCore.QSize(250, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.manageEmployeesButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageEmployeesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manageEmployeesButton.sizePolicy().hasHeightForWidth())
        self.manageEmployeesButton.setSizePolicy(sizePolicy)
        self.manageEmployeesButton.setMinimumSize(QtCore.QSize(200, 60))
        self.manageEmployeesButton.setMaximumSize(QtCore.QSize(200, 60))
        self.manageEmployeesButton.setObjectName("manageEmployeesButton")
        self.gridLayout.addWidget(self.manageEmployeesButton, 1, 0, 1, 1)
        self.viewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewChartsButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewChartsButton.sizePolicy().hasHeightForWidth())
        self.viewChartsButton.setSizePolicy(sizePolicy)
        self.viewChartsButton.setMinimumSize(QtCore.QSize(200, 60))
        self.viewChartsButton.setMaximumSize(QtCore.QSize(200, 60))
        self.viewChartsButton.setObjectName("viewChartsButton")
        self.gridLayout.addWidget(self.viewChartsButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestor de Empregods"))
        self.manageEmployeesButton.setText(_translate("MainWindow", "Gerenciar Empregados"))
        self.viewChartsButton.setText(_translate("MainWindow", "Visualizar Gráficos"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manageEmployeesButton.clicked.connect(self.manage_employees_button_clicked)
        self.ui.viewChartsButton.clicked.connect(self.view_charts_button_clicked)

    def manage_employees_button_clicked(self):
        self.hide()
        self.employeesWindow = EmployeesWindow(self)
        self.employeesWindow.show()

    def view_charts_button_clicked(self): 
        self.hide()
        self.chartWindow = ChartsWindow(self)
        self.chartWindow.show()
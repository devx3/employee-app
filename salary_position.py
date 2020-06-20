from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from database import Database
from new_salary import SalaryDialog
from new_position import PositionDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(-1, 15, -1, 15)
        self.gridLayout_5.setHorizontalSpacing(25)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 1)
        self.salaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.salaryLogLabel.setObjectName("salaryLogLabel")
        self.gridLayout_2.addWidget(self.salaryLogLabel, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 2, 1, 1)
        self.salaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.salaryTableWidget.setObjectName("salaryTableWidget")
        self.salaryTableWidget.setColumnCount(0)
        self.salaryTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.salaryTableWidget, 1, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.changeSalaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeSalaryButton.setObjectName("changeSalaryButton")
        self.gridLayout.addWidget(self.changeSalaryButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 0, 1, 1)
        self.positionLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLogLabel.setObjectName("positionLogLabel")
        self.gridLayout_3.addWidget(self.positionLogLabel, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.changePositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePositionButton.setObjectName("changePositionButton")
        self.gridLayout_4.addWidget(self.changePositionButton, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 0, 1, 3)
        self.positionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.positionTableWidget.setObjectName("positionTableWidget")
        self.positionTableWidget.setColumnCount(0)
        self.positionTableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.positionTableWidget, 1, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.salaryLogLabel.setText(_translate("MainWindow", "Salário Log"))
        self.changeSalaryButton.setText(_translate("MainWindow", "Mudar Salário"))
        self.positionLogLabel.setText(_translate("MainWindow", "Cargo Log"))
        self.changePositionButton.setText(_translate("MainWindow", "Mudar Cargo"))

class EmployeeInfoWindow(QtWidgets.QMainWindow):

    def __init__(self, id, parent):
        super(EmployeeInfoWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = id

        self.init_tables()
        self.parentWidget = parent
        self.ui.changeSalaryButton.clicked.connect(self.change_salary_button_clicked)
        self.ui.changePositionButton.clicked.connect(self.change_position_button_clicked)


    def init_tables(self):
        self.db = Database()
        result_salary   = self.db.get_salary_for_employee(self.id)
        result_position = self.db.get_position_for_employee(self.id)

        # Setting salary log
        self.init_table( self.ui.salaryTableWidget, result_salary[0], result_salary[1] )

        # Setting position log
        self.init_table( self.ui.positionTableWidget, result_position[0], result_position[1] )
        

    def init_table(self, tableWidget, header_list, values_list):

        no_rows    = len(values_list)
        no_columns = len(header_list)

        tableWidget.clear()
        tableWidget.setRowCount(no_rows)
        tableWidget.setColumnCount(no_columns)
        
        tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWidget.verticalHeader().hide()

        # Set Values
        for row in range(no_rows):
            for column in range(no_columns):
                tableWidget.setItem(row, column, QTableWidgetItem(str(values_list[row][column])))

    def change_salary_button_clicked(self):

        last_row = self.ui.salaryTableWidget.rowCount()-1

        self.salaryDialog = SalaryDialog(
            self.ui.salaryTableWidget.item(last_row, 0).text(),
            self.ui.salaryTableWidget.item(last_row, 1).text(),
            self.ui.salaryTableWidget.item(last_row, 3).text()
        )

        res = self.salaryDialog.exec()

        if res == QtWidgets.QDialog.Accepted:
            self.db.insert_new_salary( self.id, self.salaryDialog.new_salary, self.salaryDialog.reason )

            self.init_tables()
            self.parentWidget.init_table(self.db.get_employee_full_info([]))

    def change_position_button_clicked(self):
        last_row = self.ui.positionTableWidget.rowCount() - 1
        self.positionDialog = PositionDialog(
            self.ui.positionTableWidget.item(last_row, 0).text(),
            self.ui.positionTableWidget.item(last_row, 1).text(),
            self.ui.positionTableWidget.item(last_row, 3).text(),
        )
        res = self.positionDialog.exec()

        if res == QtWidgets.QDialog.Accepted:
            self.db.insert_new_position(self.id, self.positionDialog.new_position)
            self.init_tables()
            self.parentWidget.init_table(self.db.get_employee_full_info([]))
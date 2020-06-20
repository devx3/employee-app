from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent, Qt, QObject, QPoint
from new_employee import NewEmployeeDialog
from salary_position import EmployeeInfoWindow
from database import Database
from datetime import datetime

import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.topGridLayout = QtWidgets.QGridLayout()
        self.topGridLayout.setObjectName("topGridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")


        self.topGridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(898, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.topGridLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")

        self.widget.hide()
        self.toolButton.setIcon(QtGui.QIcon(':/resources/down-arrow.png'))

        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(self.widget)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.lastnameLabel = QtWidgets.QLabel(self.widget)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastnameLabel)
        self.lastnameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastnameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lastnameLineEdit.setObjectName("lastnameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastnameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(self.widget)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayLineEdit = QtWidgets.QLineEdit(self.widget)
        self.birthdayLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.birthdayLineEdit.setObjectName("birthdayLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthdayLineEdit)
        self.gridLayout_3.addLayout(self.formLayout, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.departmentLabel = QtWidgets.QLabel(self.widget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(self.widget)
        self.departmentLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(self.widget)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.widget)
        self.salaryLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(self.widget)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.positionLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.applyButton = QtWidgets.QPushButton(self.widget)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 0, 1, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.bottomGridLayout = QtWidgets.QGridLayout()
        self.bottomGridLayout.setObjectName("bottomGridLayout")
        spacerItem7 = QtWidgets.QSpacerItem(618, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomGridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.bottomGridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.bottomGridLayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")
        self.bottomGridLayout.addWidget(self.exportButton, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.bottomGridLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerenciar Empregados"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.idLabel.setText(_translate("MainWindow", "ID"))
        self.nameLabel.setText(_translate("MainWindow", "Nome"))
        self.lastnameLabel.setText(_translate("MainWindow", "Sobrenome"))
        self.birthdayLabel.setText(_translate("MainWindow", "Aniversário"))
        self.departmentLabel.setText(_translate("MainWindow", "Setor"))
        self.salaryLabel.setText(_translate("MainWindow", "Salário"))
        self.positionLabel.setText(_translate("MainWindow", "Cargo"))
        self.applyButton.setText(_translate("MainWindow", "Aplicar"))
        self.resetButton.setText(_translate("MainWindow", "Resetar"))
        self.backButton.setText(_translate("MainWindow", "Voltar"))
        self.newButton.setText(_translate("MainWindow", "Novo"))
        self.exportButton.setText(_translate("MainWindow", "Exportar"))

class EmployeesWindow(QtWidgets.QMainWindow): 
    def __init__(self, mainMenu):
        super(EmployeesWindow, self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = Database()
        
        self.init_table(self.db.get_employee_full_info([]))
        self.init_fieldmap()

        self.ui.tableWidget.viewport().installEventFilter(self)

        self.ui.backButton.clicked.connect(self.back_button_clicked)
        self.ui.newButton.clicked.connect(self.new_button_clicked)
        self.ui.toolButton.clicked.connect(self.tool_button_clicked)    
        self.ui.applyButton.clicked.connect(self.apply_button_clicked)
        self.ui.resetButton.clicked.connect(self.reset_button_clicked)
        self.ui.exportButton.clicked.connect(self.export_button_clicked)
        
    
    def init_table(self, employee_list): 
        header_list   = employee_list[0]
        value_list    = employee_list[1]
        
        no_rows    = len(value_list)
        no_columns = len(header_list)

        self.ui.tableWidget.clear()

        self.ui.tableWidget.setRowCount(no_rows)
        self.ui.tableWidget.setColumnCount(no_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.verticalHeader().hide()

        for row in range(no_rows):
            for column in range(no_columns):
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(value_list[row][column])))
        
        self.ui.tableWidget.cellChanged.connect(self.edited)

    def init_fieldmap(self):
        self.fieldmap = {}
        self.fieldmap[self.ui.idLineEdit.objectName()]         = 'e.id'
        self.fieldmap[self.ui.nameLineEdit.objectName()]       = 'e.firstname'
        self.fieldmap[self.ui.lastnameLineEdit.objectName()]   = 'e.lastname'
        self.fieldmap[self.ui.birthdayLineEdit.objectName()]   = 'e.birthday'
        self.fieldmap[self.ui.departmentLineEdit.objectName()] = 'e.department_name'
        self.fieldmap[self.ui.salaryLineEdit.objectName()]     = 'ls.salary'
        self.fieldmap[self.ui.positionLineEdit.objectName()]   = 'lp.position'

    def eventFilter(self, obj, event):
        if (obj == self.ui.tableWidget.viewport() and event.type() == QEvent.MouseButtonPress):
            if( event.button() == Qt.RightButton ):
                idx = self.ui.tableWidget.indexAt(event.pos())
                if( idx.isValid() ):
                    deleteAction = QAction("Deletar", self)
                    deleteAction.setObjectName(str(idx.row()))
                    deleteAction.triggered.connect(self.delete_action_triggered)

                    modifyAction = QAction("Modificar", self)
                    modifyAction.setObjectName(str(idx.row()))
                    modifyAction.triggered.connect(self.modify_action_triggered)

                    contextMenu = QMenu(self)
                    contextMenu.addAction(deleteAction)
                    contextMenu.addAction(modifyAction)

                    contextMenu.exec(event.globalPos())

        return QMainWindow.eventFilter(self, obj, event)

    def tool_button_clicked(self):
        if self.ui.widget.isVisible():
            self.ui.widget.hide()
            self.ui.toolButton.setIcon(QtGui.QIcon(':/resources/down-arrow.png'))
        else: 
            self.ui.toolButton.setIcon(QtGui.QIcon(':/resources/up-arrow.png'))
            self.ui.widget.show()

    def apply_button_clicked(self):
        conditional_list = []
        if self.ui.idLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.idLineEdit.objectName()], f'"{self.ui.idLineEdit.text()}"' ] )

        if self.ui.nameLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.nameLineEdit.objectName()], f'"%{self.ui.nameLineEdit.text()}%"' ] )

        if self.ui.lastnameLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.lastnameLineEdit.objectName()], f'"%{self.ui.lastnameLineEdit.text()}%"' ] )

        if self.ui.birthdayLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.birthdayLineEdit.objectName()], f'"%{self.ui.birthdayLineEdit.text()}%"' ] )

        if self.ui.departmentLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.departmentLineEdit.objectName()], f'"%{self.ui.departmentLineEdit.text()}%"' ] )

        if self.ui.salaryLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.salaryLineEdit.objectName()], f'"%{self.ui.salaryLineEdit.text()}%"' ] )

        if self.ui.positionLineEdit.text():
            conditional_list.append( [self.fieldmap[self.ui.positionLineEdit.objectName()], f'"%{self.ui.positionLineEdit.text()}%"' ] )

        print(conditional_list)

        self.init_table(self.db.get_employee_full_info(conditional_list))
    
    def reset_button_clicked(self):
        self.ui.idLineEdit.clear()
        self.ui.nameLineEdit.clear()
        self.ui.lastnameLineEdit.clear()
        self.ui.birthdayLineEdit.clear()
        self.ui.departmentLineEdit.clear()
        self.ui.salaryLineEdit.clear()
        self.ui.positionLineEdit.clear()

        self.init_table(self.db.get_employee_full_info([]))

    def delete_action_triggered(self):

        row = int(QObject.sender(self).objectName())
        fname  = self.ui.tableWidget.item(row, 1).text()
        lname  = self.ui.tableWidget.item(row, 2).text()
        reply = QMessageBox.question(self, "Deletar Empregado", f"Tem certeza que deseja deletar o funcionário: {fname + ' ' + lname}?", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            id  = self.ui.tableWidget.item(row, 0).text()
            self.db.delete_employee(id)
            self.ui.tableWidget.removeRow(row)

    def modify_action_triggered(self):
        row = int(QObject.sender(self).objectName())
        id = self.ui.tableWidget.item(row, 0).text()
        self.employeeInfoWindow = EmployeeInfoWindow(id, self)
        self.employeeInfoWindow.show()

    def edited(self):
        for tableItem in self.ui.tableWidget.selectedItems():
            print(tableItem.row(), tableItem.column(), tableItem.text())

    def back_button_clicked(self):
        self.hide()
        self.mainMenu.show()
    
    def new_button_clicked(self):
        self.employeeDialog = NewEmployeeDialog()
        res = self.employeeDialog.exec()

        if res == QtWidgets.QDialog.Accepted:
            self.db.insert_employee(self.employeeDialog.employeeInfo)

            self.init_table(self.db.get_employee_full_info([]))

    def export_button_clicked(self):
        filename = f"empregados-{datetime.today().strftime('%Y-%m-%d')}"
        path = str(QtWidgets.QFileDialog.getSaveFileName(self, "Salvar Arquivo", filename, "CSV(*.csv)")[0])

        if path != "":
            with open(path, 'w+', newline='') as stream:
                csv_writer = csv.writer(stream)

                no_columns = self.ui.tableWidget.columnCount()
                no_rows    = self.ui.tableWidget.rowCount()

                header_data = []
                for col in range(no_columns):
                    header_data.append(self.ui.tableWidget.horizontalHeaderItem(col).text())
                
                csv_writer.writerow(header_data)

                for row in range(no_rows):
                    row_data = []  
                    for col in range(no_columns):
                        item = self.ui.tableWidget.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else: 
                            row_data.append('')
                    csv_writer.writerow(row_data)
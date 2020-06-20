from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import resources

from employee_full_info import EmployeeFullInfo
from calendar_dialog import CalendarDialog
from datetime import datetime

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 365)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.lastnameLabel = QtWidgets.QLabel(Dialog)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastnameLabel)
        self.lastnameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.lastnameLineEdit.setObjectName("lastnameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastnameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(Dialog)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayToolButton = QtWidgets.QToolButton(Dialog)
        self.birthdayToolButton.setText("")
        self.birthdayToolButton.setObjectName("birthdayToolButton")

        self.birthdayToolButton.setIcon(QtGui.QIcon(':/resources/calendar_icon.png'))

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.birthdayToolButton)
        self.dateValueLabel = QtWidgets.QLabel(Dialog)
        self.dateValueLabel.setObjectName("dateValueLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateValueLabel)
        self.departmentLabel = QtWidgets.QLabel(Dialog)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(Dialog)
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(Dialog)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(Dialog)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nameLabel.setText(_translate("Dialog", "Nome"))
        self.lastnameLabel.setText(_translate("Dialog", "Sobrenome"))
        self.birthdayLabel.setText(_translate("Dialog", "Aniversário"))
        self.dateValueLabel.setText(_translate("Dialog", "Nenhuma data selecionada"))
        self.departmentLabel.setText(_translate("Dialog", "Departamento"))
        self.salaryLabel.setText(_translate("Dialog", "Salário"))
        self.positionLabel.setText(_translate("Dialog", "Cargo"))
        self.saveButton.setText(_translate("Dialog", "Salvar"))

class NewEmployeeDialog(QtWidgets.QDialog):

    def __init__(self):
        super(NewEmployeeDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.employeeInfo = None
        self.birthday = None

        self.ui.saveButton.clicked.connect(self.save_button_clicked)
        self.ui.birthdayToolButton.clicked.connect(self.birthday_button_clicked)

    def save_button_clicked(self): 

        fields = {
            'fname'     : self.ui.nameLineEdit.text(),
            'lname'     : self.ui.lastnameLineEdit.text(),
            'department': self.ui.departmentLineEdit.text(),
            'salary'    : self.ui.salaryLineEdit.text(),
            'position'  : self.ui.positionLineEdit.text()
        }

        self.employeeInfo = EmployeeFullInfo(
            fields['fname'],
            fields['lname'],
            self.birthday,
            fields['department'],
            fields['salary'],
            fields['position']
        )

        self.accept()

    def birthday_button_clicked(self):
        self.calendarDialog = CalendarDialog()
        result = self.calendarDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.birthday = self.calendarDialog.date
            self.ui.dateValueLabel.setText(QtCore.QDate(self.birthday).toString())
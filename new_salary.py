# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_salary.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 306)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(27)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameValueLabel = QtWidgets.QLabel(Dialog)
        self.nameValueLabel.setObjectName("nameValueLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameValueLabel)
        self.lastnameLabel = QtWidgets.QLabel(Dialog)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastnameLabel)
        self.lastnameValueLabel = QtWidgets.QLabel(Dialog)
        self.lastnameValueLabel.setObjectName("lastnameValueLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastnameValueLabel)
        self.currentSalary = QtWidgets.QLabel(Dialog)
        self.currentSalary.setObjectName("currentSalary")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentSalary)
        self.currentSalaryLabel = QtWidgets.QLabel(Dialog)
        self.currentSalaryLabel.setObjectName("currentSalaryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentSalaryLabel)
        self.newSalaryLabel = QtWidgets.QLabel(Dialog)
        self.newSalaryLabel.setObjectName("newSalaryLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newSalaryLabel)
        self.newSalaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.newSalaryLineEdit.setObjectName("newSalaryLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newSalaryLineEdit)
        self.reasonLabel = QtWidgets.QLabel(Dialog)
        self.reasonLabel.setObjectName("reasonLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reasonLabel)
        self.reasonLineEdit = QtWidgets.QLineEdit(Dialog)
        self.reasonLineEdit.setObjectName("reasonLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reasonLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(105, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(105, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nameLabel.setText(_translate("Dialog", "Nome"))
        self.nameValueLabel.setText(_translate("Dialog", "Erick"))
        self.lastnameLabel.setText(_translate("Dialog", "Sobrenome"))
        self.lastnameValueLabel.setText(_translate("Dialog", "Fabiani"))
        self.currentSalary.setText(_translate("Dialog", "Salário Atual"))
        self.currentSalaryLabel.setText(_translate("Dialog", "R$ 3.000"))
        self.newSalaryLabel.setText(_translate("Dialog", "Novo Salário"))
        self.reasonLabel.setText(_translate("Dialog", "Motivo"))
        self.reasonLineEdit.setPlaceholderText(_translate("Dialog", "Opcional"))
        self.saveButton.setText(_translate("Dialog", "Salvar"))

class SalaryDialog(QtWidgets.QDialog):

    def __init__(self, fname, lname, current_salary):
        super(SalaryDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.nameValueLabel.setText(fname)
        self.ui.lastnameValueLabel.setText(lname)
        self.ui.currentSalaryLabel.setText(str(current_salary))  

        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        self.new_salary = self.ui.newSalaryLineEdit.text()
        self.reason = self.ui.reasonLineEdit.text()

        self.accept()
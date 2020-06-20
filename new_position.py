# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_position.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 300)
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
        self.currentPositionLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionLabel.setObjectName("currentPositionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentPositionLabel)
        self.currentPositionValueLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionValueLabel.setObjectName("currentPositionValueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentPositionValueLabel)
        self.newPositionLabel = QtWidgets.QLabel(Dialog)
        self.newPositionLabel.setObjectName("newPositionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newPositionLabel)
        self.newPositionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.newPositionLineEdit.setPlaceholderText("")
        self.newPositionLineEdit.setObjectName("newPositionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newPositionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.currentPositionLabel.setText(_translate("Dialog", "Cargo Atual"))
        self.currentPositionValueLabel.setText(_translate("Dialog", "BIzeiro"))
        self.newPositionLabel.setText(_translate("Dialog", "Novo Cargo"))
        self.saveButton.setText(_translate("Dialog", "Salvar"))

class PositionDialog(QtWidgets.QDialog):
    def __init__(self, fname, lname, current_position):
        super(PositionDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.nameValueLabel.setText(fname)
        self.ui.lastnameValueLabel.setText(lname)
        self.ui.currentPositionValueLabel.setText(current_position)

        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):

        self.new_position = self.ui.newPositionLineEdit.text()

        self.accept()
    
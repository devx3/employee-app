# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 270)
        Dialog.setMinimumSize(QtCore.QSize(322, 270))
        Dialog.setMaximumSize(QtCore.QSize(322, 270))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(106, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.saveButton.setText(_translate("Dialog", "Salvar"))

class CalendarDialog(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.date = None

        self.ui.saveButton.clicked.connect(self.save_button_clicked)
    
    def save_button_clicked(self):
        self.date = self.ui.calendarWidget.selectedDate()
        self.done(QtWidgets.QDialog.Accepted)
        
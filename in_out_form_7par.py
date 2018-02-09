# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'in_out_form_7par.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qt7parWindow(object):
    def setupUi(self, Qt7parWindow):
        Qt7parWindow.setObjectName("Qt7parWindow")
        Qt7parWindow.resize(817, 637)
        self.buttonBoxOkCancel = QtWidgets.QDialogButtonBox(Qt7parWindow)
        self.buttonBoxOkCancel.setGeometry(QtCore.QRect(90, 580, 501, 32))
        self.buttonBoxOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOkCancel.setCenterButtons(True)
        self.buttonBoxOkCancel.setObjectName("buttonBoxOkCancel")
        self.pushButtonPushme = QtWidgets.QPushButton(Qt7parWindow)
        self.pushButtonPushme.setGeometry(QtCore.QRect(580, 540, 111, 23))
        self.pushButtonPushme.setCheckable(False)
        self.pushButtonPushme.setObjectName("pushButtonPushme")
        self.Button_open_wgs = QtWidgets.QPushButton(Qt7parWindow)
        self.Button_open_wgs.setGeometry(QtCore.QRect(30, 80, 121, 31))
        self.Button_open_wgs.setObjectName("Button_open_wgs")
        self.textEdit = QtWidgets.QTextEdit(Qt7parWindow)
        self.textEdit.setGeometry(QtCore.QRect(560, 490, 201, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_in_1 = QtWidgets.QLabel(Qt7parWindow)
        self.label_in_1.setGeometry(QtCore.QRect(30, 60, 331, 16))
        self.label_in_1.setObjectName("label_in_1")
        self.label_message = QtWidgets.QLabel(Qt7parWindow)
        self.label_message.setGeometry(QtCore.QRect(0, 0, 771, 51))
        self.label_message.setTextFormat(QtCore.Qt.AutoText)
        self.label_message.setObjectName("label_message")
        self.Button_open_datum = QtWidgets.QPushButton(Qt7parWindow)
        self.Button_open_datum.setGeometry(QtCore.QRect(30, 220, 121, 31))
        self.Button_open_datum.setObjectName("Button_open_datum")
        self.label_in_2 = QtWidgets.QLabel(Qt7parWindow)
        self.label_in_2.setGeometry(QtCore.QRect(30, 200, 361, 16))
        self.label_in_2.setObjectName("label_in_2")
        self.comboBox_elips_wgs = QtWidgets.QComboBox(Qt7parWindow)
        self.comboBox_elips_wgs.setGeometry(QtCore.QRect(500, 80, 161, 22))
        self.comboBox_elips_wgs.setObjectName("comboBox_elips_wgs")
        self.comboBox_elips_krasov = QtWidgets.QComboBox(Qt7parWindow)
        self.comboBox_elips_krasov.setGeometry(QtCore.QRect(500, 220, 161, 22))
        self.comboBox_elips_krasov.setObjectName("comboBox_elips_krasov")
        self.textBrowser_wgs = QtWidgets.QTextBrowser(Qt7parWindow)
        self.textBrowser_wgs.setGeometry(QtCore.QRect(30, 120, 721, 61))
        self.textBrowser_wgs.setObjectName("textBrowser_wgs")
        self.textBrowser_krasov = QtWidgets.QTextBrowser(Qt7parWindow)
        self.textBrowser_krasov.setGeometry(QtCore.QRect(30, 260, 721, 61))
        self.textBrowser_krasov.setObjectName("textBrowser_krasov")
        self.tableWidget_7par = QtWidgets.QTableWidget(Qt7parWindow)
        self.tableWidget_7par.setGeometry(QtCore.QRect(30, 330, 301, 141))
        self.tableWidget_7par.setObjectName("tableWidget_7par")
        self.tableWidget_7par.setColumnCount(0)
        self.tableWidget_7par.setRowCount(0)

        self.retranslateUi(Qt7parWindow)
        self.buttonBoxOkCancel.rejected.connect(Qt7parWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Qt7parWindow)

    def retranslateUi(self, Qt7parWindow):
        _translate = QtCore.QCoreApplication.translate
        Qt7parWindow.setWindowTitle(_translate("Qt7parWindow", "Форма для проверки работы кнопок"))
        self.pushButtonPushme.setText(_translate("Qt7parWindow", "Нажми меня"))
        self.Button_open_wgs.setText(_translate("Qt7parWindow", "Открыть файл"))
        self.label_in_1.setText(_translate("Qt7parWindow", "Координаты в эталонной СК  (например на элипсоиде WGS94)"))
        self.label_message.setText(_translate("Qt7parWindow", "Программа предназначена для вычисления 7ми параметров перехода между системами координат по соотвествующим точкам в градусах"))
        self.Button_open_datum.setText(_translate("Qt7parWindow", "Открыть файл"))
        self.label_in_2.setText(_translate("Qt7parWindow", "Координаты в искомой СК (например на элипсоиде Красовского)"))


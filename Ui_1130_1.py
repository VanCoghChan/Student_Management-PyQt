# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PyQt5\test.ui\1130_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from Ui_1130 import Ui_MainWindow

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 162)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 48, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 131, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "查询"))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.label.setText(_translate("Dialog", "姓名："))

class Dialog1(QtWidgets.QMainWindow, Ui_Dialog1):
    def __init__(self):
        super(Dialog1, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./piliang_ico/Toolsnet.png'))
        self.setFixedSize(self.width(),self.height())

    def get_text(self):
        return self.lineEdit.text()

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 162)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 48, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 131, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "查询"))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.label.setText(_translate("Dialog", "学号："))

class Dialog2(QtWidgets.QMainWindow, Ui_Dialog2):
    def __init__(self):
        super(Dialog2, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./piliang_ico/Toolsnet.png'))
        self.setFixedSize(self.width(),self.height())


    def get_text(self):
        return self.lineEdit.text()
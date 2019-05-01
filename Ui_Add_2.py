# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PyQt5\test.ui\Add_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog_add2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 419)
        Dialog.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.graphicsView_1 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_1.setGeometry(QtCore.QRect(40, 50, 31, 31))
        self.graphicsView_1.setStyleSheet("border-image: url(./piliang_ico/ID.png);")
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 60, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(140, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 110, 31, 31))
        self.graphicsView_2.setStyleSheet("border-image: url(./piliang_ico/name.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(40, 170, 31, 31))
        self.graphicsView_3.setStyleSheet("border-image: url(./piliang_ico/physics__easyicon.net.png);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 180, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_4.setGeometry(QtCore.QRect(40, 230, 31, 31))
        self.graphicsView_4.setStyleSheet("border-image: url(./piliang_ico/maths_.png);")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 240, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 230, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_5.setGeometry(QtCore.QRect(40, 290, 31, 31))
        self.graphicsView_5.setStyleSheet("border-image: url(./piliang_ico/mathematics.net.png);")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 300, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 360, 81, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "手动添加"))
        self.label.setText(_translate("Dialog", "学号:"))
        self.label_2.setText(_translate("Dialog", "姓名:"))
        self.label_3.setText(_translate("Dialog", "大物:"))
        self.label_4.setText(_translate("Dialog", "离散:"))
        self.label_5.setText(_translate("Dialog", "线代:"))

buttonstyle="""
padding-left: 10px;
padding-right: 10px;
padding-top: 1px;
padding-bottom: 1px;
border:3px solid orange;
border-radius:15px;
background: lightgray;
image: url(./piliang_ico/confirm.net.png);
color: white;
"""
class Add_d2(QtWidgets.QMainWindow, Ui_Dialog_add2):
    def __init__(self):
        super(Add_d2, self).__init__()
        self.setupUi(self)
        self.pushButton.setStyleSheet(buttonstyle)
        self.setWindowIcon(QIcon('./piliang_ico/export.png'))
        self.setFixedSize(self.width(),self.height())

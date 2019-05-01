# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PyQt5\test.ui\sample_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Dialog_sample(object):
    def setupUi(self, Dialog,filepath1,filepath2):
        Dialog.setObjectName("Dialog")
        Dialog.resize(877, 390)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 311, 291))
        self.graphicsView.setStyleSheet("border-image: url({});".format(filepath1))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(370, 40, 481, 291))
        self.graphicsView_2.setStyleSheet("border-image: url({});".format(filepath2))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(770, 340, 71, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "*/.txt文本格式如下："))
        self.label_2.setText(_translate("Dialog", "*/.csv文件格式如下："))


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
class sample(QtWidgets.QMainWindow, Ui_Dialog_sample):
    def __init__(self,filepath1,filepath2,parent=None):
        super(sample, self).__init__(parent)
        self.setupUi(self,filepath1,filepath2)
        self.setWindowTitle("格式提醒！")
        self.setWindowIcon((QIcon("./piliang_ico/Toolsnet.png")))
        self.pushButton.setStyleSheet(buttonstyle)
        self.pushButton.clicked.connect(self.close)
        self.setFixedSize(self.width(),self.height())
    
# app = QtWidgets.QApplication(sys.argv)
# win=sample()
# win.show()
# sys.exit(app.exec_())
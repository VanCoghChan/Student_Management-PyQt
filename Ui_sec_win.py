# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PyQt5\test.ui\sec_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from rebuild_tablewidget_2 import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(945, 546)
        self.tableWidget = tablewidget(Dialog)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(270, 10, 670, 531))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./piliang_ico/Credit_Card.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./piliang_ico/ID_128px_1179915_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./piliang_ico/physics__easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./piliang_ico/maths_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./piliang_ico/mathematics.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./piliang_ico/educational_net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 251, 531))
        self.treeWidget.setStyleSheet("border-image: url(./piliang_ico/1.jpg);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./piliang_ico/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap("./piliang_ico/timg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon6)
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(0, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./piliang_ico/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon7)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./piliang_ico/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon8)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./piliang_ico/字母_a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon9)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./piliang_ico/字母_b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./piliang_ico/Graph_.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon11)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon5)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./piliang_ico/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon12)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./piliang_ico/添加1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon13)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./piliang_ico/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon14)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./piliang_ico/database.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon15)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./piliang_ico/txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon16)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("./piliang_ico/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon17)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("./piliang_ico/xlsx.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        item_1.setIcon(0, icon18)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "大学物理"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "离散数学"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "线性代数"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "平均成绩"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "学生信息管理"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "刷新"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "查询"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Dialog", "按学号"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Dialog", "按姓名"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Dialog", "可视化学生成绩分布"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Dialog", "大学物理"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Dialog", "离散数学"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Dialog", "线性代数"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("Dialog", "平均成绩"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Dialog", "添加"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("Dialog", "手动添加"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("Dialog", "文件导入"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("Dialog", "成绩导出"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("Dialog", "导出为 */.txt"))
        self.treeWidget.topLevelItem(4).child(1).setText(0, _translate("Dialog", "导出为 */.csv"))
        self.treeWidget.topLevelItem(4).child(2).setText(0, _translate("Dialog", "导出为 */.xlsx"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

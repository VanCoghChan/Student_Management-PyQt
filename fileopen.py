import codecs
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog


class Ui_fileopen(object):
    def setupUi(self,dialog):
        pass

    def retranslateUi(self, dialog):
            _translate = QtCore.QCoreApplication.translate
            dialog.setWindowTitle(_translate("dialog", "Dialog"))
 

class fileopen_1(QtWidgets.QMainWindow, Ui_fileopen):
    def __init__(self):
        super(fileopen_1, self).__init__()
        self.setupUi(self)
    
    def read_file(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                    "选取文件",
                    "./",
                    "Text Files (*.txt);;Csv Files (*.csv)")  #设置文件扩展名过滤,注意用双分号间隔
        
        try:
            if fileName.endswith('.txt'):
                with open(fileName,'r',encoding='utf-8-sig') as info:
                    info=info.readlines()
                    info=[x.strip() for x in info]
                    info=[info[i:i+7] for i in range(0,len(info)-7,7)]
                    return info
            elif fileName.endswith('.csv'):
                with codecs.open(fileName,'r') as info:
                    # info=[each for each in csv.reader(info)]
                    info=[x for x in csv.reader(info)]
                    if not info[0][0].isdigit():
                        info=info[1:]
                    return info
                        
        except Exception as e:
            QMessageBox.warning(self,"警告！","导入失败！请检查文件格式是否正确或编码格式是否为‘UTF-8’")


class fileopen_2(QtWidgets.QMainWindow, Ui_fileopen):
    def __init__(self):
        super(fileopen_2, self).__init__()
        self.setupUi(self)
    
    def read_file(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                    "选取文件",
                    "./",
                    "Text Files (*.txt);;Csv Files (*.csv)") 
        try:
            if fileName.endswith('.txt'):
                with open(fileName,'r',encoding='utf-8-sig') as info:
                    info=info.readlines()
                    info=[x.strip() for x in info]
                    info=[info[i:i+6] for i in range(0,len(info)-6,6)]
                    return info
            elif fileName.endswith('.csv'):
                with codecs.open(fileName,'r') as info:
                    info=[x for x in csv.reader(info)]
                    if not info[0][0].isdigit():
                        info=info[1:]
                    return info

        except:
            QMessageBox.warning(self,"警告！","请检查文件格式是否正确或编码格式是否为‘UTF-8’")


# if __name__=="__main__": 
#   import sys 
#   app=QtWidgets.QApplication(sys.argv) 
#   myshow=fileopen()
#   myshow.show()
#   sys.exit(app.exec_()) 

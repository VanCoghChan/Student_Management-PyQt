import codecs
import os
import sys

import easygui as eg
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

from draw import *
from Ui_show_pic import Ui_Dialog_pic


class show_pic(QtWidgets.QMainWindow, Ui_Dialog_pic):
    def __init__(self,class_,parent=None):
        super(show_pic,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('数据可视化')
        self.setWindowIcon(QIcon(('./piliang_ico/Toolsnet.png')))
        self.resize(900, 600)
        self.setFixedSize(900,600)
        self.class_=class_
        self.data=self.get_data(self.class_)
        self.reflash_view_1()   #设置默认绘图为玫瑰饼状图
        self.pushButton.clicked.connect(self.reflash_view_1)
        self.pushButton_2.clicked.connect(self.reflash_view_2)
        self.pushButton_3.clicked.connect(self.reflash_view_3)

    def reflash_view_1(self):
        draw_pic(self.data,self.class_,'pie')
        url = 'file:///{}/render.html'.format(os.getcwd()).replace('\\','/')
        self.textBrowser.setUrl(QUrl(url))

    def reflash_view_2(self):
        draw_pic(self.data,self.class_,'bar')
        url = 'file:///{}/render.html'.format(os.getcwd()).replace('\\','/')
        self.textBrowser.setUrl(QUrl(url))

    def reflash_view_3(self):
        draw_pic(self.data,self.class_,'bar3D')
        url = 'file:///{}/render.html'.format(os.getcwd()).replace('\\','/')
        self.textBrowser.setUrl(QUrl(url))

    def get_data(self,class_):
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='Achencan123',
            db='test',
            port=3306
        )
        cur=db.cursor()
        try:
            cur.execute("select * from score_info")
            data=cur.fetchall()
        except Exception as e:
            raise e
            db.rollback()
        finally:
            db.close()

        if class_=='大学物理':
            data=[x[2] for x in data]
        elif class_=='离散数学':
            data=[x[3] for x in data]
        elif class_=='线性代数':
            data=[x[4] for x in data]
        elif class_=='平均成绩':
            data=[x[5] for x in data]
        data=[eval(x) for x in data]
        return data
        

# app = QApplication(sys.argv)
# window = show_pic()
# window.show()
# app.exec_()

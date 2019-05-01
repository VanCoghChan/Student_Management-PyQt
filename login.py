#login.py

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QVBoxLayout, QWidget)

from first_win import *
from get_userpwd import get_userpwd
from Header import FramelessWindow, TitleBar

StyleSheet = """
/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
}
/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {

    color: white;
}
#buttonClose:hover {
    color: white;
}
/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {

}
#buttonClose:pressed {
    color: white;

}
"""   #标题栏Button的样式

StyleSheet_2 = """
QComboBox{
        height: 20px;
        border-radius: 4px;
        border: 1px solid rgb(111, 156, 207);
        background: rgb(22,22,22,50);
}
QComboBox:enabled{
        color: white,
        font-size:10px;
}
QComboBox:!enabled {
        color: rgb(80, 80, 80);
}
QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(225,22,173,255),
        font-size:10px
}
QComboBox::drop-down {
        background: transparent;
}
QComboBox::drop-down:hover {
        background: lightgrey;
}

QComboBox QAbstractItemView {
        border: 1px solid rgb(111, 156, 207);
        background: white;
        outline: none;
}
"""
StyleSheet_3 = """
QLineEdit {
        border-radius: 4px;
        height: 20px;
        border: 1px solid rgb(111, 156, 207);
        background: rgb(22,22,22,50);
}
QLineEdit:enabled {
        color: rgb(84, 84, 84);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(51, 51, 51);
}
QLineEdit:!enabled {
        color: rgb(80, 80, 80);
}


"""   #QComobox和QLineEdite的样式

StyleSheet_btn = """
QPushButton{
    height:30px;
    background-color: transparent;
    color:orange;
    font-size:20px;
    font-family:Arial;
    border: 3px solid #555555;
    border-radius: 7px;

}
QPushButton:hover {
    background-color: rgb(245,48,48,70);
    border-radius: 7px;

}
"""  #登录Button的样式

class loginWnd(QWidget):
    '''登录窗口'''
    def __init__(self, *args, **kwargs):
        super(loginWnd, self).__init__()
        self._layout = QVBoxLayout(spacing=0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)
        self.setWindowOpacity(0.1)

        self.setLayout(self._layout)
        self.data=list(get_userpwd())
        self._setup_ui()
        self.add_item_his()
        self.login_btn.clicked.connect(self.check)

        

    def keyPressEvent(self, event):
        if str(event.key()) == "16777220":
            self.check()
        
    def write_usr_his(self,usrname):
        with open('usr_his.txt','a+') as usr_his:
                usr_his.write(usrname)
                usr_his.write("\n")

    def add_item_his(self):
            db=pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Achencan123',
                    db='test',
                    port=3306
            )
            cur=db.cursor()
            try:
                    cur.execute("select * from usr")
                    users=cur.fetchall()
            except Exception as e:
                    print(e)
            finally:
                    db.close()
                    self.name_box.clear()
                    for item in users:
                            self.name_box.addItem(item[0].strip())
        #     with open('usr_his.txt','r') as usr_his:
        #             usr_his=set(usr_his.readlines())
        #             self.name_box.clear()
        #             for item in usr_his:
        #                     self.name_box.addItem(item.strip())
    windowList = []
    def check(self):
        self.name_box.setEditable(True)
        username=self.name_box.currentText()
        pwd=self.passwd_box.text()
        for item in self.data:
                if username==item[0] and pwd==item[1]:
                        self.write_usr_his(username)
                        self.add_item_his()
                        self.name_box.clearEditText()
                        self.passwd_box.clear()
                        the_window =mywindow()
                        self.windowList.append(the_window)   ##注：没有这句，是不打开另一个主界面的！
                        login_close(mainWnd)
                        the_window.show()
                        break
        else:
                QMessageBox.warning(self,"提示","输入的用户或者密码错误!")
              

    def _setup_ui(self):

        self.main_layout = QGridLayout()

        self.main_layout.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel('Username: ')
        self.name_label.setStyleSheet("QLabel{color:rgb(255,48,48,250);font-size:20px;font-weight:normal;font-family:Arial;}")
        self.passwd_label = QLabel('Password: ')
        self.passwd_label.setStyleSheet("QLabel{color:rgb(255,48,48,250);font-size:20px;font-weight:normal;font-family:Arial;}")

        self.name_box = QComboBox()
        self.name_box.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.name_box.setFont(font)
        self.passwd_box = QLineEdit()
        self.passwd_box.setEchoMode(QLineEdit.Password)
        self.passwd_box.setFont(font)
        self.name_box.setStyleSheet(StyleSheet_2)
        self.passwd_box.setStyleSheet(StyleSheet_3)

        self.label = QLabel()
        self.login_btn = QPushButton("Login")
        self.login_btn.setStyleSheet(StyleSheet_btn)

        self.main_layout.addWidget(self.name_label,0,0,1,1)
        self.main_layout.addWidget(self.passwd_label,1,0,1,1)
        self.main_layout.addWidget(self.name_box,0,1,1,2)
        self.main_layout.addWidget(self.passwd_box,1,1,1, 2)
        self.main_layout.addWidget(self.label,3,0,1,3)
        self.main_layout.addWidget(self.login_btn,4,0,1,3)

        self._layout.addLayout(self.main_layout)

def login_close(win):
        win.close()


app = QApplication(sys.argv)

mainWnd = FramelessWindow()
mainWnd.setWindowTitle('  登录 / Login')
mainWnd.setWindowIcon(QIcon('./piliang_ico./Toolsnet.png'))
mainWnd.setFixedSize(QSize(500,350))  
mainWnd.setWidget(loginWnd(mainWnd))  # 把自己的窗口添加进来
mainWnd.show()

sys.exit(app.exec_())

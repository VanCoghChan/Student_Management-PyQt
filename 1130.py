import sys
import codecs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_1130 import Ui_MainWindow
from Ui_1130_1 import *

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__() 
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        self.linetext=''
        self.stu_info=self.read_info()
        self.tableWidget.setRowCount(len(self.stu_info))
        
        for i in range(len(self.stu_info)):
            cb=QCheckBox('是否删除?')
            self.tableWidget.setCellWidget(i,4,cb)
            for j in range(len(self.stu_info[i])):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(self.stu_info[i][j])))
        self.D1 = Dialog1() 
        self.D2 = Dialog2()
        self.treeWidget.clicked.connect(self.gettreeitem)
        self.treeWidget.doubleClicked.connect(self.openDialog)
         
    def read_info(self):
        with open(u'info.txt',encoding='gbk',errors="ignore") as info:
            info=[x.strip('\n') for x in info.readlines()]
            info=[info[i:i+4] for i in range(0,len(info),4)]
            return info

    def gettreeitem(self):
        item=self.treeWidget.currentItem()
        print(item.text(0))
        return item.text(0)

    def openDialog(self):
        def func1():
            self.linetext=self.D1.get_text()
            for i in self.stu_info:
                if i[0]==self.linetext:
                    self.tableWidget.setRowCount(1)
                    for j in range(4):
                        self.tableWidget.setItem(0,j,QTableWidgetItem(i[j]))
                    break
            else:
                QMessageBox.warning(self,"提示","未查找到此姓名!")

        def func2():
            self.linetext=self.D2.get_text()
            for i in self.stu_info:
                if i[1]==self.linetext:
                    self.tableWidget.setRowCount(1)
                    for j in range(4):
                        self.tableWidget.setItem(0,j,QTableWidgetItem(i[j]))
                    break
            else:
                QMessageBox.information(self,"提示",'未查找到此学号!')

        if self.gettreeitem()=='按姓名':
            self.D1.show()
            self.D1.pushButton.clicked.connect(func1)
            self.D1.pushButton.clicked.connect(self.D1.close)
        elif self.gettreeitem()=='按学号':
            self.D2.show()
            self.D2.pushButton.clicked.connect(func2)
            self.D2.pushButton.clicked.connect(self.D2.close)
      
app = QtWidgets.QApplication(sys.argv)
win=mywindow()
win.show()
sys.exit(app.exec_())




# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys

# class MyTable(QTableWidget):
#     def __init__(self,parent=None):
#         super(MyTable, self).__init__(parent)
#         self.setWindowTitle("我是一个表格")
#         self.setWindowIcon(QIcon("male.png"))
#         self.resize(920, 240)
#         self.setColumnCount(5)
#         self.setRowCount(2)
#         #设置表格有两行五列。
#         self.setColumnWidth(0, 200)
#         self.setColumnWidth(4, 200)
#         self.setRowHeight(0, 100)
#         #设置第一行高度为100px，第一列宽度为200px。

#         self.table()

#     def table(self):
#         self.setItem(0,0,QTableWidgetItem("           你的名字"))
#         self.setItem(0,1,QTableWidgetItem("性别"))
#         self.setItem(0,2,QTableWidgetItem("出生日期"))
#         self.setItem(0,3, QTableWidgetItem("职业"))
#         self.setItem(0,4, QTableWidgetItem("收入"))
#         #添加表格的文字内容.
#         self.setHorizontalHeaderLabels(["第一行", "第二行", "第三行", "第四行", "第五行"])
#         self.setVerticalHeaderLabels(["第一列", "第二列"])
#         #设置表头
#         lbp = QLabel()
#         lbp.setPixmap(QPixmap("Male.png"))
#         self.setCellWidget(1,1,lbp)
#         #在表中添加一张图片
#         twi = QTableWidgetItem("      新海诚")
#         twi.setFont(QFont("Times", 10, ))
#         self.setItem(1,0,twi)
#         #添加一个自己设置了大小和类型的文字。
#         dte = QDateTimeEdit()
#         dte.setDateTime(QDateTime.currentDateTime())
#         dte.setDisplayFormat("yyyy/MM/dd")
#         dte.setCalendarPopup(True)
#         self.setCellWidget(1,2,dte)
#         #添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
#         cbw = QComboBox()
#         cbw.addItem("医生")
#         cbw.addItem("老师")
#         cbw.addItem("律师")
#         self.setCellWidget(1,3,cbw)
#         #添加了一个下拉选择框
#         sb = QSpinBox()
#         sb.setRange(1000,10000)
#         sb.setValue(5000)#设置最开始显示的数字
#         sb.setDisplayIntegerBase(10)#这个是显示数字的进制，默认是十进制。
#         sb.setSuffix("元")#设置后辍
#         sb.setPrefix("RMB: ")#设置前辍
#         sb.setSingleStep(100)
#         self.setCellWidget(1,4,sb)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myTable = MyTable()
#     myTable.show()
#     app.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon, QBrush, QColor
# from PyQt5.QtCore import Qt
# class TreeWidgetDemo(QMainWindow):
#     def __init__(self, parent=None):
#         super(TreeWidgetDemo, self).__init__(parent)
#         self.setWindowTitle('TreeWidget 例子')

#         self.tree=QTreeWidget()
#         #设置列数
#         self.tree.setColumnCount(2)
#         #设置树形控件头部的标题
#         self.tree.setHeaderLabels(['Key','Value'])

#         #设置根节点
#         root=QTreeWidgetItem(self.tree)
#         root.setText(0,'Root')
#         root.setIcon(0,QIcon('./images/root.png'))

#         # todo 优化2 设置根节点的背景颜色
#         brush_red=QBrush(Qt.red)
#         root.setBackground(0,brush_red)
#         brush_blue=QBrush(Qt.blue)
#         root.setBackground(1,brush_blue)

#         #设置树形控件的列的宽度
#         self.tree.setColumnWidth(0,150)

#         #设置子节点1
#         child1=QTreeWidgetItem()
#         child1.setText(0,'child1')
#         child1.setText(1,'ios')
#         child1.setIcon(0,QIcon('./images/IOS.png'))

#         #todo 优化1 设置节点的状态
#         child1.setCheckState(0,Qt.Checked)

#         root.addChild(child1)

#         #设置子节点2
#         child2=QTreeWidgetItem(root)
#         child2.setText(0,'child2')
#         child2.setText(1,'')
#         child2.setIcon(0,QIcon('./images/android.png'))

#         #设置子节点3
#         child3=QTreeWidgetItem(child2)
#         child3.setText(0,'child3')
#         child3.setText(1,'android')
#         child3.setIcon(0,QIcon('./images/music.png'))

#         #加载根节点的所有属性与子控件
#         self.tree.addTopLevelItem(root)

#         #TODO 优化3 给节点添加响应事件
#         self.tree.clicked.connect(self.onClicked)

#         #节点全部展开
#         self.tree.expandAll()
#         self.setCentralWidget(self.tree)

#     def onClicked(self,qmodeLindex):
#         item=self.tree.currentItem()
#         print('Key=%s,value=%s'%(item.text(0),item.text(1)))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     tree = TreeWidgetDemo()
#     tree.show()
#     sys.exit(app.exec_())



# demo_14:关于TableWidGet的使用，注意：在table表头分为水平和垂直两种，及horizontal header和vertical header两类。

# from PyQt5.QtWidgets import (QTableWidget,QApplication,QWidget,QTableWidgetItem,QHBoxLayout)
# from PyQt5.QtCore import Qt
# import PyQt5.QtGui as QtGui

# import sys
# class Example(QWidget):
#     data=[{'num':'101','name':'JONES','sal':200,'date':'1999-10-10','sex':'女'},
#           {'num': '102', 'name': 'SITH', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#           {'num': '103', 'name': 'SDF', 'sal': 200, 'date': '1999-12-10', 'sex': '女'},
#           {'num': '104', 'name': 'JSSS', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#           {'num': '105', 'name': 'JEEE', 'sal': 200, 'date': '1912-10-10', 'sex': '女'}
#           ]

#     def __init__(self):
#             super().__init__()
#             self.initUI()

#     def initUI(self):
#             titles = ['编号', '姓名', '工资', '入职日期', ' 性别']
#             self.setWindowTitle('员工信息')
#             self.table = QTableWidget()
#             self.table.setRowCount(9)                                   #行下标最大值
#             self.table.setColumnCount(5)                                #列
#             self.table.setHorizontalHeaderLabels(titles)                #标题列


#             #表格或者窗体背景图片
#             palette =  QtGui.QPalette()
#             icon =  QtGui.QPixmap('a.jpg')
#             palette.setBrush(self.table.backgroundRole(),  QtGui.QBrush(icon))  # 添加背景图片
#             self.setPalette(palette)
#             #表格行
#             self.table.horizontalHeader().setStyleSheet("background-color: gray");
#             # self.table.setEditTriggers(QTableWidget.NoEditTriggers)#单元格不可编辑
#             # self.table.setSelectionBehavior(QTableWidget.SelectRows)  #选中列还是行，这里设置选中行
#             # self.table.setSelectionMode(QTableWidget.SingleSelection) #只能选中一行或者一列
#             #self.table.horizontalHeader().setStretchLastSection(True)  #列宽度占满表格(最后一个列拉伸处理沾满表格)
#             #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);#所有列自适应表格宽度

#             #1、设置每一个标题单元格样式
#             # for i in range(self.table.columnCount()):
#             #       headItem = self.table.horizontalHeaderItem(i)
#             #       headItem.setFont(QFont("song", 14, QFont.Bold))
#             #       headItem.setForeground(QBrush(Qt.gray))
#             #       headItem.setBackgroundColor(QColor(0, 60, 10))      # 设置单元格背景颜色
#             #       #headItem.setTextColor(QColor(200, 111, 30))        # 设置文字颜色
#             #       headItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

#             #2、设置整个表格列标题样式
#             font = self.table.horizontalHeader().font()
#             font.setBold(True)
#             self.table.horizontalHeader().setFont(font)
#             #self.table.setFrameShape(QFrame.NoFrame)                   #设置表格外层无边框
#             #self.table.setShowGrid(False)                              #是否显示单元格网格线False 则不显示
#             #self.table.horizontalHeader().setHighlightSections(False)  #设置表格列头不塌陷
#             #self.table.horizontalHeader().setFixedHeight(35)           #设置表列头高度
#             #self.table.horizontalHeader().setVisible(False)            #设置隐藏列头
#             #self.table.horizontalHeader().setFixedWidth(820)           #设置列标题头所在行，宽度（没啥用）


#             #设置表格的滚动调样式：self.table.horizontalScrollBar().setStyleSheet.... ,窗体的也可以设置：self.horizontalScrollBar().setStyleSheet...
#             self.table.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
#                                                 "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
#                                                 "QScrollBar::handle:hover{background:gray;}"
#                                                 "QScrollBar::sub-line{background:transparent;}"
#                                                 "QScrollBar::add-line{background:transparent;}");
#             self.table.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
#                                                 "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
#                                                 "QScrollBar::handle:hover{background:gray;}"
#                                                 "QScrollBar::sub-line{background:transparent;}"
#                                                 "QScrollBar::add-line{background:transparent;}");
#             #遍历数据，并形成行索引，列索引；
#             item = [(j, c,Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)]
#             print(item)
#             for v in item:
#                 #   print('行下标%s,列下标%s,值：%s' % (v[1], v[0], list(v[2])[v[0]]))
#                 print(v)
#                 print(str(list(v[2])[v[0]]))
#                 print(v[1],v[0])
#                 self.table.setItem(v[1], v[0], QTableWidgetItem(str(list(v[2])[v[0]]))) #注意，纯数值，则需要str否则放不进去，不显示
#                 self.table.setColumnWidth(v[0], 120)                                    #设置列宽度，列索引，宽度
#                 self.table.setRowHeight(v[1], 20)                                       #设置行高度，行索引，高度
#                 # 设置入职日期列，居中
#                 #print(type(self.table.item(v[1], 2)),v[1])
#                 if self.table.item(v[1], 3):
#                     self.table.item(v[1], 3).setTextAlignment(Qt.AlignHCenter)
#             row_count = self.table.rowCount()
#             self.table.insertRow(row_count)

#             mainLayout = QHBoxLayout()
#             mainLayout.addWidget(self.table)
#             self.setLayout(mainLayout)
#             self.setGeometry(200,300,600,400)
#             self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     e = Example()
#     sys.exit(app.exec_())

# 测试循环遍历上面集合，按照下标直接定位每一个元素的值
# data = [{'num': '101', 'name': 'JONES', 'sal': 200, 'date': '1999-10-10', 'sex': '女'},
#         {'num': '102', 'name': 'SITH', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#         {'num': '103', 'name': 'SDF', 'sal': 200, 'date': '1999-12-10', 'sex': '女'},
#         {'num': '104', 'name': 'JSSS', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#         {'num': '105', 'name': 'JEEE', 'sal': 200, 'date': '1912-10-10', 'sex': '女'}
#         ]
# print([(j, c, Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)])
# for v in [(j, c, Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)]:
# print('行下标%s,列下标%s,值：%s' % (v[1], v[0], list(v[2])[v[0]]))






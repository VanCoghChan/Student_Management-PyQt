import codecs
import sys

import easygui as eg
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from fileopen import *
from sec_win import *
from Ui_1130_1 import *
from Ui_1219 import *
from Ui_add1 import *
from Ui_sample_info import *


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__() 
        self.setupUi(self)
        self.setWindowIcon(QIcon(('./piliang_ico/Toolsnet.png')))
        self.setWindowTitle('学生管理 Client')
        self.treeWidget.expandAll()
        self.setFixedSize(self.width(),self.height())
        self.flash_table()
        self.treeWidget.doubleClicked.connect(self.item_reaction)
        

    def flash_table(self):
        self.info=self.get_basedinfo_from_db()
        self.stu_id=[x[0] for x in self.info]
        self.tableWidget.setRowCount(len(self.info))
        for i in range(len(self.info)):
            for j in range(len(self.info[i])):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(self.info[i][j])))
        
    def select_byname(self):
        self.linetext=self.D1.get_text().strip()
        list_1=[]
        for i in self.info:
            if i[1]==self.linetext:
                list_1.append(i)
        if len(list_1)!=0:
            self.tableWidget.setRowCount(len(list_1))
            flag=0
            for i in list_1:
                for j in range(7):
                    self.tableWidget.setItem(flag,j,QTableWidgetItem(i[j]))
                flag+=1
                
        else:
            QMessageBox.warning(self,"提示","未查找到此姓名!")

    def select_byid(self):
        self.linetext=self.D2.get_text().strip()
        for i in self.info:
            if i[0]==self.linetext:
                self.tableWidget.setRowCount(1)
                for j in range(7):
                    self.tableWidget.setItem(0,j,QTableWidgetItem(i[j]))
                break
        else:
            QMessageBox.warning(self,"提示",'未查找到此学号!')
    
    def item_reaction(self):
        item=self.get_item()
        if item=='刷新':
            self.flash_table()
        elif item=='按学号':
            self.D2=Dialog2()
            self.D2.show()
            self.D2.pushButton.clicked.connect(self.select_byid)
            self.D2.pushButton.clicked.connect(self.D2.close)
        elif item=='按姓名':
            self.D1=Dialog1()
            self.D1.show()
            self.D1.pushButton.clicked.connect(self.select_byname)
            self.D1.pushButton.clicked.connect(self.D1.close)
        elif item=='手动添加':
            self.Add_d1=Add_d1()
            self.Add_d1.show()
            self.Add_d1.pushButton.clicked.connect(self.Add_d1_reaction)
            # self.Add_d1.pushButton.clicked.connect(self.Add_d1.close)
        elif item=='文件导入':
            def func():
                Add_d2=fileopen_1()
                self.filevalues=Add_d2.read_file()
                self.Add_d2_reaction()
                self.flash_table()
            # QMessageBox.information(self,"提示!","目前仅支持从*.txt / *.csv文件导入,并且确保文件格式正确!")
            self.sample_info=sample('./piliang_ico/sample_txt1.JPG','./piliang_ico/sample_csv1.JPG')
            self.sample_info.show()
            self.sample_info.pushButton.clicked.connect(func)
        elif item=='切换为成绩信息':
            self.secwin=sec_win(self)
            self.secwin.show()

    
    def Add_d1_reaction(self):
        stu_id=''.join(self.Add_d1.lineEdit1.text().split())
        name=self.Add_d1.lineEdit2.text().strip()
        sex=self.Add_d1.comboBox1.currentText()
        age=self.Add_d1.comboBox2.currentText()
        date=self.Add_d1.dateEdit.text()[:-4]
        email=self.Add_d1.lineEdit3.text().strip()
        phone=self.Add_d1.lineEdit4.text().strip()
        if stu_id not in self.stu_id:
            if stu_id!='' and name!='' and sex!='' and age!='' and date!='' and email!='' and phone !='':
                if email.endswith('.com'):
                    db=pymysql.connect(
                        host='localhost',
                        user='root',
                        password='Achencan123',
                        db='test',
                        port=3306
                    )
                    cur=db.cursor()
                    sql_pattren="""
                    insert into based_info values(
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}'
                        )
                    """
                    sql_line=sql_pattren.format(stu_id,name,sex,age,date,email,phone)
                    try:
                        cur.execute(sql_line)
                        db.commit()
                    except:
                        db.rollback()
                    finally:
                        QMessageBox.information(self,"提示!","Success! 录入成功！")
                        db.close()
                        self.Add_d1.close()
                else:
                    QMessageBox.warning(self,"警告!","非法邮件格式！")
                self.Add_d1.raise_()
            else:
                QMessageBox.warning(self,"警告!","请填写完整信息！")
                self.Add_d1.raise_()
        else:
            QMessageBox.warning(self,"警告!","请勿重复录入同一学号！")
            self.Add_d1.raise_()
        self.flash_table()

    def Add_d2_reaction(self):
        if self.filevalues is not None and self.filevalues!=[]:
            db=pymysql.connect(
                host='localhost',
                user='root',
                password='Achencan123',
                db='test',
                port=3306
            )
            cur=db.cursor()
            sql_pattren="""
                insert into based_info values(
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}'
                )
            """

            if len(self.filevalues[0])%7==0 and self.filevalues[0][2] in ['男','女']:
                try:
                    count1=0
                    for each in self.filevalues:
                        stu_id=str(each[0])
                        if stu_id not in self.stu_id:
                            name=str(each[1])
                            sex=str(each[2])
                            age=str(each[3])
                            date=str(each[4])
                            email=str(each[5])
                            phone=str(each[6])
                            # print(sql_pattren.format(stu_id,name,sex,age,date,email,phone))
                            cur.execute(sql_pattren.format(stu_id,name,sex,age,date,email,phone))
                            db.commit()
                            count1+=1
                    count2=len(self.filevalues)-count1
                    QMessageBox.information(self,"提示!","成功导入{}条数据！其中{}条数据被过滤(原因:数据重复)".format(str(count1),str(count2)))
                except Exception as e:
                    print(e)
                    db.rollback()
                    QMessageBox.warning(self,"警告!","文件格式错误！请检查文件格式和编码格式是否为‘UTF-8’")
                finally:
                    db.close()
            else:
                QMessageBox.warning(self,"警告!","文件格式错误！请检查文件格式和编码格式是否为‘UTF-8’")

    def get_item(self):
        Item_list=self.treeWidget.selectedItems()  #return the selected item as a list
        for ii in Item_list:
            print(ii.text(0))
            return ii.text(0)
            continue

    def get_basedinfo(self): #从文本中读取信息
        with open('info1.txt','r',encoding='utf-8',errors='ignore') as info:
            info=info.readlines()
            info=[x.strip() for x in info]
            info=[info[i:i+7] for i in range(0,len(info)-7,7)]
            return info

    def get_basedinfo_from_db(self):
        db=pymysql.connect(
        host='localhost',
        user='root',
        password='Achencan123',
        db='test',
        port=3306
        )
        cur=db.cursor()
        try:
            cur.execute("select * from based_info")
            data=cur.fetchall()
            return data
        except Exception as e:
            print(e)
        finally:
            db.close()



# app = QtWidgets.QApplication(sys.argv)
# win=mywindow()
# win.show()
# sys.exit(app.exec_())


############################################

# from random import choice

# with open('stu_info.txt','w',encoding='utf-8') as info:
#     for i in range(1,1001):
#         info.write(str(631707060602+i)+'\n')
#         info.write('cchan'+str(i)+'\n')
#         info.write(choice(['男','女'])+'\n')
#         info.write(str(choice([x for x in range(18,25)]))+'\n')
#         info.write('2000-07-26'+'\n')
#         info.write('ccisahack@outlook.com'+'\n')
#         info.write('15123191093'+'\n')


# with open('score.txt','w+',encoding='utf-8') as score:
#     with open('名单.txt','r') as in_:
#         in_=[x.split() for x in in_.readlines()]
#         for each in in_:
#             id_=each[0]
#             name=each[1]
#             phy=choice(list(range(0,100)))
#             dis=choice(list(range(0,100)))
#             liner=choice(list(range(0,100)))
#             score.write(id_+'\n')
#             score.write(name+'\n')
#             score.write(str(phy)+'\n')
#             score.write(str(dis)+'\n')
#             score.write(str(liner)+'\n')
#             score.write('{:.1f}\n'.format((phy+dis+liner)/3))
            

# import pymysql
# from random import choice
# db=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='Achencan123',
#     db='test',
#     port=3306
# )
# cur=db.cursor()
# try:
#     sql_line="""
#     insert into based_info values(
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}'
#     )
#     """
#     for i in range(100):
#         id_=str(631707060602+i)
#         name=str('cchan'+str(i))
#         sex=choice(['男','女'])
#         age=choice(list(range(18,25)))
#         date='2000-07-26'
#         email='ccisahack@Outlook.com'
#         phone='15123191093'
#         print(sql_line.format(id_,name,sex,age,date,email,phone))
#         cur.execute(sql_line.format(id_,name,sex,age,date,email,phone))
#     db.commit()
# except Exception as e:
#     raise e
#     db.rollback()
# finally:
#     db.close()


# import pymysql
# db=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='Achencan123',
#     db='test',
#     port=3306
# )
# cur=db.cursor()
# try:
#     cur.execute("select * from based_info")
#     data=cur.fetchall()
#     print(data)
# except Exception as e:
#     raise e
# finally:
#     db.close()


# import pymysql
# from random import choice
# db=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='Achencan123',
#     db='test',
#     port=3306
# )
# cur=db.cursor()
# try:
#     sql_line="""
#     insert into based_info values(
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}',
#         '{}'
#     )
#     """
#     for i in range(10000):
#         id_=str(631707060602+i)
#         name=str('cchan'+str(i))
#         sex=choice(['男','女'])
#         age=choice(list(range(18,25)))
#         date='{}-{}-{}'.format(choice(list(range(1995,2002))), choice(list(range(1,13))), choice(list(range(1,29))))
#         email='ccisahack@Outlook.com'
#         phone='15123191093'
#         print(sql_line.format(id_,name,sex,age,date,email,phone))
#         cur.execute(sql_line.format(id_,name,sex,age,date,email,phone))
#     db.commit()
# except Exception as e:
#     raise e
#     db.rollback()
# finally:
#     db.close()

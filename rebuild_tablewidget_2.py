import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QAction, QDockWidget, QFileDialog, QLineEdit,
                             QListWidget, QMenu, QMessageBox)

from Ui_Add_2 import *


class tablewidget(QtWidgets.QTableWidget):
    def __init__(self,parent=None):
        super(tablewidget, self).__init__(parent)
        self.flashInfo()

    def flashInfo(self):
        db=pymysql.connect(
                host='localhost',
                user='root',
                password='Achencan123',
                db='test',
                port=3306
                )
        cur=db.cursor()
        try:
            cur.execute("select id from score_info")
            allIDs=cur.fetchall()
            self.allIDs=[]
            for i in allIDs:self.allIDs.append(i[0])
        finally:
            db.close()

    def contextMenuEvent(self, event):
        self.hitIndex = self.indexAt(event.pos()).row()
        if self.hitIndex > -1:
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除",pmenu)
            pAlterAct = QAction("修改",pmenu)
            pmenu.addAction(pAlterAct)
            pmenu.addAction(pDeleteAct)        
            pDeleteAct.triggered.connect(self.remove_row)
            pAlterAct.triggered.connect(self.alter_row)
            pmenu.popup(self.mapToGlobal(event.pos()))


    def alter_row(self):
        RowInfo=[]
        for i in range(6):
            RowInfo.append(self.item(self.hitIndex,i).text())
        self.Id=RowInfo[0]
        self.alterdialog=Add_d2()
        self.alterdialog.setWindowTitle("修改信息")
        self.alterdialog.lineEdit_1.setText(RowInfo[0])
        self.alterdialog.lineEdit_2.setText(RowInfo[1])
        self.alterdialog.lineEdit_3.setText(RowInfo[2])
        self.alterdialog.lineEdit_4.setText(RowInfo[3])
        self.alterdialog.lineEdit_5.setText(RowInfo[4])
        self.alterdialog.show()
        self.alterdialog.raise_()
        self.alterdialog.pushButton.clicked.connect(self.alter_reaction)

            
    def remove_row(self):
        button = QMessageBox.warning(self,"Warning","该操作会删除本行学生信息，是否继续操作？",QMessageBox.Ok|QMessageBox.Cancel)
        if button==QMessageBox.Ok:
            del_id=self.item(self.hitIndex,0).text()
            self.sql_del_opt(del_id)

    def alter_reaction(self):
        stu_id=self.alterdialog.lineEdit_1.text()
        name=self.alterdialog.lineEdit_2.text()
        phy=self.alterdialog.lineEdit_3.text()
        dis=self.alterdialog.lineEdit_4.text()
        liner=self.alterdialog.lineEdit_5.text()
        ave=round((int(phy)+int(dis)+int(liner))/3, 1)
        if stu_id not in self.allIDs or stu_id==self.Id:
            if stu_id!='' and name!='' and phy!='' and dis!='' and liner!='':
                db=pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Achencan123',
                    db='test',
                    port=3306
                )
                cur=db.cursor()
                sql_pattren="""
                insert into score_info values(
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}'
                )
                """
                sql_line=sql_pattren.format(stu_id,name,phy,dis,liner,ave)
                try:
                    cur.execute("delete from score_info where id='{}'".format(self.Id))
                    cur.execute(sql_line)
                    db.commit()
                    QMessageBox.information(self,"提示!","Success! 修改成功！")
                except Exception as e:
                    print(e)
                    db.rollback()
                finally:
                    db.close()
                    self.alterdialog.close()
            else:
                QMessageBox.warning(self,"警告!","请填写完整信息！")
                self.alterdialog.raise_()
        else:
            QMessageBox.warning(self,"警告!","此学号已被占用！如需使用请先删除该学号原有信息！")
            self.alterdialog.raise_()
        self.flashInfo()

    def sql_del_opt(self,del_id):
        db=pymysql.connect(
        host='localhost',
        user='root',
        password='Achencan123',
        db='test',
        port=3306
        )
        cur=db.cursor()
        sql_pattern="""
        delete from score_info where id='{}';
        """
        try:
            sql_del=sql_pattern.format(del_id)
            cur.execute(sql_del)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            self.removeRow(self.hitIndex)
            QMessageBox.information(self,"提示!","删除成功！")
            db.close()

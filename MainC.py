# _*_coding:utf-8_*_
# Author： Zachary
import os

import pymysql
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QCursor
import sys

from PyQt5.QtWidgets import QMessageBox

from login import *


class Ui(Ui_MainWindow):
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='980226', database='pain', use_unicode=True)
        self.cursor = self.conn.cursor()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # 隐藏框体
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 加阴影
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.register_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.login_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.register_widget.hide()  # 隐藏注册widget
        self.logins.clicked.connect(self.change_login_widget)  # 登录widget的连接
        self.registers.clicked.connect(self.change_register_widget)  # 注册widget的连接
        self.login_btn.clicked.connect(self.login_fct)  # 登录功能的连接
        self.register_btn.clicked.connect(self.register_fct)  # 注册功能连接

    def change_login_widget(self):
        '''
        用于点击登录，切换为登录widget
        :return: none
        '''
        self.login_widget.show()
        self.register_widget.hide()

    def change_register_widget(self):
        '''
        用于点击注册，切换为注册widget
        :return: none
        '''
        self.register_widget.show()
        self.login_widget.hide()

    def login_fct(self):
        '''
        登录功能，连接数据库进行验证
        :return:
        '''
        usr = self.login_usr.text()
        pwd = self.login_pwd.text()

        if not usr or not pwd:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "请输入完整的用户名和密码!")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            return

        my_query = "SELECT * FROM user WHERE usr = %s"
        self.cursor.execute(my_query, [usr])
        res = self.cursor.fetchall()

        if res:
            my_query = "SELECT * FROM user WHERE usr = %s and password = %s"
            self.cursor.execute(my_query, [usr, pwd])
            res = self.cursor.fetchall()
            if res:
                self.close_btn.click()
                os.system("python Mainb_interface.py")
                sys.exit(self.exec_())

            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "密码错误，请重试!")
                msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
                msg_box.exec_()
                self.login_pwd.setText("")
                return

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "用户名不存在请先注册!")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            self.login_usr.setText("")
            self.login_pwd.setText("")
            return

    def register_fct(self):
        '''
        注册功能，插入数据库
        :return:
        '''
        usr = self.register_usr.text()
        pwd = self.register_pwd.text()
        pwd_cfm = self.register_pwd_cfm.text()

        if not usr or not pwd or not pwd_cfm:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "请输入完整的用户名和想要设置的密码!")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            return
        else:
            if pwd != pwd_cfm:
                msg_box = QMessageBox(QMessageBox.Warning, "Warning", "两次密码不一致，请重试!")
                msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
                msg_box.exec_()
                self.register_pwd.setText("")
                self.register_pwd_cfm.setText("")
                return

        my_query = f"SELECT * FROM user where usr = %s"
        self.cursor.execute(my_query, [usr])
        res = self.cursor.fetchall()
        if res:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "用户已经存在!\n请登录，或者重新输入用户名！")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            self.register_usr.setText("")
            self.register_pwd.setText("")
            self.register_pwd_cfm.setText("")
            return
        else:
            my_query = "INSERT INTO user(usr,password) VALUES(%s,%s)"
            self.cursor.execute(my_query, (usr, pwd))
            self.conn.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    loginUi = Ui()
    loginUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

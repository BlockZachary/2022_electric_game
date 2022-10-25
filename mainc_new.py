# _*_coding:utf-8_*_
# Author： Zachary

import os
import subprocess
import sys
from login import *
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import pymysql


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.setupUI()
        self.retranslateUi()
        # 隐藏窗体
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

    def setupUI(self):
        # 加阴影
        self.ui.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.register_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.ui.login_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

    # 这三个方法是鼠标移动事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def retranslateUi(self):
        self.ui.register_widget.hide()  # 隐藏注册widget
        self.ui.logins.clicked.connect(self.change_login_widget)  # 登录widget的连接
        self.ui.registers.clicked.connect(self.change_register_widget)  # 注册widget的连接
        self.ui.login_btn.clicked.connect(self.login_fct)  # 登录功能的连接
        self.ui.register_btn.clicked.connect(self.register_fct)  # 注册功能连接

    def change_login_widget(self):
        '''
        用于点击登录，切换为登录widget
        :return: none
        '''
        self.ui.login_widget.show()
        self.ui.register_widget.hide()

    def change_register_widget(self):
        '''
        用于点击注册，切换为注册widget
        :return: none
        '''
        self.ui.register_widget.show()
        self.ui.login_widget.hide()

    def login_fct(self):
        '''
        登录功能，连接数据库进行验证
        :return:
        '''
        self.conn_mysql()
        usr = self.ui.login_usr.text()
        pwd = self.ui.login_pwd.text()

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
            self.conn.close()
            if res:
                self.ui.close_btn.click()
                # os.system(r"python E:\※学习资料※\postgraduate\22研电赛\220301pycharmproject_ui\mainb_new_interface.py")
                res = subprocess.run(r"python E:\※学习资料※\postgraduate\22研电赛\220301pycharmproject_ui\mainb_new_interface.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                sys.exit(self.exec_())

            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "密码错误，请重试!")
                msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
                msg_box.exec_()
                self.ui.login_pwd.setText("")
                return

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "用户名不存在请先注册!")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            self.ui.login_usr.setText("")
            self.ui.login_pwd.setText("")
            return

    def register_fct(self):
        '''
        注册功能，插入数据库
        :return:
        '''
        self.conn_mysql()
        usr = self.ui.register_usr.text()
        pwd = self.ui.register_pwd.text()
        pwd_cfm = self.ui.register_pwd_cfm.text()

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
                self.ui.register_pwd.setText("")
                self.ui.register_pwd_cfm.setText("")
                return

        my_query = f"SELECT * FROM user where usr = %s"
        self.cursor.execute(my_query, [usr])
        res = self.cursor.fetchall()
        if res:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "用户已经存在!\n请登录，或者重新输入用户名！")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            self.ui.register_usr.setText("")
            self.ui.register_pwd.setText("")
            self.ui.register_pwd_cfm.setText("")
            self.conn.close()
            return
        else:
            my_query = "INSERT INTO user(usr,password) VALUES(%s,%s)"
            self.cursor.execute(my_query, (usr, pwd))
            self.conn.commit()
            msg_box = QMessageBox(QMessageBox.Warning, "Success", "新用户已注册成功！")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/success.ico'))
            msg_box.exec_()
        self.conn.close()

    def conn_mysql(self):
        '''
        创建mysql连接的函数
        :return:
        '''
        # 101.37.160.114
        self.conn = pymysql.connect(host = '101.37.160.114', user='zachary', password='980226', database='pain', use_unicode=True)
        self.cursor = self.conn.cursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 80, 261, 471))
        self.label.setStyleSheet("border-image: url(:/images/素材库/71851-doctor-with-mobile_wps图片_29.png);\n"
"border-radius:40px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 84, 311, 461))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 120, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 170, 241, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(650, 90, 30, 30))
        self.close_btn.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"}")
        self.close_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/素材库/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QtCore.QSize(32, 32))
        self.close_btn.setObjectName("close_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 230, 215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logins = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.logins.setFont(font)
        self.logins.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.logins.setObjectName("logins")
        self.horizontalLayout.addWidget(self.logins)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.registers = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.registers.setFont(font)
        self.registers.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.registers.setObjectName("registers")
        self.horizontalLayout.addWidget(self.registers)
        self.login_widget = QtWidgets.QWidget(self.centralwidget)
        self.login_widget.setGeometry(QtCore.QRect(430, 290, 231, 211))
        self.login_widget.setObjectName("login_widget")
        self.login_btn = QtWidgets.QPushButton(self.login_widget)
        self.login_btn.setGeometry(QtCore.QRect(180, 150, 40, 40))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(173, 173, 173);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.login_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/素材库/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QtCore.QSize(40, 40))
        self.login_btn.setObjectName("login_btn")
        self.login_usr = QtWidgets.QLineEdit(self.login_widget)
        self.login_usr.setGeometry(QtCore.QRect(30, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_usr.setFont(font)
        self.login_usr.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.login_usr.setText("")
        self.login_usr.setObjectName("login_usr")
        self.label_7 = QtWidgets.QLabel(self.login_widget)
        self.label_7.setGeometry(QtCore.QRect(170, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.login_pwd = QtWidgets.QLineEdit(self.login_widget)
        self.login_pwd.setGeometry(QtCore.QRect(30, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_pwd.setFont(font)
        self.login_pwd.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.login_pwd.setText("")
        self.login_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_pwd.setObjectName("login_pwd")
        self.register_widget = QtWidgets.QWidget(self.centralwidget)
        self.register_widget.setGeometry(QtCore.QRect(430, 290, 231, 211))
        self.register_widget.setObjectName("register_widget")
        self.label_6 = QtWidgets.QLabel(self.register_widget)
        self.label_6.setGeometry(QtCore.QRect(170, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.register_btn = QtWidgets.QPushButton(self.register_widget)
        self.register_btn.setGeometry(QtCore.QRect(180, 150, 40, 40))
        self.register_btn.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(173, 173, 173);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.register_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/素材库/register-18-383390.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_btn.setIcon(icon2)
        self.register_btn.setIconSize(QtCore.QSize(40, 40))
        self.register_btn.setObjectName("register_btn")
        self.register_usr = QtWidgets.QLineEdit(self.register_widget)
        self.register_usr.setGeometry(QtCore.QRect(30, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.register_usr.setFont(font)
        self.register_usr.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.register_usr.setText("")
        self.register_usr.setObjectName("register_usr")
        self.register_pwd = QtWidgets.QLineEdit(self.register_widget)
        self.register_pwd.setGeometry(QtCore.QRect(30, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.register_pwd.setFont(font)
        self.register_pwd.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.register_pwd.setText("")
        self.register_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_pwd.setObjectName("register_pwd")
        self.register_pwd_cfm = QtWidgets.QLineEdit(self.register_widget)
        self.register_pwd_cfm.setGeometry(QtCore.QRect(30, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.register_pwd_cfm.setFont(font)
        self.register_pwd_cfm.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.register_pwd_cfm.setText("")
        self.register_pwd_cfm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_pwd_cfm.setObjectName("register_pwd_cfm")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.close_btn.raise_()
        self.widget.raise_()
        self.login_widget.raise_()
        self.register_widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "欢迎登录"))
        self.label_4.setText(_translate("MainWindow", "疼痛识别系统"))
        self.logins.setText(_translate("MainWindow", "登录"))
        self.registers.setText(_translate("MainWindow", "注册"))
        self.login_usr.setPlaceholderText(_translate("MainWindow", "用户名："))
        self.label_7.setText(_translate("MainWindow", "登录"))
        self.login_pwd.setPlaceholderText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "注册"))
        self.register_usr.setPlaceholderText(_translate("MainWindow", "用户名："))
        self.register_pwd.setPlaceholderText(_translate("MainWindow", "设置密码："))
        self.register_pwd_cfm.setPlaceholderText(_translate("MainWindow", "确认密码："))
import resource_login

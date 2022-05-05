# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1442, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 1024, 768))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 60, 321, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_disp = QtWidgets.QLabel(self.centralwidget)
        self.label_disp.setGeometry(QtCore.QRect(550, 200, 640, 480))
        self.label_disp.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.label_disp.setText("")
        self.label_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp.setObjectName("label_disp")
        self.selectButtonNo = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonNo.setGeometry(QtCore.QRect(270, 220, 221, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.selectButtonNo.setFont(font)
        self.selectButtonNo.setObjectName("selectButtonNo")
        self.selectButtonWeak = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonWeak.setGeometry(QtCore.QRect(270, 280, 221, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.selectButtonWeak.setFont(font)
        self.selectButtonWeak.setObjectName("selectButtonWeak")
        self.selectButtonModerate = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonModerate.setGeometry(QtCore.QRect(270, 340, 221, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.selectButtonModerate.setFont(font)
        self.selectButtonModerate.setObjectName("selectButtonModerate")
        self.selectButtonSevere = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonSevere.setGeometry(QtCore.QRect(270, 400, 221, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.selectButtonSevere.setFont(font)
        self.selectButtonSevere.setObjectName("selectButtonSevere")
        self.selectdata = QtWidgets.QPushButton(self.centralwidget)
        self.selectdata.setGeometry(QtCore.QRect(310, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.selectdata.setFont(font)
        self.selectdata.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/素材库/others.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectdata.setIcon(icon)
        self.selectdata.setObjectName("selectdata")
        self.displaydata = QtWidgets.QPushButton(self.centralwidget)
        self.displaydata.setGeometry(QtCore.QRect(310, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.displaydata.setFont(font)
        self.displaydata.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/素材库/play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.displaydata.setIcon(icon1)
        self.displaydata.setObjectName("displaydata")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1200, 30, 30, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/素材库/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pain_level = QtWidgets.QLineEdit(self.centralwidget)
        self.pain_level.setGeometry(QtCore.QRect(380, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pain_level.setFont(font)
        self.pain_level.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.pain_level.setText("")
        self.pain_level.setAlignment(QtCore.Qt.AlignCenter)
        self.pain_level.setPlaceholderText("")
        self.pain_level.setObjectName("pain_level")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.video_number = QtWidgets.QLineEdit(self.centralwidget)
        self.video_number.setGeometry(QtCore.QRect(380, 630, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.video_number.setFont(font)
        self.video_number.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.video_number.setText("")
        self.video_number.setAlignment(QtCore.Qt.AlignCenter)
        self.video_number.setPlaceholderText("")
        self.video_number.setObjectName("video_number")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(270, 630, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1442, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "疼痛表情模拟"))
        self.selectButtonNo.setText(_translate("MainWindow", "No pain序列"))
        self.selectButtonWeak.setText(_translate("MainWindow", "Weak pain序列"))
        self.selectButtonModerate.setText(_translate("MainWindow", "Moderate pain序列"))
        self.selectButtonSevere.setText(_translate("MainWindow", "Severe pain序列"))
        self.selectdata.setText(_translate("MainWindow", " 文 件  "))
        self.displaydata.setText(_translate("MainWindow", "播放序列"))
        self.label_16.setText(_translate("MainWindow", "疼痛等级:"))
        self.label_17.setText(_translate("MainWindow", "序列帧数:"))
import resource_display

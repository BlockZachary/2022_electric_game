# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowA.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):

    def __init__(self):
        self.selected_file = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_disp = QtWidgets.QLabel(self.centralwidget)
        self.label_disp.setGeometry(QtCore.QRect(250, 110, 640, 480))
        self.label_disp.setText("")
        self.label_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp.setObjectName("label_disp")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 921, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.selectButtonA = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonA.setGeometry(QtCore.QRect(50, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.selectButtonA.setFont(font)
        self.selectButtonA.setObjectName("selectButtonA")
        self.selectButtonB = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonB.setGeometry(QtCore.QRect(50, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.selectButtonB.setFont(font)
        self.selectButtonB.setObjectName("selectButtonB")
        self.selectButtonC = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButtonC.setGeometry(QtCore.QRect(50, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.selectButtonC.setFont(font)
        self.selectButtonC.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selectButtonC.setObjectName("selectButtonC")
        self.selectdata = QtWidgets.QPushButton(self.centralwidget)
        self.selectdata.setGeometry(QtCore.QRect(50, 360, 141, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.selectdata.setFont(font)
        self.selectdata.setObjectName("selectdata")
        self.displaydata = QtWidgets.QPushButton(self.centralwidget)
        self.displaydata.setGeometry(QtCore.QRect(50, 440, 141, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.displaydata.setFont(font)
        self.displaydata.setObjectName("displaydata")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "疼痛表情模拟"))
        self.selectButtonA.setText(_translate("MainWindow", "疼痛患者A"))
        self.selectButtonB.setText(_translate("MainWindow", "疼痛患者B"))
        self.selectButtonC.setText(_translate("MainWindow", "疼痛患者C"))
        self.selectdata.setText(_translate("MainWindow", "选择数据"))
        self.displaydata.setText(_translate("MainWindow", "播放序列"))

        self.selectButtonA.toggled.connect(self.get_button)
        self.selectButtonB.toggled.connect(self.get_button)
        self.selectButtonC.toggled.connect(self.get_button)

        self.selectdata.clicked.connect(self.msg)

        self.displaydata.clicked.connect(self.th1)

    def get_button(self):
        if self.selectButtonA.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\042-ll042\ll042t1aaunaff'
        elif self.selectButtonB.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\043-jh043\jh043t1afaff'
        elif self.selectButtonC.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\047-jl047\jl047t1aaunaff'

    def th1(self):
        t1 = threading.Thread(target=self.display_data, name='t1')
        t1.start()


    def display_data(self):
        print(f'开始显示图像{self.selected_file}')
        for root, dirs_name, files_name in os.walk(self.selected_file):
            for i in files_name:
                files_name = os.path.join(root, i)
                print(files_name)
                img_Image = QPixmap(files_name)
                self.label_disp.setPixmap(img_Image)
                self.label_disp.setScaledContents(True)
                time.sleep(0.04)

    def msg(self, Filepath):
        data_url = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", r"E:\New_OpenFace\Datasets\UNBC\Images")  # 起始路径
        self.selected_file = data_url


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
#     MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
#     ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
#     ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
#     MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
#     sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication

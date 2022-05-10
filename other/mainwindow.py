# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os
import shutil
import sys, time
import threading

from PIL.Image import Image
import numpy as np
from PyQt5.QtCore import Qt

from exe_in_pic_out_res import *
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(object):
    def __init__(self):
        self.button_flag = 0
        self.BN = train_BN('traindata.csv')
        self.most_pain_index = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_video = QtWidgets.QPushButton(self.centralwidget)
        self.button_video.setGeometry(QtCore.QRect(50, 130, 141, 41))
        self.button_video.setObjectName("button_video")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 1121, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.label_view = QtWidgets.QLabel(self.centralwidget)
        self.label_view.setGeometry(QtCore.QRect(430, 130, 631, 451))
        self.label_view.setText("")
        self.label_view.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view.setObjectName("label_view")
        self.button_recognize = QtWidgets.QPushButton(self.centralwidget)
        self.button_recognize.setGeometry(QtCore.QRect(210, 130, 141, 41))
        self.button_recognize.setObjectName("button_recognize")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 200, 301, 381))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
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
        self.button_video.setText(_translate("MainWindow", "开启录制"))
        self.title.setText(_translate("MainWindow", "疼痛识别系统"))
        self.button_recognize.setText(_translate("MainWindow", "识别疼痛"))

        self.button_video.clicked.connect(self.th1)
        self.button_recognize.clicked.connect(self.start_detect)
        self.textBrowser.setText(f'请点击开启录制')

    def th1(self):
        t = threading.Thread(target=self.open_video, name='t')
        t.start()

    def open_video(self):
        try:
            os.mkdir('./data_set')
        except:
            shutil.rmtree('./data_set')
            os.mkdir('./data_set')
        self.button_flag = 1

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 800)  # set video width
        cam.set(4, 600)  # set video height
        framerate = 4  # set frame
        count_frame = 1
        flag = 0

        while True:
            if self.button_flag == 1:
                self.textBrowser.append(f'{time.strftime("%Y-%m-%d %X", time.localtime())}摄像头已开启录制，点击识别疼痛暂停并识别')
                while True:
                    ret, img = cam.read()
                    img = cv2.flip(img, 1)  # 水平翻转
                    # cv2.imshow("pic", img)
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = bytesPerComponent * width

                    _img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    _img = QImage(_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    self.label_view.setPixmap(QPixmap.fromImage(_img))
                    if count_frame % framerate == 0:
                        cv2.imwrite(f'./data_set/{flag}_pic.png', img)
                        flag += 1
                    # time.sleep(0.05)
                    count_frame += 1
                    # key = cv2.waitKey(10)  # 原来是10
                    if self.button_flag == 0:
                        break
            else:
                break

    def th2(self):
        t2 = threading.Thread(target=self.show_most_img, name='t2')
        t2.start()

    def show_most_img(self):
        img_path = f'./data_set/{self.most_pain_index}_pic.png'
        img_Image = QPixmap(img_path)
        self.label_view.setPixmap(img_Image)


    def start_detect(self):
        self.label_view.clear()
        self.button_flag = 0
        self.textBrowser.append(f'{time.strftime("%Y-%m-%d %X", time.localtime())}摄像头已关闭,开始检测')
        # BN = train_BN('traindata.csv')
        # print("[info]BN建模完成")
        self.textBrowser.append('[info]BN已建模完成')

        # 第一步，读取in_dir并执行exe，将结果输出到out_dir-->csv
        # 要处理的图片/视频路径
        path_dir = os.path.abspath('./')  # 获取当前项目文件夹绝对路径
        # in_dir = r"E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff"  # 这个路径是你的待识别图像的路径，路径必须完整
        in_dir = fr"{path_dir}data_set"
        # csv输出路径
        out_dir = fr"{path_dir}result"  # 这个是在当前项目文件夹下的result文件夹，路径必须完整
        execute_pic(in_dir, out_dir)
        # print("[info]特征点获取完成")
        self.textBrowser.append('[info]特征点获取完成')

        # 第二步，获取csv中需要的AU4,6,7,9,10，并根据特征点计算EAR值，判断AU43
        # 第三步，将所获取的证据生成单独的csv文件
        read_csv_output_result(f"{out_dir}/{os.path.basename(in_dir)}.csv")
        # print("[info]完成AU的计算并保存")
        self.textBrowser.append('[info]完成AU的计算并保存')

        # 第四步，把证据csv送到Bayesian network中进行推理，并输出结果
        result = predict(self.BN, "test_au.csv")
        # print(f"[info]输出了预测结果{res}")
        self.textBrowser.append(f'[info]输出了预测结果{result[0]}')

        self.most_pain_index = result[1]
        self.textBrowser.append(f'[info]结果准确率为{result[3]:.2f}%')
        self.textBrowser.append(f'[result]疼痛程度最剧烈的是第{result[1]+1}帧，等级为{result[2]}')


        self.th2()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication

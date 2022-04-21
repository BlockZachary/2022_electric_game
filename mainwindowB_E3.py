# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowB_E3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import shutil
import sys, time
import threading
from socket import *

from PIL.Image import Image
import numpy as np
from PyQt5.QtCore import Qt

from exe_in_pic_out_res import *
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.button_flag = 0
        self.BN = train_BN('traindata.csv')
        self.most_pain_index = 0

        try:
            address = "192.168.1.146"  # 8266的服务器的ip地址
            port = 8266  # 8266的服务器的端口号
            self.buffsize = 1024  # 接收数据的缓存大小
            self.s = socket(AF_INET, SOCK_STREAM)
            self.conn = ("192.168.1.124", 1234)
            self.s.connect((address, port))
            self.button_treatment_flag = "0"
        except:
            print('未能成功连接设备，请重试...')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_video = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_video.sizePolicy().hasHeightForWidth())
        self.button_video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.button_video.setFont(font)
        self.button_video.setObjectName("button_video")
        self.horizontalLayout_2.addWidget(self.button_video)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_recognize = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_recognize.sizePolicy().hasHeightForWidth())
        self.button_recognize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.button_recognize.setFont(font)
        self.button_recognize.setObjectName("button_recognize")
        self.horizontalLayout_2.addWidget(self.button_recognize)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.lineEdit_treatement_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_treatement_time.setMinimumSize(QtCore.QSize(0, 5))
        self.lineEdit_treatement_time.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.lineEdit_treatement_time.setFont(font)
        self.lineEdit_treatement_time.setObjectName("lineEdit_treatement_time")
        self.horizontalLayout_3.addWidget(self.lineEdit_treatement_time)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.button_medicare = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_medicare.sizePolicy().hasHeightForWidth())
        self.button_medicare.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.button_medicare.setFont(font)
        self.button_medicare.setObjectName("button_medicare")
        self.horizontalLayout_3.addWidget(self.button_medicare)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_5.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_view = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_view.sizePolicy().hasHeightForWidth())
        self.label_view.setSizePolicy(sizePolicy)
        self.label_view.setMinimumSize(QtCore.QSize(640, 480))
        self.label_view.setText("")
        self.label_view.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view.setObjectName("label_view")
        self.verticalLayout_3.addWidget(self.label_view)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 26))
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
        self.title.setText(_translate("MainWindow", "疼痛识别系统"))
        self.button_video.setText(_translate("MainWindow", "开启录制"))
        self.button_recognize.setText(_translate("MainWindow", "识别疼痛"))
        self.label_2.setText(_translate("MainWindow", "建议"))
        self.label.setText(_translate("MainWindow", "分钟治疗"))
        self.button_medicare.setText(_translate("MainWindow", "启动治疗"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        self.button_video.clicked.connect(self.th1)
        self.button_recognize.clicked.connect(self.start_detect)
        self.button_medicare.clicked.connect(self.button_medicare_ctrl)
        self.textBrowser.setText(f'请点击开启录制')

    def th1(self):
        """
        线程1：连接 open_video
        :return:
        """
        t = threading.Thread(target=self.open_video, name='t')
        t.start()

    def th2(self):
        """
        线程2：连接 show_most_img
        :return:
        """
        t2 = threading.Thread(target=self.show_most_img, name='t2')
        t2.start()

    def th3(self):
        """
        线程3：连接 set_treatment_time
        :return:
        """
        t3 = threading.Thread(target=self.set_treatment_time, name='t3')
        t3.start()

    def button_medicare_ctrl(self):
        """
        控制按摩仪的程序
        :return:
        """
        try:
            if self.button_treatment_flag == "0":
                self.button_treatment_flag = "1"
                self.ctrl_treatment()
            else:
                self.button_treatment_flag = '0'
                self.ctrl_treatment()
        except:
            self.textBrowser.append('[warning]未连接治疗仪，无法启动治疗...')

    def ctrl_treatment(self):
        """
        发送控制信息
        :return:
        """
        senddata = self.button_treatment_flag
        self.s.send(senddata.encode())
        time.sleep(2)

    def open_video(self):
        """
        创建文件夹并打开摄像头
        :return:
        """
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

    def show_most_img(self):
        """
        显示最剧烈的疼痛程度图像
        :return:
        """
        img_path = f'./data_set/{self.most_pain_index}_pic.png'
        img_Image = QPixmap(img_path)
        self.label_view.setPixmap(img_Image)

    def set_treatment_time(self):
        """
        根据识别到的疼痛等级结果，给出治疗时间
        :return:
        """
        dic = {'No': 0, 'Weak': 10, 'Moderate': 20, 'Severe': 30}
        self.commend_treatment_time = dic[self.most_pain_level]
        self.lineEdit_treatement_time.setText(f'{self.commend_treatment_time}')
        self.textBrowser.append(f'[recommend]建议治疗{self.commend_treatment_time}分钟')
        # print(f'建议治疗{self.commend_treatment_time}')

    def start_detect(self):
        """
        对拍摄下来的图像检测疼痛程度
        :return:
        """
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
        self.textBrowser.append(f'[result]疼痛程度最剧烈的是第{result[1] + 1}帧，等级为{result[2]}')

        self.most_pain_level = result[2]

        self.th2()
        self.th3()
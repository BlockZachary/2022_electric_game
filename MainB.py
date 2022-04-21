# _*_coding:utf-8_*_
# Author： Zachary
from mainwindowB_E4 import *
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

class Ui(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.button_flag = 0
        self.BN = train_BN('traindata.csv')
        self.most_pain_index = 0

        try:
            address = "192.168.1.112"  # 8266的服务器的ip地址
            port = 8266  # 8266的服务器的端口号
            self.buffsize = 1024  # 接收数据的缓存大小
            self.s = socket(AF_INET, SOCK_STREAM)
            self.conn = ("192.168.1.113", 1234)
            self.s.connect((address, port))
            self.button_treatment_flag = "0"
        except:
            print('未能成功连接设备，请重试...')

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.button_video.clicked.connect(self.th1)
        self.button_recognize.clicked.connect(self.start_detect)
        self.button_medicare.clicked.connect(self.button_medicare_ctrl)
        self.textBrowser.setText(f'请点击[开启录制]按钮')

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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
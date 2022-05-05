# _*_coding:utf-8_*_
# Author： Zachary
import serial

from main_interface import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from flask import Flask, render_template
from socket import *
from exe_in_pic_out_res import *
import threading
import numpy as np


class Mainwindows(QMainWindow):
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

        self.video_flag = 0
        self.BN = train_BN('traindata_2.csv')
        self.most_pain_index = 0

        # 启动ESP8266的线程
        self.thread_esp8266_init()

        task_port = threading.Thread(target=self.listen_port, name='task_port')
        task_port.start()

    def setupUI(self):
        # 加阴影
        self.ui.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_9.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))
        self.ui.label_11.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))
        self.ui.label_12.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))

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
        self.ui.diagnose_widget.hide()
        self.ui.treatment_widget.hide()
        self.ui.recognizers.clicked.connect(self.change_recognize_widget)
        self.ui.diagnosers.clicked.connect(self.change_diagnose_widget)
        self.ui.treatments.clicked.connect(self.change_treatment_widget)

        self.ui.rcg_start.clicked.connect(self.thread_video_start)
        self.ui.rcg_stop.clicked.connect(self.stop_video)
        self.ui.rcg_recognize.clicked.connect(self.start_recognize)
        self.ui.rcg_save.clicked.connect(self.save_painimg)

        self.ui.dag_search.clicked.connect(self.diagnose_search)
        self.ui.dag_reset.clicked.connect(self.diagnose_reset)
        self.ui.dag_submit.clicked.connect(self.diagnose_submit)

        self.ui.trm_search.clicked.connect(self.treatment_search)
        self.ui.trm_reset.clicked.connect(self.treatment_reset)
        self.ui.trm_start.clicked.connect(self.button_medicare_ctrl)  # TODO 这个是trm的控制按钮 到时候往后面挪

    # 三个widget之间切换
    def change_recognize_widget(self):
        '''
        点击识别按钮，切换为recognize_widget
        :return:
        '''
        self.ui.recognize_widget.show()
        self.ui.diagnose_widget.hide()
        self.ui.treatment_widget.hide()

    def change_diagnose_widget(self):
        '''
        点击诊断按钮，切换为diagnose_widget
        :return:
        '''
        self.ui.diagnose_widget.show()
        self.ui.recognize_widget.hide()
        self.ui.treatment_widget.hide()

    def change_treatment_widget(self):
        '''
        点击治疗按钮，切换为treatment_widget
        :return:
        '''
        self.ui.treatment_widget.show()
        self.ui.recognize_widget.hide()
        self.ui.diagnose_widget.hide()

    def conn_mysql(self):
        '''
        创建mysql连接的函数
        :return:
        '''
        self.conn = pymysql.connect(user='root', password='980226', database='pain', use_unicode=True)
        self.cursor = self.conn.cursor()

    # recognizers widget的功能实现
    def thread_video_start(self):
        '''
        线程1：recognizers连接open_video
        :return:
        '''
        thd1 = threading.Thread(target=self.video_start, name='thd1')
        thd1.start()

    def thread_show_mostimg(self):
        '''
        线程2：用于recognizers显示识别最剧烈一帧
        :return:
        '''
        thd2 = threading.Thread(target=self.show_mostimg, name='thd2')
        thd2.start()

    def thread_esp8266_init(self):
        '''
        线程3：用于类初始化连接上ESP8266
        :return:
        '''
        thd3 = threading.Thread(target=self.esp8266_init, name='thd3')
        thd3.start()

    def video_start(self):
        """
        recognizers创建文件夹并打开摄像头
        :return:
        """
        try:
            os.mkdir('./data_set')
        except:
            shutil.rmtree('./data_set')
            os.mkdir('./data_set')
        self.video_flag = 1

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640)  # set video width
        cam.set(4, 480)  # set video height
        framerate = 1  # set frame
        count_frame = 1
        self.flag = 0

        while True:
            if self.video_flag == 1:
                self.ui.rcg_browser.append(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 摄像头已开启录制，点击停止拍摄图像结束录制！')
                while True:
                    ret, img = cam.read()
                    img = cv2.flip(img, 1)  # TODO 水平翻转 使用摄像头的时候注释掉
                    # cv2.imshow("pic", img)
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = bytesPerComponent * width

                    _img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    _img = QImage(_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    self.ui.rcg_videoshow.setPixmap(QPixmap.fromImage(_img))
                    if count_frame % framerate == 0:
                        cv2.imwrite(f'./data_set/{self.flag}_pic.png', img)
                        self.flag += 1
                    # time.sleep(0.05)
                    count_frame += 1
                    # key = cv2.waitKey(10)  # 原来是10
                    if self.video_flag == 0:
                        break
            else:
                break

    def stop_video(self):
        '''
        recognizers暂停摄像头的拍摄
        :return:
        '''
        self.video_flag = 0
        time.sleep(0.1)
        self.ui.rcg_videoshow.clear()
        self.ui.rcg_browser.setText(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 拍摄图像结束！请点击疼痛表情识别！')

    def show_mostimg(self):
        '''
        recognizers显示最剧烈一帧图像
        :return:
        '''
        img_path = f'./data_set/{self.most_pain_index}_pic.png'
        img_Image = QPixmap(img_path)
        self.ui.rcg_videoshow.setPixmap(img_Image)

    def start_recognize(self):
        '''
        recognizers对拍摄好的图像检测疼痛程度
        :return:
        '''
        self.ui.rcg_browser.setText(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 开始检测疼痛表情！')
        # 第一步，读取in_dir并执行exe，将结果输出到out_dir-->csv
        # 要处理的图片/视频路径
        path_dir = os.path.abspath('./')  # 获取当前项目文件夹绝对路径
        print(path_dir)
        # in_dir = r"E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff"  # 这个路径是你的待识别图像的路径，路径必须完整
        in_dir = fr"{path_dir}data_set"
        # csv输出路径
        out_dir = fr"{path_dir}result"  # 这个是在当前项目文件夹下的result文件夹，路径必须是绝对路径
        execute_pic(in_dir, out_dir)
        # 第二步，获取csv中需要的AU4,6,7,9,10，并根据特征点计算EAR值，判断AU43
        # 第三步，将所获取的证据生成单独的csv文件
        read_csv_output_result(fr"{out_dir}\{os.path.basename(in_dir)}.csv")
        # 第四步，把证据csv送到Bayesian network中进行推理，并输出结果
        self.result = predict(self.BN, "test_au.csv")
        self.ui.rcg_browser.append(f'检测到疼痛图像{self.flag}帧')

        self.most_pain_index = self.result[1]
        # self.textBrowser.append(f'[result]疼痛程度最剧烈的是第{result[1] + 1}帧，等级为{result[2]}')

        self.most_pain_level = self.result[2]

        self.thread_show_mostimg()
        self.set_tablewidget(self.result)

    def set_tablewidget(self, res):
        '''
        recognizers设置表格数据
        :param res:
        :return:
        '''
        if 'No' in res[0]:
            item_no = QTableWidgetItem(str(res[0]['No']))
            item_no.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(0, 0, item_no)
        else:
            item_no = QTableWidgetItem('0')
            item_no.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(0, 0, item_no)

        if 'Weak' in res[0]:
            item_weak = QTableWidgetItem(str(res[0]['Weak']))
            item_weak.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(1, 0, item_weak)
        else:
            item_weak = QTableWidgetItem('0')
            item_weak.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(1, 0, item_weak)

        if 'Moderate' in res[0]:
            item_moderate = QTableWidgetItem(str(res[0]['Moderate']))
            item_moderate.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(2, 0, item_moderate)
        else:
            item_moderate = QTableWidgetItem('0')
            item_moderate.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(2, 0, item_moderate)

        if 'Severe' in res[0]:
            item_severe = QTableWidgetItem(str(res[0]['Severe']))
            item_severe.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(3, 0, item_severe)
        else:
            item_severe = QTableWidgetItem('0')
            item_severe.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.ui.rcg_tableWidget.setItem(3, 0, item_severe)

        item_accuracy = QTableWidgetItem(f'{res[3]:.2f}%')
        item_accuracy.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.ui.rcg_tableWidget.setItem(4, 0, item_accuracy)

    def save_painimg(self):
        '''
        recognizers保存最剧烈疼痛帧
        :return:
        '''
        name = self.ui.rcg_name.text()

        if not name:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "请输入患者姓名进行保存!")
            msg_box.setWindowIcon(QtGui.QIcon('./素材库/warning.ico'))
            msg_box.exec_()
            return

        try:
            os.mkdir('./pain_img')
        except:
            pass
        finally:
            img_path = f'./data_set/{self.most_pain_index}_pic.png'
            img = cv2.imread(img_path)
            save_path = f'./pain_img/{name}_{self.most_pain_level}.png'
            # cv2.imwrite(save_path, img)
            cv2.imencode('.png', img)[1].tofile(save_path)
        self.conn_mysql()

        my_query = f"SELECT * FROM patient where name = %s"
        self.cursor.execute(my_query, [name])
        res = self.cursor.fetchall()

        if res:
            my_update = f"UPDATE patient SET painlevel = %s where name = %s"
            self.cursor.execute(my_update, (self.most_pain_level, name))
            self.conn.commit()
        else:
            my_insert = f"INSERT INTO patient(name,painlevel) values (%s,%s)"
            self.cursor.execute(my_insert, (name, self.most_pain_level))
            self.conn.commit()
        self.conn.close()

    # TODO 在这里修改ESP8266的ip
    def esp8266_init(self):
        '''
        初始化连接ESP8266
        :return:
        '''
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

    # diagnosers widget的功能实现
    def diagnose_search(self):
        '''
        diagnosers点击查询按钮的功能
        在患者姓名为空的时候，提示信息提示输入姓名，
        输入姓名之后去patient表查询是否存在患者，若不存在则显示“患者不存在”；若存在则显示患者疼痛等级 并显示对应等级的图片
        :return:
        '''
        self.conn_mysql()
        patient_name = self.ui.dag_name.text()
        if not patient_name:
            self.ui.dag_browser.setText("[warning]请输入患者姓名，再点击查询按钮...")
            self.ui.dag_videoshow.clear()
            return
        else:
            my_query = f"SELECT * FROM patient where name = %s"
            self.cursor.execute(my_query, [patient_name])
            res = self.cursor.fetchone()
            if not res:
                self.ui.dag_browser.setText("[warning]患者不存在...")
                self.ui.dag_videoshow.clear()
                return
            else:
                self.ui.dag_browser.setText("[success]查询成功！")
                self.ui.dag_painlevel.setText(res[2])
                # TODO 这里给图片加点儿东西
                img_path = f'./pain_img/{patient_name}_{self.ui.dag_painlevel.text()}.png'
                img_Image = QPixmap(img_path)
                self.ui.dag_videoshow.setPixmap(img_Image)
            self.conn.close()

    def face_detect(self,image_path):
        image = cv2.imread(image_path)
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)  # COLOR_BGR2RGBA
        gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)  # 读取图像并转化为灰度
        # Detect faces in the image
        faces = self.faceCascade.detectMultiScale(  # 面部级联检测
            gray,  # 灰度图像
            scaleFactor=1.1,  # 比例因子对图像进行补偿
            minNeighbors=5,  # 定义在当前对象前检测到多少对象
            minSize=(30, 30),  # 给出每个窗口的最小值
        )
        self.textBrowser.setText("Found {0} faces!".format(len(faces)))
        # Draw a rectangle around the faces and recognize and sign
        for (x, y, w, h) in faces:  # 在检测到的面部周围画框
            cv2.rectangle(image, (x, y), (x + w, y + h), (237, 149, 100), 2)
        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QPixmap(_image)
        return jpg_out

    def diagnose_reset(self):
        '''
        diagnosers点击重置按钮的功能
        :return:
        '''
        self.ui.dag_name.setText("")
        self.ui.dag_videoshow.clear()
        self.ui.dag_painlevel.setText("")
        if self.ui.dag_male.isChecked() == True:
            self.ui.dag_male.setAutoExclusive(False)
            self.ui.dag_male.setChecked(False)
            self.ui.dag_male.setAutoExclusive(True)
        if self.ui.dag_female.isChecked() == True:
            self.ui.dag_female.setAutoExclusive(False)
            self.ui.dag_female.setChecked(False)
            self.ui.dag_female.setAutoExclusive(True)
        self.ui.dag_browser.clear()
        self.ui.dag_mechine.setChecked(False)
        self.ui.dag_treattime.setText("")
        if self.ui.dag_drug1.isChecked() == True:
            self.ui.dag_drug1.setAutoExclusive(False)
            self.ui.dag_drug1.setChecked(False)
            self.ui.dag_drug1.setAutoExclusive(True)
        if self.ui.dag_drug2.isChecked() == True:
            self.ui.dag_drug2.setAutoExclusive(False)
            self.ui.dag_drug2.setChecked(False)
            self.ui.dag_drug2.setAutoExclusive(True)
        if self.ui.dag_drug3.isChecked() == True:
            self.ui.dag_drug3.setAutoExclusive(False)
            self.ui.dag_drug3.setChecked(False)
            self.ui.dag_drug3.setAutoExclusive(True)
        if self.ui.dag_drug4.isChecked() == True:
            self.ui.dag_drug4.setAutoExclusive(False)
            self.ui.dag_drug4.setChecked(False)
            self.ui.dag_drug4.setAutoExclusive(True)
        self.ui.dag_remark.clear()

    def diagnose_submit(self):
        '''
        diagnosers点击提交按钮的功能
        :return:
        '''
        self.conn_mysql()
        name = self.ui.dag_name.text()
        if not name:
            self.ui.dag_browser.setText("[warning]请输入信息后再提交！")
            return
        painlevel = self.ui.dag_painlevel.text()
        if self.ui.dag_male.isChecked() == True:
            gender = '男'
        elif self.ui.dag_female.isChecked() == True:
            gender = '女'
        else:
            gender = '男'

        if self.ui.dag_mechine.isChecked() == True:
            mechine = '是'
        elif self.ui.dag_mechine.isChecked() == False:
            mechine = '否'
        else:
            mechine = '否'
        mechine_time = self.ui.dag_treattime.text()
        if not mechine_time:
            mechine_time = 'NULL'
        drug = 'NULL'
        if self.ui.dag_drug1.isChecked() == True:
            drug = '酮铬酸'
        elif self.ui.dag_drug2.isChecked() == True:
            drug = '氯诺昔康'
        elif self.ui.dag_drug3.isChecked() == True:
            drug = '保泰松'
        elif self.ui.dag_drug4.isChecked() == True:
            drug = '芬太尼'
        else:
            pass
        remark = self.ui.dag_remark.toPlainText()
        if not remark:
            remark = 'NULL'

        my_query = f"SELECT * FROM patient where name = %s"
        self.cursor.execute(my_query, [name])
        res = self.cursor.fetchall()

        if res:
            my_update = f"UPDATE patient SET painlevel = %s,gender = %s,mechine = %s,mechine_time = %s,drug = %s,remark = %s where name = %s"
            print(my_update)
            print((painlevel, gender, mechine, mechine_time, drug, remark, name))
            self.cursor.execute(my_update, (painlevel, gender, mechine, mechine_time, drug, remark, name))
            self.conn.commit()
        else:
            my_insert = f"INSERT INTO patient(name,painlevel,gender,mechine,mechine_time,drug,remark) values (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(my_insert, (name, painlevel, gender, mechine, mechine_time, drug, remark))
            self.conn.commit()
        self.conn.close()
        self.ui.dag_browser.setText("[success]提交成功！")

    # treatments widget的功能实现
    def treatment_search(self):
        '''
        treatments点击查询按钮的功能
        :return:
        '''
        self.conn_mysql()
        patient_name = self.ui.trm_name.text()
        if not patient_name:
            self.ui.trm_browser.setText("[warning]请输入患者姓名，再点击查询按钮...")
            return
        else:
            my_query = f"SELECT * FROM patient where name = %s"
            self.cursor.execute(my_query, [patient_name])
            res = self.cursor.fetchone()
            if not res:
                self.ui.trm_browser.setText("[warning]患者不存在...")
                return
            else:
                self.ui.trm_browser.setText("[success]查询成功！")
                self.ui.trm_painlevel.setText(res[2])
                self.ui.trm_gender.setText(res[3])
                self.ui.trm_mechine.setText(res[4])
                self.ui.trm_treattime.setText(res[5])
                self.ui.trm_drug.setText(res[6])
                self.ui.trm_remark.setText(res[7])

        self.conn.close()

    def treatment_reset(self):
        '''
        treatments点击重置按钮的功能
        :return:
        '''
        self.ui.trm_name.setText("")
        self.ui.trm_painlevel.setText("")
        self.ui.trm_gender.setText("")
        self.ui.trm_mechine.setText("")
        self.ui.trm_treattime.setText("")
        self.ui.trm_drug.setText("")
        self.ui.trm_remark.setText("")
        self.ui.trm_browser.setText("")
        self.ui.trm_mechine_workmode.setCurrentIndex(0)
        self.ui.trm_mechine_worktime.setText("")
        self.ui.trm_durg_use.setCurrentIndex(0)
        self.ui.trm_drug_mass.setText("")
        self.ui.trm_drug_speed.setText("")

    # TODO 控制端的两个测试例子，这两个到时候往后挪动
    def button_medicare_ctrl(self):
        """
        控制按摩仪的程序
        :return:
        """
        workmode = self.ui.trm_mechine_workmode.currentIndex()
        try:
            if workmode == 1:
                self.button_treatment_flag = "1"
                self.ctrl_treatment()
                self.ui.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 2:
                self.button_treatment_flag = "2"
                self.ctrl_treatment()
                self.ui.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 3:
                self.button_treatment_flag = '3'
                self.ctrl_treatment()
                self.ui.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 0:
                self.button_treatment_flag = '4'
                self.ctrl_treatment()
                self.ui.trm_browser.setText('[success]治疗仪启动成功！')
        except:
            self.ui.trm_browser.setText('[warning]未连接治疗仪，无法启动治疗...')


    # TODO 控制端的两个测试例子，这两个到时候往后挪动
    def ctrl_treatment(self):
        """
        发送控制信息
        :return:
        """
        senddata = self.button_treatment_flag
        self.s.send(senddata.encode())
        time.sleep(2)

    # 语音模块控制按摩仪
    def listen_port(self):
        try:
            ser = serial.Serial(port='COM11', baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=2)
            while True:
                message = ser.readline()
                try:
                    # print(int(message[0:1]))
                    if int(message[0:1]) == 3:
                        # TODO 这块添加止痛泵的控制
                        self.ui.trm_start.click()
                        print('已经打开了止痛泵！')
                    elif int(message[0:1]) == 4:
                        print('已经关闭了止痛泵！')
                    else:
                        continue
                except:
                    continue
        except:
            pass


f = Flask(__name__)


@f.route("/")
def index():
    # 1.获取所有的留言板数据

    # 2.把数据分配到模板中（Html页面渲染）
    data1 = model('select * from patient')
    data2 = model('select * from user')
    data = []
    data.append(data1)
    data.append(data2)

    return render_template('index2.html', data=data)


# 封装MySQL操作方法
def model(sql):
    conn = pymysql.connect(user='root', password='980226', host='localhost', database='pain', charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = conn.cursor()

        row = cursor.execute(sql)
        conn.commit()

        # 返回结果，如果有数据则返回，没有数据则返回影响的行数
        data = cursor.fetchall()
        if data:
            return data
        else:
            return row

    except:
        conn.rollback()
    finally:
        conn.close()


# 运行flask的线程
def frun():
    f.run(debug=False, host='127.0.0.1', port='8080')




if __name__ == '__main__':
    t = threading.Thread(target=frun, name='t')
    t.start()
    app = QApplication(sys.argv)
    win = Mainwindows()
    sys.exit(app.exec_())
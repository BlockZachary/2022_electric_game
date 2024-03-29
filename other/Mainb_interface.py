# _*_coding:utf-8_*_
# Author： Zachary
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from flask import Flask, render_template
from main_interface import *
import sys
from socket import *
from exe_in_pic_out_res import *
import threading
import numpy as np


class Ui(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.video_flag = 0
        self.BN = train_BN('traindata.csv')
        self.most_pain_index = 0

        # 启动ESP8266的线程
        self.thread_esp8266_init()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # 隐藏框体
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 加阴影
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_9.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))
        self.label_11.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))
        self.label_12.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0))

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.diagnose_widget.hide()
        self.treatment_widget.hide()
        self.recognizers.clicked.connect(self.change_recognize_widget)
        self.diagnosers.clicked.connect(self.change_diagnose_widget)
        self.treatments.clicked.connect(self.change_treatment_widget)
        self.rcg_start.clicked.connect(self.thread_video_start)
        self.rcg_stop.clicked.connect(self.stop_video)
        self.rcg_recognize.clicked.connect(self.start_recognize)
        self.rcg_save.clicked.connect(self.save_painimg)

        self.dag_search.clicked.connect(self.diagnose_search)
        self.dag_reset.clicked.connect(self.diagnose_reset)
        self.dag_submit.clicked.connect(self.diagnose_submit)

        self.trm_search.clicked.connect(self.treatment_search)
        self.trm_reset.clicked.connect(self.treatment_reset)
        self.trm_start.clicked.connect(self.button_medicare_ctrl)  # TODO 这个是trm的控制按钮 到时候往后面挪


    # 三个widget之间切换
    def change_recognize_widget(self):
        '''
        点击识别按钮，切换为recognize_widget
        :return:
        '''
        self.recognize_widget.show()
        self.diagnose_widget.hide()
        self.treatment_widget.hide()

    def change_diagnose_widget(self):
        '''
        点击诊断按钮，切换为diagnose_widget
        :return:
        '''
        self.diagnose_widget.show()
        self.recognize_widget.hide()
        self.treatment_widget.hide()

    def change_treatment_widget(self):
        '''
        点击治疗按钮，切换为treatment_widget
        :return:
        '''
        self.treatment_widget.show()
        self.recognize_widget.hide()
        self.diagnose_widget.hide()

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
        framerate = 4  # set frame
        count_frame = 1
        self.flag = 0

        while True:
            if self.video_flag == 1:
                self.rcg_browser.append(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 摄像头已开启录制，点击停止拍摄图像结束录制！')
                while True:
                    ret, img = cam.read()
                    # TODO 水平翻转 使用摄像头的时候注释掉
                    img = cv2.flip(img, 1)
                    # cv2.imshow("pic", img)
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = bytesPerComponent * width

                    _img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    _img = QImage(_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    self.rcg_videoshow.setPixmap(QPixmap.fromImage(_img))
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
        self.rcg_videoshow.clear()
        self.rcg_browser.setText(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 拍摄图像结束！请点击疼痛表情识别！')

    def show_mostimg(self):
        '''
        recognizers显示最剧烈一帧图像
        :return:
        '''
        img_path = f'./data_set/{self.most_pain_index}_pic.png'
        img_Image = QPixmap(img_path)
        self.rcg_videoshow.setPixmap(img_Image)

    def start_recognize(self):
        '''
        recognizers对拍摄好的图像检测疼痛程度
        :return:
        '''
        self.rcg_browser.setText(f'{time.strftime("%Y-%m-%d %X", time.localtime())} 开始检测疼痛表情！')
        # 第一步，读取in_dir并执行exe，将结果输出到out_dir-->csv
        # 要处理的图片/视频路径
        path_dir = os.path.abspath('./')  # 获取当前项目文件夹绝对路径
        # in_dir = r"E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff"  # 这个路径是你的待识别图像的路径，路径必须完整
        in_dir = fr"{path_dir}data_set"
        # csv输出路径
        out_dir = fr"{path_dir}result"  # 这个是在当前项目文件夹下的result文件夹，路径必须是绝对路径
        execute_pic(in_dir, out_dir)
        # 第二步，获取csv中需要的AU4,6,7,9,10，并根据特征点计算EAR值，判断AU43
        # 第三步，将所获取的证据生成单独的csv文件
        read_csv_output_result(f"{out_dir}/{os.path.basename(in_dir)}.csv")
        # 第四步，把证据csv送到Bayesian network中进行推理，并输出结果
        self.result = predict(self.BN, "test_au.csv")
        self.rcg_browser.append(f'检测到疼痛图像{self.flag}帧')

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
            self.rcg_tableWidget.setItem(0, 0, item_no)
        else:
            item_no = QTableWidgetItem('0')
            item_no.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(0, 0, item_no)

        if 'Weak' in res[0]:
            item_weak = QTableWidgetItem(str(res[0]['Weak']))
            item_weak.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(1, 0, item_weak)
        else:
            item_weak = QTableWidgetItem('0')
            item_weak.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(1, 0, item_weak)

        if 'Moderate' in res[0]:
            item_moderate = QTableWidgetItem(str(res[0]['Moderate']))
            item_moderate.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(2, 0, item_moderate)
        else:
            item_moderate = QTableWidgetItem('0')
            item_moderate.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(2, 0, item_moderate)

        if 'Severe' in res[0]:
            item_severe = QTableWidgetItem(str(res[0]['Severe']))
            item_severe.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(3, 0, item_severe)
        else:
            item_severe = QTableWidgetItem('0')
            item_severe.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.rcg_tableWidget.setItem(3, 0, item_severe)

        item_accuracy = QTableWidgetItem(f'{res[3]:.2f}%')
        item_accuracy.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.rcg_tableWidget.setItem(4, 0, item_accuracy)

    def save_painimg(self):
        '''
        recognizers保存最剧烈疼痛帧
        :return:
        '''
        name = self.rcg_name.text()

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
        patient_name = self.dag_name.text()
        if not patient_name:
            self.dag_browser.setText("[warning]请输入患者姓名，再点击查询按钮...")
            self.dag_videoshow.clear()
            return
        else:
            my_query = f"SELECT * FROM patient where name = %s"
            self.cursor.execute(my_query, [patient_name])
            res = self.cursor.fetchone()
            if not res:
                self.dag_browser.setText("[warning]患者不存在...")
                self.dag_videoshow.clear()
                return
            else:
                self.dag_browser.setText("[success]查询成功！")
                self.dag_painlevel.setText(res[2])
                # TODO 这里给图片加点儿东西
                img_path = f'./pain_img/{patient_name}_{self.dag_painlevel.text()}.png'
                img_Image = QPixmap(img_path)
                self.dag_videoshow.setPixmap(img_Image)
            self.conn.close()

    def diagnose_reset(self):
        '''
        diagnosers点击重置按钮的功能
        :return:
        '''
        self.dag_name.setText("")
        self.dag_videoshow.clear()
        self.dag_painlevel.setText("")
        if self.dag_male.isChecked() == True:
            self.dag_male.setAutoExclusive(False)
            self.dag_male.setChecked(False)
            self.dag_male.setAutoExclusive(True)
        if self.dag_female.isChecked() == True:
            self.dag_female.setAutoExclusive(False)
            self.dag_female.setChecked(False)
            self.dag_female.setAutoExclusive(True)
        self.dag_browser.clear()
        self.dag_mechine.setChecked(False)
        self.dag_treattime.setText("")
        if self.dag_drug1.isChecked() == True:
            self.dag_drug1.setAutoExclusive(False)
            self.dag_drug1.setChecked(False)
            self.dag_drug1.setAutoExclusive(True)
        if self.dag_drug2.isChecked() == True:
            self.dag_drug2.setAutoExclusive(False)
            self.dag_drug2.setChecked(False)
            self.dag_drug2.setAutoExclusive(True)
        if self.dag_drug3.isChecked() == True:
            self.dag_drug3.setAutoExclusive(False)
            self.dag_drug3.setChecked(False)
            self.dag_drug3.setAutoExclusive(True)
        if self.dag_drug4.isChecked() == True:
            self.dag_drug4.setAutoExclusive(False)
            self.dag_drug4.setChecked(False)
            self.dag_drug4.setAutoExclusive(True)
        self.dag_remark.clear()

    def diagnose_submit(self):
        '''
        diagnosers点击提交按钮的功能
        :return:
        '''
        self.conn_mysql()
        name = self.dag_name.text()
        if not name:
            self.dag_browser.setText("[warning]请输入信息后再提交！")
            return
        painlevel = self.dag_painlevel.text()
        if self.dag_male.isChecked() == True:
            gender = '男'
        elif self.dag_female.isChecked() == True:
            gender = '女'
        else:
            gender = '男'

        if self.dag_mechine.isChecked() == True:
            mechine = '是'
        elif self.dag_mechine.isChecked() == False:
            mechine = '否'
        else:
            mechine = '否'
        mechine_time = self.dag_treattime.text()
        if not mechine_time:
            mechine_time = 'NULL'
        drug = 'NULL'
        if self.dag_drug1.isChecked() == True:
            drug = '酮铬酸'
        elif self.dag_drug2.isChecked() == True:
            drug = '氯诺昔康'
        elif self.dag_drug3.isChecked() == True:
            drug = '保泰松'
        elif self.dag_drug4.isChecked() == True:
            drug = '芬太尼'
        else:
            pass
        remark = self.dag_remark.toPlainText()
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
        self.dag_browser.setText("[success]提交成功！")

    # treatments widget的功能实现
    def treatment_search(self):
        '''
        treatments点击查询按钮的功能
        :return:
        '''
        self.conn_mysql()
        patient_name = self.trm_name.text()
        if not patient_name:
            self.trm_browser.setText("[warning]请输入患者姓名，再点击查询按钮...")
            return
        else:
            my_query = f"SELECT * FROM patient where name = %s"
            self.cursor.execute(my_query, [patient_name])
            res = self.cursor.fetchone()
            if not res:
                self.trm_browser.setText("[warning]患者不存在...")
                return
            else:
                self.trm_browser.setText("[success]查询成功！")
                self.trm_painlevel.setText(res[2])
                self.trm_gender.setText(res[3])
                self.trm_mechine.setText(res[4])
                self.trm_treattime.setText(res[5])
                self.trm_drug.setText(res[6])
                self.trm_remark.setText(res[7])

        self.conn.close()

    def treatment_reset(self):
        '''
        treatments点击重置按钮的功能
        :return:
        '''
        self.trm_name.setText("")
        self.trm_painlevel.setText("")
        self.trm_gender.setText("")
        self.trm_mechine.setText("")
        self.trm_treattime.setText("")
        self.trm_drug.setText("")
        self.trm_remark.setText("")
        self.trm_browser.setText("")
        self.trm_mechine_workmode.setCurrentIndex(0)
        self.trm_mechine_worktime.setText("")
        self.trm_durg_use.setCurrentIndex(0)
        self.trm_drug_mass.setText("")
        self.trm_drug_speed.setText("")

    # TODO 控制端的两个测试例子，这两个到时候往后挪动
    def button_medicare_ctrl(self):
        """
        控制按摩仪的程序
        :return:
        """
        workmode = self.trm_mechine_workmode.currentIndex()
        try:
            if workmode == 1:
                self.button_treatment_flag = "1"
                self.ctrl_treatment()
                self.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 2:
                self.button_treatment_flag = "2"
                self.ctrl_treatment()
                self.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 3:
                self.button_treatment_flag = '3'
                self.ctrl_treatment()
                self.trm_browser.setText('[success]治疗仪启动成功！')
            elif workmode == 0:
                self.button_treatment_flag = '4'
                self.ctrl_treatment()
                self.trm_browser.setText('[success]治疗仪启动成功！')
        except:
            self.trm_browser.setText('[warning]未连接治疗仪，无法启动治疗...')


    # TODO 控制端的两个测试例子，这两个到时候往后挪动
    def ctrl_treatment(self):
        """
        发送控制信息
        :return:
        """
        senddata = self.button_treatment_flag
        self.s.send(senddata.encode())
        time.sleep(2)

    def conn_mysql(self):
        '''
        创建mysql连接的函数
        :return:
        '''
        self.conn = pymysql.connect(user='root', password='980226', database='pain', use_unicode=True)
        self.cursor = self.conn.cursor()


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
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    loginUi = Ui()
    loginUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

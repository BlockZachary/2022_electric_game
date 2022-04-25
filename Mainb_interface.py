# _*_coding:utf-8_*_
# Author： Zachary
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from main_interface import *
import sys
from socket import *
from exe_in_pic_out_res import *
import threading


class Ui(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.video_flag = 0
        self.BN = train_BN('traindata.csv')
        self.most_pain_index = 0

        self.conn = pymysql.connect(user='root', password='980226', database='pain', use_unicode=True)
        self.cursor = self.conn.cursor()

        # try:
        #     address = "192.168.1.112"  # 8266的服务器的ip地址
        #     port = 8266  # 8266的服务器的端口号
        #     self.buffsize = 1024  # 接收数据的缓存大小
        #     self.s = socket(AF_INET, SOCK_STREAM)
        #     self.conn = ("192.168.1.113", 1234)
        #     self.s.connect((address, port))
        #     self.button_treatment_flag = "0"
        # except:
        #     print('未能成功连接设备，请重试...')

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
                    img = cv2.flip(img, 1)  # 水平翻转
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    loginUi = Ui()
    loginUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

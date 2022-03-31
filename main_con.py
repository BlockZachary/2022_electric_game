# _*_coding:utf-8_*_
# Author： Zachary

from mainwindow2 import Ui_MainWindow
from PyQt5 import QtWidgets
import threading
import sys


class Maincon(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super()
        self.setupUi(self)
        self.action()
        self.button_flag = 0

    def action(self):
        self.button_video.clicked.connect(self.open_video)
        self.button_recognize.clicked.connect(self.start_detect)

    def th(self):
        t = threading.Thread(target=self.open_video,name='t')
        t.start()

    def open_video(self):
        self.button_flag = 1
        while True:
            if self.button_flag == 1:
                print('开启摄像头')
            else:
                break

    def start_detect(self):
        self.button_flag = 0
        print("摄像头已经关闭，开始检测")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    maincon = Maincon()
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(maincon)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    maincon.show()
    sys.exit(app.exec_())

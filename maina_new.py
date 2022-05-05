# _*_coding:utf-8_*_
# Author： Zachary
import sys
import os
import threading
import time

from PyQt5.QtGui import QPixmap

from display import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class display(QMainWindow):
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

    def setupUI(self):
        # 加阴影
        self.ui.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_disp.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

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
        self.ui.selectButtonNo.toggled.connect(self.get_button)
        self.ui.selectButtonWeak.toggled.connect(self.get_button)
        self.ui.selectButtonModerate.toggled.connect(self.get_button)
        self.ui.selectButtonSevere.toggled.connect(self.get_button)

        self.ui.selectdata.clicked.connect(self.msg)

        self.ui.displaydata.clicked.connect(self.th1)

    def get_button(self):
        if self.ui.selectButtonNo.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\042-ll042\ll042t1aaunaff'
            self.painlevel = "No"
        elif self.ui.selectButtonWeak.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\043-jh043\jh043t1afaff'
            self.painlevel = "Weak"
        elif self.ui.selectButtonModerate.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\047-jl047\jl047t1aaunaff'
            self.painlevel = "Moderate"
        elif self.ui.selectButtonSevere.isChecked():
            self.selected_file = r'E:\New_OpenFace\Datasets\UNBC\Images\047-jl047\jl047t1aaunaff'
            self.painlevel = "Severe"

    def th1(self):
        t1 = threading.Thread(target=self.display_data, name='t1')
        t1.start()


    def display_data(self):
        count = 0
        self.ui.video_number.clear()
        self.ui.pain_level.clear()
        print(f'开始显示图像{self.selected_file}')
        for root, dirs_name, files_name in os.walk(self.selected_file):
            for i in files_name:
                files_name = os.path.join(root, i)
                print(files_name)
                img_Image = QPixmap(files_name)
                self.ui.label_disp.setPixmap(img_Image)
                self.ui.label_disp.setScaledContents(True)
                count += 1
                time.sleep(0.04)
        self.ui.video_number.setText(f"{count}")
        self.ui.pain_level.setText(f"{self.painlevel}")

    def msg(self):

        data_url = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", r"E:\New_OpenFace\Datasets\UNBC\Images")  # 起始路径
        self.selected_file = data_url


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dis = display()
    sys.exit(app.exec_())

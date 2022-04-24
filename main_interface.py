# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1536, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 1024, 768))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 70, 321, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1230, 60, 30, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/素材库/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 130, 1024, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recognizers = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recognizers.setFont(font)
        self.recognizers.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.recognizers.setObjectName("recognizers")
        self.horizontalLayout.addWidget(self.recognizers)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.diagnosers = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.diagnosers.setFont(font)
        self.diagnosers.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.diagnosers.setObjectName("diagnosers")
        self.horizontalLayout.addWidget(self.diagnosers)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.treatments = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treatments.setFont(font)
        self.treatments.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.treatments.setObjectName("treatments")
        self.horizontalLayout.addWidget(self.treatments)
        self.recognize_widget = QtWidgets.QWidget(self.centralwidget)
        self.recognize_widget.setGeometry(QtCore.QRect(250, 180, 1024, 621))
        self.recognize_widget.setObjectName("recognize_widget")
        self.rcg_videoshow = QtWidgets.QLabel(self.recognize_widget)
        self.rcg_videoshow.setGeometry(QtCore.QRect(40, 30, 640, 480))
        self.rcg_videoshow.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"image: url(:/images/素材库/person_2.ico);\n"
"border-radius: 10px;")
        self.rcg_videoshow.setText("")
        self.rcg_videoshow.setObjectName("rcg_videoshow")
        self.rcg_browser = QtWidgets.QTextBrowser(self.recognize_widget)
        self.rcg_browser.setGeometry(QtCore.QRect(40, 520, 640, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rcg_browser.setFont(font)
        self.rcg_browser.setStyleSheet("border-radius: 10px;\n"
"border: 1px solid rgb(0, 0, 0);")
        self.rcg_browser.setCursorWidth(1)
        self.rcg_browser.setObjectName("rcg_browser")
        self.rcg_start = QtWidgets.QPushButton(self.recognize_widget)
        self.rcg_start.setGeometry(QtCore.QRect(760, 80, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rcg_start.setFont(font)
        self.rcg_start.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(":/icons/素材库/camera-change.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rcg_start.setIcon(icon1)
        self.rcg_start.setIconSize(QtCore.QSize(30, 30))
        self.rcg_start.setObjectName("rcg_start")
        self.rcg_stop = QtWidgets.QPushButton(self.recognize_widget)
        self.rcg_stop.setGeometry(QtCore.QRect(760, 150, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rcg_stop.setFont(font)
        self.rcg_stop.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/素材库/camera.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rcg_stop.setIcon(icon2)
        self.rcg_stop.setIconSize(QtCore.QSize(30, 30))
        self.rcg_stop.setObjectName("rcg_stop")
        self.rcg_recognize = QtWidgets.QPushButton(self.recognize_widget)
        self.rcg_recognize.setGeometry(QtCore.QRect(760, 220, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rcg_recognize.setFont(font)
        self.rcg_recognize.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/素材库/face-recognition.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rcg_recognize.setIcon(icon3)
        self.rcg_recognize.setIconSize(QtCore.QSize(30, 30))
        self.rcg_recognize.setObjectName("rcg_recognize")
        self.rcg_name = QtWidgets.QLineEdit(self.recognize_widget)
        self.rcg_name.setGeometry(QtCore.QRect(770, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rcg_name.setFont(font)
        self.rcg_name.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.rcg_name.setText("")
        self.rcg_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rcg_name.setObjectName("rcg_name")
        self.rcg_save = QtWidgets.QPushButton(self.recognize_widget)
        self.rcg_save.setGeometry(QtCore.QRect(910, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rcg_save.setFont(font)
        self.rcg_save.setStyleSheet("QPushButton {\n"
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
        self.rcg_save.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/素材库/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rcg_save.setIcon(icon4)
        self.rcg_save.setIconSize(QtCore.QSize(30, 30))
        self.rcg_save.setObjectName("rcg_save")
        self.rcg_tableWidget = QtWidgets.QTableWidget(self.recognize_widget)
        self.rcg_tableWidget.setGeometry(QtCore.QRect(750, 380, 211, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rcg_tableWidget.setFont(font)
        self.rcg_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rcg_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rcg_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.rcg_tableWidget.setRowCount(5)
        self.rcg_tableWidget.setObjectName("rcg_tableWidget")
        self.rcg_tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.rcg_tableWidget.setItem(4, 0, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "智能疼痛管理系统"))
        self.recognizers.setText(_translate("MainWindow", "识别"))
        self.diagnosers.setText(_translate("MainWindow", "诊断"))
        self.treatments.setText(_translate("MainWindow", "治疗"))
        self.rcg_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.rcg_browser.setPlaceholderText(_translate("MainWindow", "[操作提示]"))
        self.rcg_start.setText(_translate("MainWindow", "开始拍摄图像"))
        self.rcg_stop.setText(_translate("MainWindow", "停止拍摄图像"))
        self.rcg_recognize.setText(_translate("MainWindow", "疼痛表情识别"))
        self.rcg_name.setPlaceholderText(_translate("MainWindow", "患者姓名："))
        item = self.rcg_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.rcg_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Weak"))
        item = self.rcg_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", " Moderate"))
        item = self.rcg_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Severe"))
        item = self.rcg_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "准确率"))
        item = self.rcg_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "帧数"))
        __sortingEnabled = self.rcg_tableWidget.isSortingEnabled()
        self.rcg_tableWidget.setSortingEnabled(False)
        self.rcg_tableWidget.setSortingEnabled(__sortingEnabled)
import resource_interface

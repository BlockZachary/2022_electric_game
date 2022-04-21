# _*_coding:utf-8_*_
# Author： Zachary

from login import *

class Ui(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # 隐藏框体
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 加阴影
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    loginUi = Ui()
    loginUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# _*_coding:utf-8_*_
# Author： Zachary
import os

import cv2
import time,shutil

def capmethod():
    try:
        os.mkdir('./data_set')
    except:
        shutil.rmtree('./data_set')
        os.mkdir('./data_set')
    flag = 0
    cam = cv2.VideoCapture(0)
    cam.set(3, 800)  # set video width
    cam.set(4, 600)  # set video height
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # 水平翻转
        cv2.imshow("pic", img)
        # time.sleep(0.1)
        cv2.imwrite(f'./data_set/{flag}_pic.png',img)
        flag += 1
        key = cv2.waitKey(10)


capmethod()

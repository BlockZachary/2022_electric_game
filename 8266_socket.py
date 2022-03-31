# _*_coding:utf-8_*_
# Author： Zachary
import time
from socket import *
import threading



# address="172.20.10.3"   #8266的服务器的ip地址
address="192.168.1.146"   #8266的服务器的ip地址

port=8266           #8266的服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
conn = ("192.168.1.124",1234)
s.connect((address,port))



while True:
    senddata=input("请你输入：")
    s.send(senddata.encode())
    # time.sleep(2)
    #recvdata=s.recv(buffsize).decode('utf-8')
    #print(recvdata)



# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('localhost',8082))
# s.listen(1)
# sock,addr=s.accept()
# data=sock.recv(1024)
# print('收到来自%s的信息%s' %(str(addr),data))
# content = "hello"
# con = bytes(content)
# sock.send(con)
# s.close()
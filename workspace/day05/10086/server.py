#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,addr =  sk.accept()
    conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.')
    Flag = True
    while Flag:
        data = conn.recv(1024)
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('通过可能会被录音.balabala一大推')
        else:
            conn.sendall('请重新输入.')
    conn.close()
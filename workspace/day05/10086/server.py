#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,addr =  sk.accept()
    conn.sendall('��ӭ�µ� 10086��������1xxx,0ת�˹�����.')
    Flag = True
    while Flag:
        data = conn.recv(1024)
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('ͨ�����ܻᱻ¼��.balabalaһ����')
        else:
            conn.sendall('����������.')
    conn.close()
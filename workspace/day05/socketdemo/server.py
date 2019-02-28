#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket
from _mysql import result

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)   #最多连接数
while True:
    conn,address = sk.accept()
    #result = sk.accept()
    #print result
    #print type(result)
    #conn,address
    conn.send('hello.')
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()
    
    




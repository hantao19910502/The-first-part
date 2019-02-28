#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket
import sys

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)

while True:

    data = sk.recv(1024)
    print data
    inp = raw_input('')
    sk.sendall(inp)
    if inp == 'exit':
        break
    
sk.close()
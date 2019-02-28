#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
while True:
    inp = raw_input('Êý¾Ý£º').strip()
    if inp == 'exit':
        break
    sk.sendto(inp,ip_port)

sk.close()
    
    
#!/usr/bin/env python
#_*_coding:utf-8_*_


import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'C:/tmp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            #��ȡ���󷽷����ļ������ļ���С
            cmd,file_name,file_size = pre_data.split('|')
            #�Ѿ������ļ��Ĵ�С
            recv_size = 0
            #�ϴ��ļ�·��ƴ��
            file_dir = os.path.join(base_path,file_name)
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                #δ�ϴ���ϣ�
                if int(file_size)>recv_size:
                    #������1024�����ܽ��յ�С��1024
                    data = conn.recv(1024) 
                    recv_size+=len(data)
                #�ϴ���ϣ����˳�ѭ��
                else:
                    recv_size = 0
                    Flag = False
                    continue
        
                #д���ļ�
                f.write(data)
            print 'upload successed.'
            f.close()
    
instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
instance.serve_forever()    
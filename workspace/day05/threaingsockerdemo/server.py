#!/usr/bin/env python
#_*_coding:utf-8_*_

import SocketServer


class  MyServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        #print self.request,self.client_address,self.server
        while True:
            conn = self.request
            conn.send('hello.')
            flag = True
            while flag:
                data = conn.recv(1024)
                print data
                if data == 'exit':
                    flag = False
                conn.send('sb')
            conn.close()

    def finish(self):   
        pass
        
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()

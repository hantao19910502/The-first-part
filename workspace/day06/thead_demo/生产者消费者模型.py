#!/usr/bin/env python
#_*_coding:utf-8_*_

from threading import Thread
from Queue import Queue
import time
class Procuder(Thread):
    def __init__(self,name,queue):
        '''
        @param name: 消费者的名字
        @param queue:容器
        '''
        self.__Name = name
        self.__Queue = queue
        super(Procuder, self).__init__()
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print '%s 生产一个包子' %(self.__Name,)               
                #Thread.run(self)
        
class Consuner(Thread):
    def __init__(self,name,queue):
        '''
        @param name: 消费者的名字
        @param queue:容器
        '''
        self.__Name = name
        self.__Queue =  queue
        super(Consuner,self).__init__()
    def run(self):
        while True:
            if self.__Queue.empty():
                    time.sleep(1)
            else:
                    self.__Queue.get()
                    time.sleep(1)
                    print '%s 消费一个包子' %(self.__Name,)              
                    #Thread.run(self)
        
que = Queue(maxsize=10)
baogou1 = Procuder('老狗1',que)
baogou1.start()
baoguo2 = Procuder('老狗2',que)
baoguo2.start()
baoguo3 = Procuder('老狗3',que)
baoguo3.start()

for h in range(5):
    name = 'chentao%d' % (h,)
    temp = Consuner(name,que)
    temp.start()
    

#放数据和取数据的方法
'''
que.put('1')
que.put('2')

#print que.qsize()  队列的大小

print 'get:',que.get()
print 'get:',que.get()
'''
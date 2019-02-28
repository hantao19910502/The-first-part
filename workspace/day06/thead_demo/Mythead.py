#!/usr/bin/env python
#_*_coding:utf-8_*_


#run方法的重写
from threading import Thread
import time


class Mythread(Thread):
    def run(self):
        print "mythread"
        time.sleep(2)
        Thread.run(self)
        
        
def Bar():
    print 'bar'
    
t1 = Mythread(target=Bar)
t1.start()
t1.join()
print 'over '


#
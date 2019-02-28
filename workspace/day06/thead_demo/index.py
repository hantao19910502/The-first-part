#!/usr/bin/env python
#_*_coding:utf-8_*_


from threading import Thread
import time
def Foo(arg,v):
    #模拟耗时的操作
    for item in range(100):
        print item
        time.sleep(1)
print 'before'   
#线程一 
t1 = Thread(target=Foo,args=('ddd',2,))
print t1.isDaemon()   #查看线程的状态
t1.setDaemon(True)    #设置状态
t1.start()            #执行线程
print t1.getName()    #get线程的名字
t1.join(5)            #主线程执行到print t1,getName的时候等待五秒
#线程二
#t2 = Thread(target=Foo,args=('ddd',2,))
#t2.setDaemon(True)
#t2.start()
#print t2.getName()
print 'after'
        

#主线程执行完了，子线程就不会执行了  
time.sleep(10)



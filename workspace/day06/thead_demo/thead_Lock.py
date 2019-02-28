#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading
import time
 
gl_num = 0


'''
def Func():
    lock.acquire()
    global gl_num
    gl_num +=1
    time.sleep(1)
    print gl_num
    lock.release()
    
lock = threading.Lock()   
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
'''

'''
gl_num1 = 0
def Func():
    global gl_num
    global gl_num1 
    time.sleep(1)
    lock.acquire()
    gl_num +=1
    lock.acquire()
    gl_num1 +=2
    lock.release()
    lock.release()
    print gl_num
    
lock = threading.RLock()    #如果不用RLock两个防止死锁  
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
'''
gl_num1 = 0
def Func(n):
    time.sleep(1)
    global gl_num
    samp.acquire()
    time.sleep(0.001)
    gl_num +=1
    print '%s' % gl_num
    samp.release()

    
samp = threading.BoundedSemaphore(4)    #四个线程同时进入，只输出一个值
for i in range(200):
    t = threading.Thread(target=Func,args=(i,))
    t.start()


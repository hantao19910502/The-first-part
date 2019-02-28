#!/usr/bin/env python
#_*_coding:utf-8_*_

from multiprocessing import Process,Queue
from test.test_threading_local import target
'''
#开辟了一块内存空间
def f(q,n):
    q.put([n,'hello'])
   
if __name__ == '__main__':
    q = Queue()
    for h in range(5):
        P = Process(target=f,args=(q,h))
        P.start()
    for h in range(5):
        print q.get()
'''       
#以上的方法就可以在一个队列或者一快内存里开辟多个进程的方法
print '============不用共享内存的===================='

#开辟了五个内存空间
import Queue as Q2
def f(q,n):
    q.put([n,'hello'])
    print q.get()
if __name__ == '__main__':
    q = Q2.Queue()
    for h in range(5):
        P = Process(target=f,args=(q,h))
        P.start()
        
'''
[hantao@sjs-yunwei-base-3-200 scripes]$ python mul2.py   
[0, 'hello']
[1, 'hello']
[2, 'hello']
[3, 'hello']
[4, 'hello']
'''
        
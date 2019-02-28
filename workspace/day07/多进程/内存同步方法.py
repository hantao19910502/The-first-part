#!/usr/bin/env python
#_*_coding:utf-8_*_
from test.test_threading_local import target

#主进程和子进程进行同步的方法是通过value array方法实现的
'''
from multiprocessing import Process,Value,Array
from test.test_threading_local import target

def f(n,a,raw):
    n.value = 3.14
    for h in range(5):
        a[h] = -a[h]
    raw.append(9999)
    print raw
    
if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('h',range(10))
    raw_list = range(10)
    print num.value
    print arr[:]

    p = Process(target=f,args=(num,arr,raw_list))
    p.start()
    p.join()
    print num.value
    print arr[:]
    
 '''   
#manager实现内存共享

from multiprocessing import Process,Manager

def f(d,l):
    d[1] = 1
    d[2] = 2
    d[0.25] = None
    l.reverse()        #倒转
    
     
if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    P = Process(target=f,args=(d,l))
    P.start()
    P.join()
    print d
    print l
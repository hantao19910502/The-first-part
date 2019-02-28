#!/usr/bin/env python
#_*_coding:utf-8_*_

from multiprocessing import Process,Lock
import time
from test.test_threading_local import target
def f(l,i):
    time.sleep(0.5)
    #l.acquire()
    print 'hello world',i
    #l.release()

if __name__ == '__main__':
    lock = Lock()
    for h in range(10):
        p = Process(target=f,args=(lock,h))
        p.start()
        p.join()
        
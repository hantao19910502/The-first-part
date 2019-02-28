#!/usr/bin/env python
#_*_coding:utf-8_*_

from multiprocessing import Process
import os
from test.test_threading_local import target

def info(title):
    print title
    print 'module name',__name__
    if hasattr(os, 'getppid'):
        print 'parent process:',os.getppid()
    print 'process id:',os.getpid()

def f(name):
    info('function f')
    print 'hello',name


if __name__ == '__main__':
    info('main line')
    print '--------------'
    p =  Process(target=f,args=('bob',))
    p.start()
    p.join()   
#!/usr/bin/env python
#_*_coding:utf-8_*_

from multiprocessing import Process,Queue
from test.test_threading_local import target
'''
#������һ���ڴ�ռ�
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
#���ϵķ����Ϳ�����һ�����л���һ���ڴ��￪�ٶ�����̵ķ���
print '============���ù����ڴ��===================='

#����������ڴ�ռ�
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
        
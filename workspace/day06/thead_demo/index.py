#!/usr/bin/env python
#_*_coding:utf-8_*_


from threading import Thread
import time
def Foo(arg,v):
    #ģ���ʱ�Ĳ���
    for item in range(100):
        print item
        time.sleep(1)
print 'before'   
#�߳�һ 
t1 = Thread(target=Foo,args=('ddd',2,))
print t1.isDaemon()   #�鿴�̵߳�״̬
t1.setDaemon(True)    #����״̬
t1.start()            #ִ���߳�
print t1.getName()    #get�̵߳�����
t1.join(5)            #���߳�ִ�е�print t1,getName��ʱ��ȴ�����
#�̶߳�
#t2 = Thread(target=Foo,args=('ddd',2,))
#t2.setDaemon(True)
#t2.start()
#print t2.getName()
print 'after'
        

#���߳�ִ�����ˣ����߳̾Ͳ���ִ����  
time.sleep(10)



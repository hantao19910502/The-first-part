#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading,time,Queue,random

def Proudcer(name,que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            print '%s ������һ������ =============' %(name)
        else:
            print '������������ ������������'
        time.sleep(random.randrange(5))
def Consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s ������һ������' %(name)
        except Exception:
            print 'û�а����ˡ�������������'
        time.sleep(random.randrange(6))

q = Queue.Queue()
P1 = threading.Thread(target=Proudcer,args=('����', q))
P2 = threading.Thread(target=Proudcer,args=('��ٻ', q))
P1.start()
P2.start()


C1 = threading.Thread(target=Consumer,args=('־ΰ', q))
C2 = threading.Thread(target=Consumer,args=('����', q))
C1.start()
C2.start()
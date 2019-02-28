#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading,time,Queue,random

def Proudcer(name,que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            print '%s 生产了一个包子 =============' %(name)
        else:
            print '还有三个包子 。。。。。。'
        time.sleep(random.randrange(5))
def Consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s 消费了一个包子' %(name)
        except Exception:
            print '没有包子了。。。。。。。'
        time.sleep(random.randrange(6))

q = Queue.Queue()
P1 = threading.Thread(target=Proudcer,args=('韩涛', q))
P2 = threading.Thread(target=Proudcer,args=('张倩', q))
P1.start()
P2.start()


C1 = threading.Thread(target=Consumer,args=('志伟', q))
C2 = threading.Thread(target=Consumer,args=('美震', q))
C1.start()
C2.start()
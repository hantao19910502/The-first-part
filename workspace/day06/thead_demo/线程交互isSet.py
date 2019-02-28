#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading
import time

def Proudcer():
    print 'chef:等人买包子'
    event.wait()
    event.clear()
    print 'chef:sb is coming buy baozi'
    print 'chef:正在做包子'
    time.sleep(5)
    print 'chef: 你的包子好了'
    event.set()
    
    
def Consumer():
    print '韩涛：去买包子'
    event.set()
    time.sleep(2)
    print '韩涛：wait to 拿包子'
    while True:
        '''
        @param : 不用等待这段时间可以去干点别的事情
        '''
        if event.isSet():
            print 'Thank......'
            break
        else:
            print '还你妈的没好啊？'
            time.sleep(1)
    
    
event = threading.Event()
p = threading.Thread(target=Proudcer)
c = threading.Thread(target=Consumer)
p.start()
c.start()    
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
    event.wait()
    #event.isSet()
    print 'Thank......'
    
    
event = threading.Event()
p = threading.Thread(target=Proudcer)
c = threading.Thread(target=Consumer)
p.start()
c.start()    
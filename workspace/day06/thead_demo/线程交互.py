#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading
import time

def Proudcer():
    print 'chef:���������'
    event.wait()
    event.clear()
    print 'chef:sb is coming buy baozi'
    print 'chef:����������'
    time.sleep(5)
    print 'chef: ��İ��Ӻ���'
    event.set()
    
    
def Consumer():
    print '���Σ�ȥ�����'
    event.set()
    time.sleep(2)
    print '���Σ�wait to �ð���'
    event.wait()
    #event.isSet()
    print 'Thank......'
    
    
event = threading.Event()
p = threading.Thread(target=Proudcer)
c = threading.Thread(target=Consumer)
p.start()
c.start()    
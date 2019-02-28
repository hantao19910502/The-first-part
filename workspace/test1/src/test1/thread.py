#!/usr/bin/env python
#_*_coding:utf-8_*_

from threading  import Thread

class Mythread(Thread):
    def run(self):
        B

def Bar():
    print "Bar"        
t1 = Mythread(target=Bar)
t1.start()               
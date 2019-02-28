#!/usr/bin/env python
#_*_coding:utf-8_*_


import task
import sys
import person
#from person import Information
from person import b1
from person import b2

class jieju:
    def __init__(self,jj):
        self.JJ=jj
        
    def __zuohou(self):
        print b1.Name+'和'+b2.Name,self.JJ
    def zhe(self):
        self.__zuohou()

        
j1=jieju('在一起')
j2=jieju('分手')

def JieGuo():
    aa = raw_input('guoqi/siqi:')
    if aa == 'guoqi':
        j2.zhe()
        sys.exit('结束了')
    else:
        j1.zhe()
        sys.exit('结束了')

JieGuo()
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
        print b1.Name+'��'+b2.Name,self.JJ
    def zhe(self):
        self.__zuohou()

        
j1=jieju('��һ��')
j2=jieju('����')

def JieGuo():
    aa = raw_input('guoqi/siqi:')
    if aa == 'guoqi':
        j2.zhe()
        sys.exit('������')
    else:
        j1.zhe()
        sys.exit('������')

JieGuo()
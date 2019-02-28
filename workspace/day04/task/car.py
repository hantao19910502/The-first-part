#!/usr/bin/env python
#_*_coding:utf-8_*_
import task
import person
from person import b1
from pip._vendor.distlib.locators import Page
hantao = task.person.b1
qianqian = task.person.b2 


class Car:
    def __init__(self,name,page):
        self.Name = name
        self.Page = page
    def kaiche(self):
        print hantao.Name,'开着',self.Page,'的',self.Name,'接',qianqian.Name
        print '''
               job/KaiChe
                                    去国企工作：Job/guoqi
                                   去私企工作：Job/私企
              '''
        
        
baoma = Car('宝马','一百万')
xiali = Car('夏利','三万')
benchi = Car('奔驰','三百万')
dazhong = Car('大众','二十万')

def KaiChe():
    aa = raw_input('aa：')
    if aa == 'baoma':
        baoma.kaiche()
    elif aa == 'xiali':
        xiali.kaiche()
    elif aa == 'benchi':
        benchi.kaiche()
    else:
        dazhong.kaiche()
    
KaiChe()

    
    
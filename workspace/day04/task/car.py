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
        print hantao.Name,'����',self.Page,'��',self.Name,'��',qianqian.Name
        print '''
               job/KaiChe
                                    ȥ��������Job/guoqi
                                   ȥ˽������Job/˽��
              '''
        
        
baoma = Car('����','һ����')
xiali = Car('����','����')
benchi = Car('����','������')
dazhong = Car('����','��ʮ��')

def KaiChe():
    aa = raw_input('aa��')
    if aa == 'baoma':
        baoma.kaiche()
    elif aa == 'xiali':
        xiali.kaiche()
    elif aa == 'benchi':
        benchi.kaiche()
    else:
        dazhong.kaiche()
    
KaiChe()

    
    
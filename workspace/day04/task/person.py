#!/usr/bin/env python
#_*_coding:utf-8_*_

import time
import task
import University
from University import Coll


class Information():
    def __init__(self,name,sex,age,job,salary):
        self.Name = name
        self.Sex = sex
        self.Age = age
        self.Salary = salary
    def jieshao1(self):
        print self.Name,self.Sex,'��һ��������'
    @staticmethod
    def JieShao():
        b1.jieshao1() 
        time.sleep(1)
        b2.jieshao1()
        time.sleep(1)
        print b1.Name,'��',b2.Name,'��Լһ��ȥ',task.University.bjdx.gotoColl()
        time.sleep(1)
        print b1.Name,'û�п���,����ֻ��ȥ',task.University.tjdx.gotoColl()
        time.sleep(1)
        print '''
            Please input: car/KaiChe
                          job/GuoZuo
                          jieju/JieGuo
                           
            '''     
        #bb=raw_input('���������')
b1 = Information('����','��',25,'��ά',5000)
b2 = Information('��ٻٻ','Ů',25,'��ά',5000)
Information.JieShao()







        
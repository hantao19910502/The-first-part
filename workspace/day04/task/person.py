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
        print self.Name,self.Sex,'是一名高中生'
    @staticmethod
    def JieShao():
        b1.jieshao1() 
        time.sleep(1)
        b2.jieshao1()
        time.sleep(1)
        print b1.Name,'和',b2.Name,'相约一起去',task.University.bjdx.gotoColl()
        time.sleep(1)
        print b1.Name,'没有考上,所以只能去',task.University.tjdx.gotoColl()
        time.sleep(1)
        print '''
            Please input: car/KaiChe
                          job/GuoZuo
                          jieju/JieGuo
                           
            '''     
        #bb=raw_input('你想继续吗：')
b1 = Information('韩涛','男',25,'运维',5000)
b2 = Information('张倩倩','女',25,'运维',5000)
Information.JieShao()







        
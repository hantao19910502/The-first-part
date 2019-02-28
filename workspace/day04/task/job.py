#!/usr/bin/env python
#_*_coding:utf-8_*_

class Job:
    gongzuo = '参加工作'
    def __init__(self,name,salary):
        self.Name = name
        self.__Salary = salary
    def memory(self):
        print '进入' + self.Name,'工资：',self.__Salary
        
guoqi = Job('国企',5000)
siqi = Job('私企',4000)
def GuoZuo():
    aa = raw_input('工作在')
    if aa == 'guoqi':
        print Job.gongzuo
        
        guoqi.memory()
    else:
        print Job.gongzuo
        siqi.memory()

GuoZuo()
        

#!/usr/bin/env python
#_*_coding:utf-8_*_

class Job:
    gongzuo = '�μӹ���'
    def __init__(self,name,salary):
        self.Name = name
        self.__Salary = salary
    def memory(self):
        print '����' + self.Name,'���ʣ�',self.__Salary
        
guoqi = Job('����',5000)
siqi = Job('˽��',4000)
def GuoZuo():
    aa = raw_input('������')
    if aa == 'guoqi':
        print Job.gongzuo
        
        guoqi.memory()
    else:
        print Job.gongzuo
        siqi.memory()

GuoZuo()
        

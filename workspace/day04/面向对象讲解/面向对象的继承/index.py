#!/usr/bin/env python
#_*_coding:utf-8_*_

class Father():
    def __init__(self):                      #���캯��
        self.Fname = 'fffff'
    def Func(self):
        print 'father.func'
    def Bad(self):
        print '���̺Ⱦ���ͷ'    

class Son(Father):
    def __init__(self):
        self.Sname = 'aaaaaa'
        Father.__init__(self)               #�̳и������캯���ķ���
    def Bar(self):
        print 'son.func'
    def Bad(self):
        Father.Bad(self)
        print 'son.�Ĳ�'


s1 = Son()
print s1.Sname      #����Լ��Ĺ��캯��
s1.Bar()            #ִ���Լ��ķ���
s1.Func()           #�̳и����ķ���
s1.Bad()            #�̳и����ķ������ֽ�������д
print s1.Fname      #�̳и��̳к���





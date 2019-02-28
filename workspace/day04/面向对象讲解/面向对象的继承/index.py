#!/usr/bin/env python
#_*_coding:utf-8_*_

class Father():
    def __init__(self):                      #构造函数
        self.Fname = 'fffff'
    def Func(self):
        print 'father.func'
    def Bad(self):
        print '抽烟喝酒烫头'    

class Son(Father):
    def __init__(self):
        self.Sname = 'aaaaaa'
        Father.__init__(self)               #继承父辈构造函数的方法
    def Bar(self):
        print 'son.func'
    def Bad(self):
        Father.Bad(self)
        print 'son.赌博'


s1 = Son()
print s1.Sname      #输出自己的构造函数
s1.Bar()            #执行自己的方法
s1.Func()           #继承父辈的方法
s1.Bad()            #继承父辈的方法，又进行了重写
print s1.Fname      #继承父继承函数





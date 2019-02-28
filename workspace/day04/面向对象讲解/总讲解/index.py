#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
class Person:
    xue = '血'
    
class Alex:
    xx = '没心没肺'
    def __init__(self,name):
            self.name = name
p1 = Alex('李阳')
print p1.name
 
 '''
 
class province:
    #静态字段
    mem = '中国的23个省之一'
    def __init__(self,name,capital,leader):
        #动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader
    #动态方法
    def sport_meet(self):
        print self.Name + '正在开运动会'
    #静态方法
    @staticmethod     #必须的
    def Foo():
        print '每个省要抬头反复 '
    #特性
    @property
    def Bar(self):
        print self.Name + '正在打假'
        return 'nothing'
hb = province('河北','石家庄','老大')
#print hb.Name
#print hb.Capital 
#print hb.Leader         #属于对象 ===动态字段self.xxx
#print province.mem      #属于类  ====静态字段
sd = province('山东','济南','韩涛')
#print sd
#类不能访问静态字段
#print province.Name
#对像可以访问静态字段
#print hb.mem         #字段的调用方法
#hb.sport_meet()      #动态方法的调用方法
#province.Foo()       #静态方法的调用方法
hb.Bar                #特性的调用方法
print hb.Bar



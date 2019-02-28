#!/usr/bin/env python
#_*_coding:utf-8_*_
#from optparse import Values
'''
#=====================特性========================
#经典类和形式类中的特性的区别


#经典类中的特性全部都是可读可写（没有只读的功能）
class person:
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
p1 = person()
print p1.Name         #通过特性Name,读取self.__name 的值
p1.Name = 'xxx'       #通过特性Name,设置self.__name 的值
print p1.Name


#形势类的特性默认都是只读的  ，如果需要设置，那么就需要在创建一个被装饰@xxx.setter修饰的特性

class Person(object):
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
p1 = Person()
print p1.Name         #通过特性Name,读取self.__name 的值
#p1.Name = 'xxx' 
#print p1.Name         #Error 通过特性Name设置self.__name 的值的时候，就会出错。
#AttributeError: can't set attribute

'''
#形势类的这么做的好处是防止私有变量的修改，所有的对象就只能读取，不能别修改。（例如人的基因，只能看不能修改）
'''
    @Name.setter
    def Name(self,value):
        self.__name = value
        '''     
#这样一来，就可以通过特性来修改了
#即上述中的p1.Name = 'xx' 就不会报错了


#应用场景
class Person(object):
    def __init__(self,gene,clothes):
        self.__gene = gene
        self.__clothes = clothes
        
    @property
    def Gene(self):
            return self.__gene
    @property
    def Clothes(self):
            return self.__clothes
    @Clothes.setter
    def Clothes(self,value):
            self.__clothes = value
            
#创建基因为AB的人，衣服是比基尼
b1 = Person('AB','bikini')
#print b1.Gene

#=================重新定义会报错=================
b1.Gene = 'CD'
print b1.Gene
#AttributeError: can't set attribute

#=================重新定义====================
print b1.Clothes
b1.Clothes = 'yiban'
print b1.Clothes

#私有方法不能直接更改，需要通过@xxxx.setter给私有方法一个可写的权限才能使用







#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
#类
class provice:
    #静态字段(属于类)
    memo = '中国23个省之一'
    @staticmethod
    def hantao():
        print 'nihao'
    def sport_meet(self):
        print self.Name + '正在开运动会'
                 #b1  hantao 19 
    def __init__(self,name,age):   #通过__init__实例化(name,age变量)  
        #动态字段
        self.Name = name            #声明一个变量
        self.Age = age
    #静态方法（属于类）  
    @staticmethod
    def Foo():
        print '要带头看法'
    #provice.Foo()的输出方法
    
    
    #特性（方法的方法的不同而已）
    @property
    def Bar(self):
        print self.Name + '正在打假'
        return 'nothing'
    #hb.Bar
        
#将hantao 19  封装到b1这个容器,b1就先当于一个对象
b1 = provice('hantao',19)
           
#将b1中封装对象的元素打印出来
print b1.Age                        #对象  ----动字段


#静态方法的输出方法
print provice.memo                   #静态方法



#类的特性 （1）封装  Name是定义变量的时候定义的变量
#类不能访问动态字段，对象可以访问静态字段


#每个省都可以干自己事情 （）可以对象可以做自己的事情
#动态方法
def sport_meets1(self):
    print self.Name + '是好人'

#定义做什么事情的时候输出方法：    
b1.sport_meet()   


#静态方法
provice.Foo()


#使用的类的原因---1）将重复的方法简单化（将重复的动作避免重复化编写）
#记忆的方法：1）两种方法2）两种特性
  


provice.hantao()

'''

'''
#==========================私有方法============================
from _multiprocessing import flags

class provice():
    def __init__(self,name,leader,flag):
        self.Name = name
        self.Leader = leader
        #私有字段
        self.__Thailand = flag
    #私有字段的的输出方法的（中间传递的）
    def show(self):
        print self.__Thailand   
    #私有方法（私有方法在外面是不能访问的，必须通过公有方法调用）
    def __sha(self):
        print '我爱你张倩'
    #作用就是为了调用私有方法，以便能够私有方法调用出来
    def Foo(self):
        self.__sha()  
    #可以通过特性的方式直接访问私有字段
    @property
    def Thailand(self):
        return self.__Thailand   

b2 = provice('日本','王八蛋',True)

#==============私有方法不能直接调用=====================
#print b2.__Thailand


#==============私有字段的输出方法======================
#b2.show()

#==============私有方法的输出方法======================
#b2.Foo()

#==============特性的方式直接访问私有字段==================
print b2.Thailand


#==============强行的直接调用私有方法==========================
b2._provice__sha()


'''

'''
#=====================只读方法、可写=============================
class provice(object):
    def __init__(self,name,leader,flag):
        self.Name = name
        self.Leader = leader
        self.__Thailand = flag
    #只读
    @property
    def Thailand(self):
        return self.__Thailand  
    #可写
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value 
b2 = provice('日本','王八蛋',True)
print b2.Thailand
b2.Thailand = False
print b2.Thailand    
'''


'''
#========================setter的作用的展示=====================
class test1():
    def __init__(self):
        self.__pravite = 'test 1'
        
    @property
    def Show(self):
            return  self.__pravite
 
class test2(object):
    def __init__(self):
        self.__pravite = 'test 2'
        
    @property
    def Show(self):
        return  self.__pravite
    @Show.setter
    def Show(self,value):
        self.__pravite =  value   

t1 = test1()
print t1.Show 
t1.Show = 'change 1'
print t1.Show

t2 = test2()
print t2.Show
t2.Show = 'change 2'
print t2.Show
'''



#=========================析构函数=================================
#解释：python内部函数回事自动去检验还有函数来调用这个函数，如果没有了就去通知析构函数去调用__del__,释放内存
class Foo():
    def __init__(self):
        pass
    
    def __del__(self):
        print '解释器要销毁了。我要做最后一次的呐喊'
        
    


#=========================__call__方法============================
#解释：执行的方法特殊性

class Foo():
    def __init__(self):
        pass
    
    def __del__(self):
        print '解释器要销毁了。我要做最后一次的呐喊'
    def go(self):
        print '一般方法。'
    def __call__(self):
        print '执行的call方法'
f1 = Foo()      #面向对象后面加上一个（）执行类的方法
f1.go()         #面向对象的一般执行方法
f1()            #call方法的执行方法

#一般方法。
#执行的call方法
#解释器要销毁了。我要做最后一次的呐喊


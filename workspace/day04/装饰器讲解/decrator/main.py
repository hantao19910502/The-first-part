#!/usr/bin/env python
#coding:utf-8_*_

'''
#装饰器
def outer(fun):
    def hantao():
        #print 'hantao'
        fun()
    return hantao   #放进内存
@outer              #outer(func1)
def func1():
    print 'func1'
func1()
'''

'''
#装饰器的传参
def outer(fun):
    def name(arg):
        #print 'hantao'
        fun(arg)
    return name   #放进内存
@outer              #outer(func1)
def func1(arg):
    print '姓名:',arg
func1('hantao')
'''

'''
#添加返回值
def outer(fun):
    def name(*arg,**kwargs):
        print '姓名:',arg
        ss = fun(*arg,**kwargs)    
        print '姓名:',arg   
        return ss
       
    return name   #放进内存
@outer              #outer(func1)
def func1(*arg,**kwargs):
    #print '姓名:',arg
    return 'OK'
respose = func1('hantao','hantao')
print respose

'''

def outer(fun):
    def name(*arg,**kwargs):
        return fun(*arg,**kwargs)
    return name
@outer
def test(*arg,**kwargs):
    print "OK",arg

test('hantao')





#!/usr/bin/env python
#coding:utf-8_*_

'''
#װ����
def outer(fun):
    def hantao():
        #print 'hantao'
        fun()
    return hantao   #�Ž��ڴ�
@outer              #outer(func1)
def func1():
    print 'func1'
func1()
'''

'''
#װ�����Ĵ���
def outer(fun):
    def name(arg):
        #print 'hantao'
        fun(arg)
    return name   #�Ž��ڴ�
@outer              #outer(func1)
def func1(arg):
    print '����:',arg
func1('hantao')
'''

'''
#��ӷ���ֵ
def outer(fun):
    def name(*arg,**kwargs):
        print '����:',arg
        ss = fun(*arg,**kwargs)    
        print '����:',arg   
        return ss
       
    return name   #�Ž��ڴ�
@outer              #outer(func1)
def func1(*arg,**kwargs):
    #print '����:',arg
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





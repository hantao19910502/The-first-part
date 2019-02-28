#!/usr/bin/env python
#_*_coding:utf-8_*_

from django.shortcuts import render
from django.template.context_processors import request
from django.shortcuts import render ,render_to_response
from django.shortcuts import HttpResponse
from test.test_generators import fun_tests
# Create your views here.

'''
#【第1课】01 s8day14  上节作业答疑之装饰器的使用
def outer(fun):
    def wrapper(request,*args,**kwargs):
        if  not request.session.get('username'):
            return fun(request,*args,**kwargs)
        else:
            return HttpResponse('login')
    return wrapper


def index(request,*args,**kwargs):
    print args
    #访问值 序列  (u'1',)
    return HttpResponse('index')



def  show(request,*args,**kwargs):
    print kwargs
    #访问值   字典{'page': u'1'}
    return HttpResponse('show')

'''

#【第2课】02 s8day14  自定义装饰器功能扩展
def filter(before_func,after_func):
    def outer(main_func):
        def warpper(request,*args,**kwargs):
            before_fun1 = before_func(request)
            if (before_fun1 != None):
                return before_fun1
                
            main_func1 = main_func(request)
            if (main_func1 != None):
                return main_func1
            
            after_func1 = after_func(request)
            if (after_func1 != None):
                return after_func1
        return warpper
        
    return outer

def before_index(request):
    print "before==========="
    
def after_index(request):
    print "after============"
    return HttpResponse('after')

@filter(before_index,after_index)
def index(request):
    #访问值 序列  (u'1',)
    print "index"
    return HttpResponse('index')

def  show(request,*args,**kwargs):
    print kwargs
    #访问值   字典{'page': u'1'}
    return HttpResponse('show')

def INDEX(request):
    print "================"
    return render_to_response('index.html')


#!/usr/bin/env python
#_*_coding:utf-8_*_

from django.shortcuts import render
from django.template.context_processors import request
from django.shortcuts import render ,render_to_response
from django.shortcuts import HttpResponse
from test.test_generators import fun_tests
# Create your views here.

'''
#����1�Ρ�01 s8day14  �Ͻ���ҵ����֮װ������ʹ��
def outer(fun):
    def wrapper(request,*args,**kwargs):
        if  not request.session.get('username'):
            return fun(request,*args,**kwargs)
        else:
            return HttpResponse('login')
    return wrapper


def index(request,*args,**kwargs):
    print args
    #����ֵ ����  (u'1',)
    return HttpResponse('index')



def  show(request,*args,**kwargs):
    print kwargs
    #����ֵ   �ֵ�{'page': u'1'}
    return HttpResponse('show')

'''

#����2�Ρ�02 s8day14  �Զ���װ����������չ
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
    #����ֵ ����  (u'1',)
    print "index"
    return HttpResponse('index')

def  show(request,*args,**kwargs):
    print kwargs
    #����ֵ   �ֵ�{'page': u'1'}
    return HttpResponse('show')

def INDEX(request):
    print "================"
    return render_to_response('index.html')


#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.template.context_processors import request
from django.template.context import RequestContext

# Create your views here.


def login(request):
    if  request.method  == "POST":
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'alex' and pwd == '123456':
            request.session['is_login'] = {'user':user}
            return redirect('app06/index/')
        else:
            return render_to_response('app06/login.html',{'status':'用户名或密码错误'})
    
    return render_to_response('app06/login.html')

def index(request):
    user_dict = request.session.get('is_login',None)
    print user_dict
    if user_dict:
        return render_to_response('app06/index.html',{'username':user_dict['user']})
    else:
        return render_to_response('app06/login.html')

def logout(request):
    #登出的时候销毁session
    del  request.session['is_login']
    return render_to_response('app06/login.html')
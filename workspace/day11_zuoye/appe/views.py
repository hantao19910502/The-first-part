#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import request
from django.contrib.redirects.models import Redirect

# Create your views here.



def login(request):
    ret = {'status':'123'}
    '''
    if request.method  == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_emtry = all([username,password])
        if is_emtry:
            count = models.UserInfo.object.filter(username=username,password=password).count()
            if  count == '1':
                return Redirect('appe/index/')
            else:
                ret['status'] = '用户名或密码错误'
        else:
            ret['status'] = '用户名或密码不能为空'
    else:
        return render_twebponse('appe/login.html',ret)
    '''
    return render_to_response('regrite.html',{'status':'用户和密码错误'})



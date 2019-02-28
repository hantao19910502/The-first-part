#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
# Create your views here.
from app02 import models

def index(request):
    u1 = models.UserInfo.objects.get(id=1)
    g1 = models.UserGroup.objects.get(id=2)
    #添加连表数据的方法
    #=======1、======
    #g1.user.add(u1)
    #=======2 =======
    u1.usergroup_set.add(g1)
    return HttpResponse('OK')
def index1(request):
    u1 = models.UserInfo.objects.get(username='hantao1')
    g1 = models.UserGroup.objects.get(GroupName='报警组')
    g1.user.add(u1)
    return HttpResponse('OK')
#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from ad import models
from django.http.response import HttpResponse
import os 
from pip._vendor.requests.api import request
from urllib2 import Request
from django.template.context import RequestContext
# Create your views here.

def register(request):
    #创建用户类型
    #t1 = models.UserType.objects.create(name='超级管理员')
    #t2 = models.UserType.objects.create(name='普通管理员')
    #创建用户
    t3 = models.UserType.objects.get(name='超级管理员')
    u1 = models.UserInfo.objects.create(username='张倩倩',
                                        password='198198',
                                        email='1@qq.com',
                                        user_type=t3) 
    t4 = models.UserType.objects.get(name='普通管理员')
    u1 = models.UserInfo.objects.create(username='张倩倩',
                                        password='198198',
                                        email='1@qq.com',
                                        user_type=t4)
    groupObjA = models.UserGroup.objects.create(GroupName='用户组A')
    groupObjB = models.UserGroup.objects.create(GroupName='用户组B')
    groupObjA.user.add(u1)
    groupObjB.user.add(u1)  
    return HttpResponse('注册成功.')

def login(request):
    ret = {'status':''}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_emtry = all([username,password])
        if is_emtry:
            count = models.UserInfo.objects.filter(username=username,password=password).count()
            if count == 1:
                return redirect('/ad/index/')
                #return render_to_response('index.html')
            else:
                ret['status']='用户名或者密码错误'
        else:
            ret['status']='用户名或者密码不能为空'
    return render_to_response('login.html',ret)

def index(request):
    return render_to_response('ad/index.html')

def host(request):
    ret = {'status':"",'data':None,'group':None,'groupid':None}
    usergroup = models.UserGroup.objects.all()
    #{group:'{'用户组A':1,'用户组B':2}
    ret['group'] = usergroup
    
    if request.method == 'POST':
        hostname = request.POST.get('hostname',None)
        ip = request.POST.get('ip',None)
        groupid = request.POST.get('group',None)
        is_emtry  = all([hostname,ip])
        if is_emtry:
            #groupObj = models.UserGroup.objects.get(GroupName=groupid)
            groupObj = models.UserGroup.objects.get(id=groupid)
            print groupObj
            models.Asset.objects.create(hostname=hostname,ip=ip,user_group=groupObj)
        else:
            ret['status'] = '用户或密码不能为空'
    #过滤出groupname 为用户组A的数据
    #data_groupName = models.Asset.objects.filter(user_group__GroupName='用户组A')
    #ret['data'] = data_groupName
    #过滤出groupid 为1的数据
    #groupid = models.Asset.objects.filter(user_group__id=1)
    #ret['data'] = groupid
    #sql   left join
    #获取所有数据
    All_data = models.Asset.objects.all()
    ret['data'] = All_data
    for item in All_data:
        print item
        '''
                    当前Asset序列(hantao,192.168.137.129)
                    当前Asset序列(哈娜塔,1.1.1.1)
                    当前Asset序列(韩涛,1.1)
                    当前Asset序列(韩涛,1.2)
                    当前Asset序列(meinv,1.3)
                    当前Asset序列(hantoa,123)
        '''
    return render_to_response('ad/host.html',ret)     
   
def delete(request):
    id = request.POST.get('deleteid',None)
    models.Asset.objects.get(id=id).delete()
    return redirect('/ad/host/')

def SCP(request):
    print Request.data
    if request.method == 'POST':
        ip= request.POST.get('ip',None) 
        filename= request.POST.get('filename',None) 
        print ip,filename
        os.environ['ip']=str(ip)
        os.environ['filename']=str(filename)
        uu=os.system('ls')
        print uu
        return HttpResponse(uu)
    return render_to_response('ad/scp.html')

    
    
    
    
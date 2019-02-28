#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render ,HttpResponse
from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app01 import models
from django.template.context_processors import request
# Create your views here.

@api_view(['GET','PUT','DELETE','POST'])
def addGroup(request):
    method = request.method
    if method == "POST":
        groupname = request.POST.getlist("groupname",None)
        groupname = groupname[0].replace("\r\n"," ").split()
        
        print "groupname",groupname
    
        groupbase = request.POST.getlist("groupbase",None)
        groupbase = groupbase[0].replace("\r\n"," ").split()
        print "groupbase",groupbase
        for h in range(len(groupname)):
            groupname_son = groupname[h]
            groupbase_son = groupbase[h]
        models.Grouptask.objects.create(
                                        groupname=groupname_son,
                                        groupbase=groupbase_son)
        return render_to_response('app01/addgroup.html')
    
    return render_to_response('app01/addgroup.html')

def addHost(request):
    ret = {'hostgroup':None}
    hostgroup = models.Grouptask.objects.all()
    
    ret['hostgroup']  = hostgroup
    
    method = request.method
    if method == "POST":
       hostname = request.POST.getlist("hostname",None)
       hostname = hostname[0].replace("\r\n"," ").split()
    
       role = request.POST.getlist("role",None)
       role = role[0].replace("\r\n"," ").split()
       
       hostgroup = request.POST.get("hostgroup",None)
       for item in range(len(hostname)):
           hostname = hostname[item]
           role = role[item]
           models.Host.objects.create(
                                      HostName=hostname,
                                      host_group=hostgroup,
                                      Role=role
                                      )
       return render_to_response('app01/addhost.html',ret)
    return render_to_response('app01/addhost.html',ret)

def index(request):
    return render_to_response('app01/index.html')
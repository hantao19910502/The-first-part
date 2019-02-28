#!/usr/bin/env python
#-*-coding:utf-8-*-


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from web.models import Asset,Updata_1,UserInfo
from web.form import Alogin
from pip._vendor.distlib._backport.tarfile import pwd
#from httplib import HTTPResponse

# Create your views here.

def index(request):
    return HttpResponse('index')
def Add(request,name):   
    Asset.objects.create(hostname=name)
    return HttpResponse('OK')
def Delete(request,id):   
    Asset.objects.get(id=id).delete()
    return HttpResponse('OK') 
def Update(request,id,hostname):
    '''
    obj=Asset.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
    '''
    Asset.objects.filter(id__gt=id).update(hostname=hostname)
    
    return HttpResponse('OK')

def Get(request,id):
    
    #1
    assetlist=Asset.objects.filter(id__contains=id)
    print assetlist.all()
    for items in assetlist:
        return HttpResponse(items.hostname)
   
    '''
    #2
    alldata = Asset.objects.all()
    temp = Asset.objects.all()[0:2]
    for items in alldata:
        print '1_'+items.hostname
    for items in temp:
        print '2_'+items.hostname
    alldata=Asset.objects.all().order_by('id')
    for items in alldata:
        print '3_'+items.hostname
    alldata=Asset.objects.all().order_by('-id')
    for items in alldata:
        print '4_'+items.hostname
    '''
    '''
    #3   SELECT `web_asset`.`id`, `web_asset`.`hostname`, `web_asset`.`create_date`, `web_asset`.`update_date` FROM `web_asset`
    alldata = Asset.objects.all()
    print alldata.query
    '''
    #4
    #<QuerySet [{'hostname': u'hantao123', 'id': 2L}, {'hostname': u'hantao123', 'id': 3L}]>
    #SELECT `web_asset`.`id`, `web_asset`.`hostname` FROM `web_asset`
    #4
    '''
    alldata = Asset.objects.all().values('id','hostname')
    print alldata
    print alldata.query
    
    return HttpResponse('OK')
    '''
def Updata_add(request,name,sex,job):
    Updata_1.objects.create(name=name,sex=sex,job=job)
    return HttpResponse('OK')


def Updata_delete(request,id):
    Updata_1.objects.get(id=id).delete()
    return HttpResponse('OK')

def Updata_updata(request,id,name):
    obj = Updata_1.objects.get(id=id)
    obj.name=name
    obj.save()
    return HttpResponse('OK')   
    
def Updata_get(request,id):
    assetlist = Updata_1.objects.filter(id__contains=id)
    for items in assetlist:
        return HttpResponse(items.name)   
    
def Assetlist(request):
    asset_list = Asset.objects.all()
    #把数据嵌套在html里面
    result = render_to_response('assetlist.html',{'data':asset_list,'user':'hantao'})
    return result

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd =  request.POST.get('password',None)
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result == 1:
            #return render_to_response('assetlist.html')
            return render_to_response('regrite.html')
        else:
            return render_to_response('login.html',{'status':'用户和密码错误'})
    else:
        return render_to_response('login.html')
def Alogins(request):
    repiter = Alogin()
    if request.method == 'POST':
        form = Alogin(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print data
        else:
            print form.errors.as_json()
        
    return render_to_response('regrite.html',{'form':repiter})





    
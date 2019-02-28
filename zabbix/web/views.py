#!/usr/bin/python
# -*- coding: UTF-8 -*-



# Create your views here.

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
import models
import os
import json
import html_helper
import requests
import sys
import urllib2
import argparse
import requests
from urllib2 import URLError
reload(sys)
sys.setdefaultencoding('gbk')
from web import  models
import zabbix_api
from zabbix_api import zabbix_api
import time
import MySQLdb
import commands

# 装饰器
def outer(fun):
    def war(request,*arg,**kwargs):
	#request.session['url_sess']  = 	url
        user_dict = request.session.get('is_login', None)

        if not user_dict:
            return render_to_response('web/login1.html')
        else:
            return  fun(request,*arg,**kwargs)

    return war




@outer
def show_web_asset(request,page):
    user_dict = request.session.get('is_login', None)
    print user_dict
    # print  "======================="
    # if not user_dict:
    #     return render_to_response('web/login1.html', )

    try:
        page = int(page)
    except Exception, e:
        page = 1
    per_item = 5
    start = (page - 1) * per_item
    end = page * per_item

    All_list = models.Asset.objects.all().count()
    all_list= models.Asset.objects.all()[start:end].count()
    result = models.Asset.objects.all()[start:end]
    all = divmod(All_list, per_item)
    if all[1] == 0:
        all_page_count = all[0]
    else:
        all_page_count = all[0] + 1

    page_string = html_helper.Pager(page,all_page_count)
    ret = {'all_list': result,'page': page_string,'username':user_dict['user']}

    return  render_to_response('web/assetlist.html',ret)

@outer
def loginadmin(request):
    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        request.session['is_login'] = {'user': user}
        result = authenticate(username=user, password=pwd)
        user_dict = request.session.get('is_login', None)
        allist = request.session.get('allist', None)
        if result:
            return render_to_response('web/index.html',{'username':user_dict['user'],'allist':allist})
        else:
            return render_to_response('web/login.html',{'status':'用户和密码错误'},context_instance=RequestContext(request))
    return render_to_response('web/login.html',context_instance=RequestContext(request))

@outer
def ADD_HOST(request):
    user_dict = request.session.get('is_login', None)
    # if not user_dict:
    #     return render_to_response('web/login1.html', )
    if request.method == 'POST':
        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        hostnane = request.POST.get('hostname',None)
        ip = request.POST.get('ip', None)
        groupid = request.POST.get('groupid',None)
	proxyid = request.POST.get('proxyid',None)
        headers = {'content-type': 'application/json'}

        templateid = request.POST.get('templateid',None)
        p = zabbix_api()
        username = request.session.get('username', None)
        password = request.session.get('password', None)
        print 'xxx', p.login(username, password)
        add_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.create",
                "params": {
                    "host": hostnane,
                    "interfaces": [
                        {
                            "type": 1,
                            "main": 1,
                            "useip": 1,
                            "ip": ip,
                            "dns": "",
                            "port": "10050"
                        }
                    ],
                    "groups": [
                        {
                            "groupid": groupid
                        }
                    ],
		    "proxy_hostid":proxyid
                },
                "auth": p.login(username, password),
                "id": 1
            }
        )
        b = requests.post(url, data=add_host, headers=headers)

        get_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "host": [
                            hostnane,
                        ]
                    }
                },
                "auth": p.login(username, password),
                "id": 1
            }
        )
        e = requests.post(url, data=get_host, headers=headers)
        result1 = e.text
        result1 = result1.encode("utf-8")
        result1=eval(result1)
        result = result1.get("result")
        result = result[0]
        hostid = result.get("hostid")
        add_template = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "template.massadd",
                "params": {
                    "templates": [
                        {
                            "templateid": templateid
                        }
                    ],
                    "hosts": [
                        {
                            "hostid": hostid
                        }
                    ]
                },
                "auth": p.login(username, password),
                "id": 1
            }
        )


        h = requests.post(url, data=add_template, headers=headers)

        return HttpResponse(h.text)
    return render_to_response('web/add_host.html', {'username':user_dict['user']})

@outer
def TEXT(request):
    user_dict = request.session.get('is_login', None)
    # if not user_dict:
    #     return render_to_response('web/login1.html', )
    if request.method == 'POST':
        '''定义请求条件'''
        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}
        hostnane = request.POST.get('hostname', None)
        hostname = hostnane.encode("utf8").strip("\n").split()    # 解码列表化
        ip = request.POST.get('ip', None)
        ip = ip.encode("utf8").strip("\n").split()
        groupid = request.POST.get('groupid', None)
        templateid = request.POST.getlist('templateid',None)
        proxyid = request.POST.get('proxyid',None)
        p = zabbix_api()
        username = request.session.get('username', None)
        password = request.session.get('password', None)
        print 'xxx', p.login(username, password)
        if len(hostnane) == 0  or len(groupid)  == 0  or len(templateid) == 0:
            return render_to_response('web/mass_addhost.html', {'username': user_dict['user'], 'status': '主机信息不完整'})
        else:
            hostname_ip = dict(zip(hostname,ip))

            for hostname in hostname_ip:
                localtime = time.asctime(time.localtime(time.time()))
                localtime = time.strftime("%Y-%m-%d", time.localtime())
                localtime = str(localtime)
                user = user_dict['user']
                user = str(user)
                print type(user)
                models.zabbix_delete.objects.create(
                    ip=hostname_ip[hostname],
                    hostname=hostname,
                    last_ti=localtime,
                    user=user,
                    status_code="1")

                add_host = json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "method": "host.create",
                        "params": {
                            "host": hostname,
                            "interfaces": [
                                {
                                    "type": 1,
                                    "main": 1,
                                    "useip": 1,
                                    "ip": hostname_ip[hostname],
                                    "dns": "",
                                    "port": "10050"
                                }
                            ],
                            "groups": [
                                {
                                    "groupid": groupid
                                }
                            ],
			    "proxy_hostid":proxyid
                        },
                        "auth": p.login(username, password),
                        "id": 1
                    }
                )
                h = requests.post(url, data=add_host, headers=headers)
                h.text
                print h.text,
                get_host = json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                            "output": "extend",
                            "filter": {
                                "host": [
                                    hostname,
                                ]
                            }
                        },
                        "auth": p.login(username, password),
                        "id": 1
                    }
                )
                e = requests.post(url, data=get_host, headers=headers)
                result1 = e.text
                result1 = result1.encode("utf-8")
                result1 = eval(result1)
                result = result1.get("result")
                print result
                result = result[0]
                hostid = result.get("hostid")

                for template in templateid:
                    add_template = json.dumps(
                        {
                            "jsonrpc": "2.0",
                            "method": "template.massadd",
                            "params": {
                                "templates": [
                                    {
                                        "templateid":template
                                    }
                                ],
                                "hosts": [
                                    {
                                        "hostid": hostid
                                    }
                                ]
                            },
                            "auth": p.login(username, password),
                            "id": 1
                        }
                    )
                    h = requests.post(url, data=add_template, headers=headers)
                    h.text

            return render_to_response('web/mass_addhost.html', {'username':user_dict['user'],'status':'主机创建完成'})
    return render_to_response('web/mass_addhost.html', {'username':user_dict['user']})

@outer
def INDEX(request):
    user_dict = request.session.get('is_login', None)
    if user_dict:
        return render_to_response('web/index.html', {'username':user_dict['user']})
    else:
        return render_to_response('web/login.html', context_instance=RequestContext(request))

def login(request):
    p = zabbix_api()
    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        request.session['is_login'] = {'user': user}
        user_dict = request.session.get('is_login', None)
        allist = request.session.get('allist', None)
        request.session['username'] = user
        request.session['password'] = pwd
        url_sess = request.session.get('url_sess', None)
	print url_sess
        if p.login(user,pwd):
            return render_to_response('web/zhanshi.html',{'username':user_dict['user'],'allist':allist})
        else:
            return render_to_response('web/login1.html',{'status':'用户和密码错误'})
    return render_to_response('web/login1.html',)

@outer
def delete_one(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )

    if request.method == 'POST':
        ip = request.POST.get('nip', None)

        p = zabbix_api()
        p.delete(ip)
        return redirect('/web/zhanshi/available/1')

@outer
def delete_hosts(request):

    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )

    try:

        if request.method == 'POST':
            ip = request.POST.getlist('ip', None)
            ip = ip[0].replace("\r\n"," ").split()
            if len(ip) == 0:
                return render_to_response('web/deletehosts.html', {'status': '主机列表不能为空', 'username': user_dict['user']})
                exit()
            else:
                for ip in ip:
                    p = zabbix_api()
                    p.delete(ip)
                    localtime = time.asctime(time.localtime(time.time()))
                    localtime = time.strftime("%Y-%m-%d", time.localtime())
                    localtime = str(localtime)
                    user = user_dict['user']
                    user = str(user)
                    print type(user)
                    models.zabbix_delete.objects.create(
                                                        ip=ip,
                                                        last_ti=localtime,
                                                        user=user,
                                                        status_code="2"
                                                        )
                return  render_to_response('web/deletehosts.html',{'status':'主机已删除','username':user_dict['user']})
    except IndexError,e:
        return render_to_response('web/deletehosts.html', {'status': '主机删除失败','username':user_dict['user']})

    return render_to_response('web/deletehosts.html',{'username':user_dict['user']})

@outer
def update_hostid(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )
    if request.method == 'POST':
        ip = request.POST.getlist('ip', None)
        ip = ip[0].replace("\r\n", " ").split()
        genber = request.POST.get('genber', None)
        print genber
        if genber == "male":
            genber = 0
        else:
            genber = 1
        if len(ip) == 0:
            return render_to_response('web/update_hostid.html',{'status':'主机列表不能为空','username':user_dict['user']})
        else:
            p = zabbix_api()
            for ip in ip:
                try:
                    p.update_hoststatus(ip,genber)
                except Exception,e:
                    continue
            return render_to_response('web/update_hostid.html',{'status': '主机操作已完成','username':user_dict['user']})
    return render_to_response('web/update_hostid.html',{'username':user_dict['user']})


@outer
def GameProject_Register(request):
    if request.method == "POST":
        gameproject_name = request.POST.get('project',None)
        project_chine = request.POST.get('project_chine',None)
        if gameproject_name and project_chine is not None:
            models.gameproject_name.objects.create(gameproject_name=gameproject_name,
                                                   gameproject_name_chinese=project_chine)
        return render_to_response('web/register.html')
    return render_to_response('web/register.html')

@outer
def  scp(request):
    if request.method == "POST":
        pass

@outer
def ziban(request):
    return render_to_response('web/ziban.html')
@outer
def zhanshi(request,key,val,page):
    p = zabbix_api()
    status_name = {}
    if key == "available" and val == "2":
        status_name="宕机状态"

    elif key == "status" and val == "1":
        status_name="禁止状态"

    else:
        status_name="非监控状态"

    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )
    if request.method == 'GET':

        try:
            page = int(page)
        except Exception, e:
            page = 1
        per_item = 50
        start = (page - 1) * per_item
        end = page * per_item

        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}
        username = request.session.get('username',None)
        password = request.session.get('password',None)
        print 'xxx',p.login(username,password)
        all_host =  json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": "extend",
                        "filter": {key:val},
                        "selectInterfaces": ["ip"],
                    },
                    "id": 2,
                    "auth": p.login(username,password)
                }
        )
        e = requests.post(url, data=all_host, headers=headers)
        result1 = e.text
        result1 = result1.encode("utf-8")
        result1 = eval(result1)
        result = result1.get("result")



        # ----------------给前端图表传数据   开始-----------------
        for interface in result:
            interface["interfaces"] = interface["interfaces"][0]["ip"]

        status = {'0':'available','1':'status','2':'available'}
        status_html={}

        for stu,f in status.items():
            status_one = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": "extend",
                        "filter": {f: stu},

                    },
                    "id": 2,
                    "auth": "e40f54a7efb0671b54073832e51693de"
                }
            )
            f = requests.post(url, data=status_one, headers=headers)

            result2 = f.text
            result2 = result2.encode("utf-8")
            result2 = eval(result2)
            result2 = result2.get("result")

            # 排除列表中的包含“YZ/JXQ”
            # =================================================
            tag = 0
            for num in range(len(result2)):
                a = num - tag
                if "YZ" in result2[a]['host'] or "JXQ" in result2[a]['host']:
                    del result2[a]
                    tag += 1
            # ==================================================
            status_num = len(result2)
            status_html[stu]=status_num
        # ----------------给前端图表传数据   结束-----------------

        tag = 0
        for num in range(len(result)):

            a = num - tag
            if "YZ" in result[a]['host'] or "JXQ" in result[a]['host']:

                del result[a]
                tag+=1

        All_list = len(result)
        result = result[start:end]
        all = divmod(All_list, per_item)
        if all[1] == 0:
            all_page_count = all[0]
        else:
            all_page_count = all[0] + 1
        page_string = html_helper.Pager(page, all_page_count)



        ret = {'all_list': result, 'page': page_string,'status_html':status_html,'username':user_dict['user'],"status_name":status_name}
        return render_to_response('web/zhanshi.html',ret,)
    return render_to_response('web/zhanshi.html',{'username':user_dict['user']})


def getInfo(ip):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    all_host = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "host": []
                },
                "selectInterfaces": ["ip"]
            },
            "auth": "e40f54a7efb0671b54073832e51693de",
            "id": 1
        })
    e = requests.post(url, data=all_host, headers=headers)
    result1 = e.text
    result1 = result1.encode("utf-8")
    result1 = eval(result1)
    result = result1.get("result")
    for result1 in result:
        if result1["interfaces"][0]["ip"] == ip:
            return result1['host']
        else:
            continue
@outer
def SEARCH(request,page):
    p = zabbix_api()
    username = request.session.get('username', None)
    password = request.session.get('password', None)
    print 'xxx', p.login(username, password)
    if request.method == 'POST':

        try:
            page = int(page)
        except Exception, e:
            page = 1
        per_item = 50
        start = (page - 1) * per_item
        end = page * per_item

        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}

        ip = request.POST.get('ip', None)

        if  ip.startswith('1'):
            ip = getInfo(ip)

        all_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "extend",
                    "filter": {'host': ip},
                    "selectInterfaces": ["ip"],
                },
                "id": 2,
                "auth": p.login(username, password)
            }
        )
        e = requests.post(url, data=all_host, headers=headers)
        result1 = e.text
        result1 = result1.encode("utf-8")
        result1 = eval(result1)
        result = result1.get("result")

        # ----------------给前端图表传数据   开始-----------------
        for interface in result:
            interface["interfaces"] = interface["interfaces"][0]["ip"]



        status = {'0': 'available', '1': 'status', '2': 'available'}
        status_html = {}
        for stu, f in status.items():
            status_one = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": "extend",
                        "filter": {f: stu},

                    },
                    "id": 2,
                    "auth": p.login(username, password)
                }
            )
            f = requests.post(url, data=status_one, headers=headers)

            result2 = f.text
            result2 = result2.encode("utf-8")
            result2 = eval(result2)
            result2 = result2.get("result")

            # 排除列表中的包含“YZ/JXQ”
            # =================================================
            tag = 0
            for num in range(len(result2)):
                a = num - tag
                if "YZ" in result2[a]['host'] or "JXQ" in result2[a]['host']:
                    del result2[a]
                    tag += 1
            # ==================================================
            status_num = len(result2)
            status_html[stu] = status_num
        # ----------------给前端图表传数据   结束-----------------

        tag = 0
        for num in range(len(result)):

            a = num - tag
            if "YZ" in result[a]['host'] or "JXQ" in result[a]['host']:
                del result[a]
                tag += 1

        All_list = len(result)
        result = result[start:end]
        all = divmod(All_list, per_item)
        if all[1] == 0:
            all_page_count = all[0]
        else:
            all_page_count = all[0] + 1
        page_string = html_helper.Pager(page, all_page_count)

        ret = {'all_list': result, 'page': page_string, 'status_html': status_html}
        return render_to_response('web/zhanshi.html', ret, )
    return render_to_response('web/zhanshi.html')

@outer
def edit(request,hostname,hostid,ip,status_name,page):
    p = zabbix_api()
    username = request.session.get('username', None)
    password = request.session.get('password', None)
    print 'xxx', p.login(username, password)
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )
    ret = {'hostname':hostname,"hostid":hostid,'ip':ip,'username':user_dict['user'],"status_name":status_name}


    if request.method == 'POST':
        hostname = request.POST.get('hostname', None)
        hostid = request.POST.get('hostid', None)
        print "hostnane",hostname
        print "hostid",hostid
        try:
            page = int(page)
        except Exception, e:
            page = 1
        per_item = 50
        start = (page - 1) * per_item
        end = page * per_item

        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}

        all_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.update",
                "params": {
                    "hostid": hostid,
                    "host": hostname

                },
                "auth": p.login(username, password),
                "id": 1
            }
        )
        e = requests.post(url, data=all_host, headers=headers)
        result1 = e.text
        result1 = result1.encode("utf-8")
        result1 = eval(result1)
        result = result1.get("result")
        print "result",result

        return render_to_response('web/zhanshi.html', )
    print "ret", ret
    print type(ret)
    return render_to_response('web/edit.html',ret,)

@outer
def dashboard(request):
    p = zabbix_api()
    username = request.session.get('username', None)
    password = request.session.get('password', None)
    print 'xxx', p.login(username, password)
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )
    if request.method == 'GET':

        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}

        status = {'0': 'available', '1': 'status', '2': 'available'}
        status_html = {}

        for stu, f in status.items():
            status_one = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": "extend",
                        "filter": {f: stu},

                    },
                    "id": 2,
                    "auth": p.login(username, password)
                }
            )
            f = requests.post(url, data=status_one, headers=headers)

            result2 = f.text
            result2 = result2.encode("utf-8")
            result2 = eval(result2)
            result2 = result2.get("result")

            # 排除列表中的包含“YZ/JXQ”
            # =================================================
            tag = 0
            for num in range(len(result2)):
                a = num - tag
                if "YZ" in result2[a]['host'] or "JXQ" in result2[a]['host']:
                    del result2[a]
                    tag += 1
            # ==================================================
            status_num = len(result2)
            status_html[stu] = status_num
        print status_html
        ret = {'status_html':status_html,'username':user_dict['user']}
        return render_to_response('web/dashboard.html', ret, )

@outer
def user(request,TYPE):
    p = zabbix_api()
    username = request.session.get('username', None)
    password = request.session.get('password', None)
    print 'xxx', p.login(username, password)
    status_name = {}

    if TYPE == "1":
        status_name = "普通用户"

    elif TYPE == "2":
        status_name = "管理员"

    else:
        status_name = "超级管理员"
    user_dict = request.session.get('is_login', None)

    if not user_dict:
        return render_to_response('web/login1.html', )
    if request.method == 'GET':
        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}
        all_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "user.get",
                "params": {
                    "output": "extend"
                },
                "auth": p.login(username, password),
                "id": 1
            }
        )
        e = requests.post(url, data=all_host, headers=headers)
        result1 = e.text
        result1 = result1.encode("utf-8")
        result1 = eval(result1)
        result = result1.get("result")
        user_type=[]
        for result_son in result:
            if result_son['type'] == TYPE:
                user_type.append(result_son)
        ret = {"result":user_type,'username':user_dict['user'],"status_name":status_name}

        return render_to_response('web/user.html', ret,)


def createUser(request):
    pass

@outer
def zabbix_deletelist(request,TYPE,page):
    if TYPE == "1":
        status_name = "创建日志"

    elif TYPE == "2":
        status_name = "删除日志"

    else:
        status_name = "更改日志"
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web/login1.html', )
    try:
        page = int(page)
    except Exception, e:
        page = 1
    per_item = 100
    start = (page - 1) * per_item
    end = page * per_item

    All_list = models.zabbix_delete.objects.all().count()
    all_list = models.zabbix_delete.objects.all()[start:end].count()
    result = models.zabbix_delete.objects.all()[start:end]
    all = divmod(All_list, per_item)
    if all[1] == 0:
        all_page_count = all[0]
    else:
        all_page_count = all[0] + 1

    page_string = html_helper.Pager(page, all_page_count)
    ret = {'all_list': result, 'page': page_string, 'username': user_dict['user'],"status_name":status_name,"TYPE":TYPE}

    return render_to_response('web/zabbix_deletelist.html', ret)

@outer
def zabbxLostHostList(request,page):
    user_dict = request.session.get('is_login', None)
    filepath = "/home/pirate/optools/zabbix/list/"
    files = os.listdir(filepath)
    filename = "create.list"
    fullname = (os.sep).join([filepath, filename])
    print fullname
    localtime = time.strftime("%Y-%m-%d", time.localtime())
    localtime = str(localtime)
    #f = open()
    with open(fullname) as f:
        filelist = f.readlines()
        for ip in filelist:
            ip = ip.strip('\n')
            #print ip
            date_list = models.zabbixLostHostList.objects.filter(last_ti=localtime)
            date_list = list(date_list)

            if  len(date_list) != len(filelist):
                models.zabbixLostHostList.objects.create(
                    ip=ip,
                    last_ti=localtime,
                    )

    try:
        page = int(page)
    except Exception, e:
        page = 1
    per_item = 100
    start = (page - 1) * per_item
    end = page * per_item
    All_list = models.zabbixLostHostList.objects.all().count()
    all_list = models.zabbixLostHostList.objects.all()[start:end].count()
    result = models.zabbixLostHostList.objects.all()[start:end]
    all = divmod(All_list, per_item)
    if all[1] == 0:
        all_page_count = all[0]
    else:
        all_page_count = all[0] + 1

    #print "result",result
    page_string = html_helper.Pager(page, all_page_count)
    ret = {'all_list': result, 'page': page_string,"today":localtime,'username': user_dict['user']}
    return render_to_response('web/zabbixlosthostlist.html',ret)


def  get_hostid(hostname):
     url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
     headers = {'content-type': 'application/json'}
     get_host = json.dumps(
          {
              "jsonrpc": "2.0",
              "method": "host.get",
              "params": {
                  "output": "extend",
                  "filter": {
                      "host": [
                          hostname,
                      ]
                  }
              },
              "auth": 'e40f54a7efb0671b54073832e51693de',
              "id": 1
          }
     )
     e = requests.post(url, data=get_host, headers=headers)
     result1 = e.text
     result1 = result1.encode("utf-8")
     result1 = eval(result1)
     result = result1.get("result")
     print result
     result = result[0]
     hostid = result.get("hostid")
     return hostid

def get_trigger(hostname,triggername):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    get_trigger = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "trigger.get",
            "params": {
            "output": [
                "triggerid"
            ],
            "filter": {
                "hostid": get_hostid(hostname),"description": triggername

            },
            "sortorder": "DESC"
            },
            "auth": "e40f54a7efb0671b54073832e51693de",
            "id": 1
       }
    )
    e = requests.post(url, data=get_trigger, headers=headers)
    result1 = e.text
    result1 = result1.encode("utf-8")
    result1 = eval(result1)
    result = result1.get("result")
    print result
    result = result[0]
    triggerid = result.get("triggerid")
    return triggerid

def change_trigger_status(request):
    if request.method == 'POST':
 
        hostname = request.POST.getlist('hostname', None)
        hostname = hostname[0].replace("\r\n", " ").split()

        triggername = request.POST.getlist('triggername', None)
        triggername = triggername[0].replace("\r\n", " ").split()

        genber1 = request.POST.get('genber1', None)
        print 'genber',genber1
        if genber1 == "male1":
            status = 0
        else:
            status = 1

        for h in range(len(hostname)):
            url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
            headers = {'content-type': 'application/json'}
            change = json.dumps(
                {
            "jsonrpc": "2.0",
            "method": "trigger.update",
            "params": {
                "hostid":get_hostid(hostname[h]),
                "triggerid": get_trigger(hostname[h],triggername[h]),
                "status": status
            },
            "auth": "e40f54a7efb0671b54073832e51693de",
            "id": 1
            }
            )

            e = requests.post(url, data=change, headers=headers)
            result1 = e.text
        return render_to_response('web/disable_trigger.html',)
    return render_to_response('web/disable_trigger.html',)


def select_data(request,page1,page):

    try:
        page = int(page)
    except Exception, e:
        page = 1
    per_item = 50
    start = (page - 1) * per_item
    end = page * per_item

    zabbix_nanme = request.POST.get("zabbix_name", None)
    status = request.POST.get("status", None)

    print 'zabbix_nanme:',zabbix_nanme
    if status is  None:
       status = "4" 
    db = MySQLdb.connect("127.0.0.1","root","2WTWzvor8qASHZfjII2FNdJKOSwDQ5Rm","dbname")
    cursor = db.cursor()
    cursor.execute("select *,FROM_UNIXTIME(clock,'%Y-%m-%d %H:%i:%S') from alerts where  message not like '%%app%%' and message not like '%%OK%%' limit 100;")
    if zabbix_nanme:
        print "+++++++++++++++"
        cursor.execute("select *,FROM_UNIXTIME(clock,'%%Y-%%m-%%d %%H:%%i:%%S') from alerts where FROM_UNIXTIME(clock,'%%Y-%%m-%%d %%H:%%i:%%S')  like '%%%s%%' and status = 1 and message not like '%%app%%' and message not like '%%OK%%'"%(zabbix_nanme))

    data = cursor.fetchall()


    
    dic_fa = []
    for item in data:
        old_list = {}

        
        old_list['message'] = item[8]
        old_list['date'] = item[14]
        dic_fa.append(old_list)




         #print '-------------------' 
         #old_list.append(item[0])
    db.close()
    ret = {'result':dic_fa}
    return render_to_response('web/search_alert.ht',ret)

def event_acknowledge(request):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    #uri = request.get_full_path()   
    #url = "192.168.2.199:8000/%s"%(uri)
    TM = time.time()
    TM = str(TM).split('.')[0]
    if request.method == 'POST':
	eventids = request.POST.get('eventids', None)
    	info = request.POST.get('info', None)
	print info
	
    	#hostname = hostnane.encode("utf8").strip("\n").split()
    	set_acknowledge = json.dumps(
    	      	{
    	          "jsonrpc": "2.0",
    	          "method": "event.acknowledge",
    	          "params": {
    	              "eventids": eventids,
    	              "message": "%s"%(info)
    	          },
    	          "auth": "e40f54a7efb0671b54073832e51693de",
    	          "id": 1
    	      }
    	)
    	e = requests.post(url, data=set_acknowledge, headers=headers)
    	result1 = e.text
	return render_to_response('web/success.html')
    TOKEN = request.GET.get('tok',None)
    info = request.GET.get('info',None)
    eventids = request.GET.get('eventid',None)
    # ==== get acknowledge informtion begin======== 
    get_acknowledge = json.dumps(
        {       
                "jsonrpc": "2.0",
                "method": "event.get",
                "params": {
                    "output": "extend",
                    "select_acknowledges": "extend",
                    "eventids": ["%s"%(eventids)],
                    "sortfield": ["clock", "eventid"],
                    "sortorder": "DESC"
                },
                "auth": "e40f54a7efb0671b54073832e51693de",
                "id": 1
        }
        )
    e = requests.post(url, data=get_acknowledge, headers=headers)
    result1 = e.text
    #result1 = result1.encode("gbk")
    result1 = result1.decode('unicode-escape') # 解析\u6b63\u5728\u5904\u7406 汉字乱码
    result1 = eval(result1)
    result = result1.get("result")
    result = result[0]
    result = result.get('acknowledges')
    acknowledges = []
    for acknowledge in result:
	message = acknowledge['message']
	user = acknowledge['alias']
	clock = int(acknowledge['clock'])
        clock = time.localtime(clock)
        clock = time.strftime("%Y-%m-%d %H:%M:%S", clock)
	acknowledges.append({"user":user,"message":message,"clock":clock})
    f = file('/home/pirate/optools/zabbix/web/token.csv','a')
    f.write(TOKEN)
    f.write('\t')
    f.write(TM)
    f.write('\n')
    f.close()
    f = file('/home/pirate/optools/zabbix/web/token.csv','r')
    sige = False
    for line in f.readlines():
        line = line.split()
	diff = int(TM) - int(line[1])
	if TOKEN == line[0]:
		if diff > 3600:
			return render_to_response("web/false.html")
		sige = True
    if not sige:
	return render_to_response("web/false.html")

    a,b = commands.getstatusoutput('sh /home/pirate/optools/zabbix/web/Verification.sh "%s"'%(TOKEN))
    if a == 0:
    	ret = {'eventids':eventids, 'hostname':info ,'acknowledges':acknowledges}
        return render_to_response('web/acknowledge.html',ret)
    else:
        return HttpResponse("web/false.html")

def get_eventd_info(eventids):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    get_acknowledge = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "event.get",
                "params": {
                    "output": "extend",
                    "select_acknowledges": "extend",
                    "eventids": ["%s"%(eventids)],
                    "sortfield": ["clock", "eventid"],
                    "sortorder": "DESC"
                },
                "auth": "e40f54a7efb0671b54073832e51693de",
                "id": 1
        }
        )
    e = requests.post(url, data=get_acknowledge, headers=headers)
    result1 = e.text
    #result1 = result1.encode("gbk")
    result1 = result1.decode('unicode-escape') # 解析\u6b63\u5728\u5904\u7406 汉字乱码
    result1 = eval(result1)
    result = result1.get("result")
    result = result[0]
    result = result.get('acknowledges')
    acknowledges = []
    for acknowledge in result:
        message = acknowledge['message']
        user = acknowledge['alias']
        clock = int(acknowledge['clock'])
        clock = time.localtime(clock)
        clock = time.strftime("%Y-%m-%d %H:%M:%S", clock)
        acknowledges.append({"user":user,"message":message,"clock":clock})
    return acknowledges

def hantao(request , page):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    TM = time.time()
    TM = str(TM).split('.')[0] 
    try:
            page = int(page)
    except Exception, e:
            page = 1
    per_item = 50
    start = (page - 1) * per_item
    end = page * per_item    

    f = file('/tmp/events_list.csv','r')
    eventid_list=[]
    for Info in f.readlines():
	eventid = Info.split(',')[0]
	info = Info.split(',')[1]
	eventid_list.append({"eventid":eventid,"info":info})    
    acknowledges = []
    for h in eventid_list:
        a = get_eventd_info(h['eventid'])
	if len(a) == 0:
	   sig = {"alert":h['info']}
	else:
	   sig = a[0]
	   sig['alert'] = h['info']
	acknowledges.append(sig)
    All_list = len(acknowledges)
    acknowledges = acknowledges[start:end]
    all = divmod(All_list, per_item)
    if all[1] == 0:
            all_page_count = all[0]
    else:
            all_page_count = all[0] + 1
    page_string = html_helper.Pager(page, all_page_count)
    ret = {'acknowledges':acknowledges,'page': page_string}
    return render_to_response("web/acknowledge_zhanshi.html",ret)




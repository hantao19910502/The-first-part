#!/usr/bin/env  python
#coding:utf-8



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
from urllib2 import URLError
reload(sys)
sys.setdefaultencoding('utf-8')
from web01 import  models
import zabbix_api
from zabbix_api import zabbix_api
import MySQLdb


# 装饰器
def outer(fun):
    def war(request):
        print request.method
        if request.method == 'POST':
            return render_to_response('web01/login1.html')
        else:
            return  fun()
    return  war




def show_web_asset(request,page):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )
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

    return  render_to_response('web01/assetlist.html',ret)
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
            return render_to_response('web01/index.html',{'username':user_dict['user'],'allist':allist})
        else:
            return render_to_response('web01/login.html',{'status':'用户和密码错误'},context_instance=RequestContext(request))
    return render_to_response('web01/login.html',context_instance=RequestContext(request))


def ADD_HOST(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )
    if request.method == 'POST':
        url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
        hostnane = request.POST.get('hostname',None)
        ip = request.POST.get('ip', None)
        groupid = request.POST.get('groupid',None)
        headers = {'content-type': 'application/json'}
        templateid = request.POST.get('templateid',None)
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
                    ]
                },
                "auth": "e6fbc31edbf382c6203033f3d1422280",
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
                "auth": "35a9525240fdc38b9c08d57b6f0618aa",
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
                "auth": "35a9525240fdc38b9c08d57b6f0618aa",
                "id": 1
            }
        )


        h = requests.post(url, data=add_template, headers=headers)

        return HttpResponse(h.text)
    return render_to_response('web01/add_host.html', {'username':user_dict['user']})


def TEXT(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )
    if request.method == 'POST':
        '''定义请求条件'''
        url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}
        hostnane = request.POST.get('hostname', None)
        hostname = hostnane.encode("utf8").strip("\n").split()    # 解码列表化
        ip = request.POST.get('ip', None)
        ip = ip.encode("utf8").strip("\n").split()
        groupid = request.POST.get('groupid', None)
        templateid = request.POST.getlist('templateid',None)
        print templateid
        if len(hostnane) == 0  or len(groupid)  == 0  or len(templateid) == 0:
            return render_to_response('web01/mass_addhost.html', {'username': user_dict['user'], 'status': '主机信息不完整'})
        else:
            hostname_ip = dict(zip(hostname,ip))

            for hostname in hostname_ip:
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
                            ]
                        },
                        "auth": "35a9525240fdc38b9c08d57b6f0618aa",
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
                        "auth": "35a9525240fdc38b9c08d57b6f0618aa",
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
                            "auth": "35a9525240fdc38b9c08d57b6f0618aa",
                            "id": 1
                        }
                    )
                    h = requests.post(url, data=add_template, headers=headers)
                    h.text

            return render_to_response('web01/mass_addhost.html', {'username':user_dict['user'],'status':'主机创建完成'})
    return render_to_response('web01/mass_addhost.html', {'username':user_dict['user']})







def INDEX(request):
    user_dict = request.session.get('is_login', None)
    if user_dict:
        return render_to_response('web01/index.html', {'username':user_dict['user']})
    else:
        return render_to_response('web01/login.html', context_instance=RequestContext(request))





def login(request):
    p = zabbix_api()
    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        request.session['is_login'] = {'user': user}
        user_dict = request.session.get('is_login', None)
        allist = request.session.get('allist', None)
        if p.login(user,pwd):
            return render_to_response('web01/zhanshi.html',{'username':user_dict['user'],'allist':allist})
        else:
            return render_to_response('web01/login1.html',{'status':'用户和密码错误'})
    return render_to_response('web01/login1.html',)

def delete_one(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )

    if request.method == 'POST':
        ip = request.POST.get('nip', None)

        p = zabbix_api()
        p.delete(ip)
        return redirect('/web01/zhanshi/available/1')


def delete_hosts(request):

    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )

    try:

        if request.method == 'POST':
            ip = request.POST.getlist('ip', None)
            ip = ip[0].replace("\r\n"," ").split()
            if len(ip) == 0:
                return render_to_response('web01/deletehosts.html', {'status': '主机列表不能为空', 'username': user_dict['user']})
                exit()
            else:
                for ip in ip:
                    p = zabbix_api()
                    p.delete(ip)
                return  render_to_response('web01/deletehosts.html',{'status':'主机已删除','username':user_dict['user']})
    except IndexError,e:
        return render_to_response('web01/deletehosts.html', {'status': '主机删除失败','username':user_dict['user']})

    return render_to_response('web01/deletehosts.html',{'username':user_dict['user']})


def update_hostid(request):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )
    if request.method == 'POST':
        ip = request.POST.getlist('ip', None)
        ip = ip[0].replace("\r\n", " ").split()
        genber = request.POST.get('genber', None)
        if genber == "male":
            genber = 0
        else:
            genber = 1
        if len(ip) == 0:
            return render_to_response('web01/update_hostid.html',{'status':'主机列表不能为空','username':user_dict['user']})
        else:
            p = zabbix_api()
            for ip in ip:
                p.update_hoststatus(ip,genber)
            return render_to_response('web01/update_hostid.html',{'status': '主机操作已完成','username':user_dict['user']})
    return render_to_response('web01/update_hostid.html',{'username':user_dict['user']})


@outer
def GameProject_Register(request):
    if request.method == "POST":
        gameproject_name = request.POST.get('project',None)
        project_chine = request.POST.get('project_chine',None)
        if gameproject_name and project_chine is not None:
            models.gameproject_name.objects.create(gameproject_name=gameproject_name,
                                                   gameproject_name_chinese=project_chine)
        return render_to_response('web01/register.html')
    return render_to_response('web01/register.html')

@outer
def  scp(request):
    if request.method == "POST":
        pass


def ziban(request):
    return render_to_response('web01/ziban.html')

def zhanshi(request,key,val,page):
    user_dict = request.session.get('is_login', None)
    if not user_dict:
        return render_to_response('web01/login1.html', )
    if request.method == 'GET':

        try:
            page = int(page)
        except Exception, e:
            page = 1
        per_item = 50
        start = (page - 1) * per_item
        end = page * per_item

        url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}

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
                    "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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
                    "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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



        ret = {'all_list': result, 'page': page_string,'status_html':status_html}
        return render_to_response('web01/zhanshi.html',ret,)
    return render_to_response('web01/zhanshi.html')


def getInfo(ip):
    url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
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
            "auth": "35a9525240fdc38b9c08d57b6f0618aa",
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

def SEARCH(request,page):


    if request.method == 'POST':

        try:
            page = int(page)
        except Exception, e:
            page = 1
        per_item = 50
        start = (page - 1) * per_item
        end = page * per_item

        url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
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
                "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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
                    "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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
        return render_to_response('web01/zhanshi.html', ret, )
    return render_to_response('web01/zhanshi.html')



def getgroupid(request):
    pass
    conn = MySQLdb.connect(host="192.168.2.47", user="zabbix", passwd='zabbix', port=3306)
    cur = conn.cursor()
    slave_status_cur = cur.execute('select * from hosts_groups')
    slave_status = cur.fetchone()
    columns = cur.description
    print slave_status
    cur.close
    conn.close()
    return slave_status


def tree(request,ip,page):


    try:
        page = int(page)
    except Exception, e:
        page = 1
    per_item = 50
    start = (page - 1) * per_item
    end = page * per_item

    url = "http://192.168.2.47/zabbix/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}

    # ip = request.POST.get('ip', None)
    print ip
    if  ip.startswith('1'):
        ip = getInfo(ip)
    print ip

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
            "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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
                "auth": "35a9525240fdc38b9c08d57b6f0618aa"
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
    print ret
    return render_to_response('web01/tree.html', ret, )
#return render_to_response('web01/tree.html')


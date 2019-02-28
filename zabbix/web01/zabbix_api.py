#!/usr/bin/env python
#-*-coding:utf-8-*-

from django.shortcuts import render, render_to_response, redirect
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


class zabbix_api:
    def __init__(self):
        self.url = 'http://192.168.2.47/zabbix/api_jsonrpc.php'
        self.header = {"Content-Type": "application/json"}

    def login(self,username,password):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": username,
                "password": password
            },
            "id": 0
        })
        request = urllib2.Request(self.url, data)

        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
            response = json.loads(result.read())
            result.close()
            self.authID = response['result']
            return self.authID
        except URLError as e:
            print "\033[041m 认证失败，请检查URL !\033[0m", e.code
            sys.exit()
        except KeyError as e:
            print "\033[041m 认证失败，请检查用户名密码 !\033[0m", e
            sys.exit()
    def delete(self,ip):
        get_zabbix_hostid = json.dumps({
              "jsonrpc": "2.0",
              "method": "host.get",
              "params": {
                  "output": "extend",
                  "filter": {
                      "ip": [
                        ip
                      ]
                  }
              },
              "auth": "35a9525240fdc38b9c08d57b6f0618aa",
              "id": 1
        })

        request = urllib2.Request(self.url,get_zabbix_hostid)
        for key in self.header:
            request.add_header(key, self.header[key])
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        result.close()
        print 'result',result
        result= response['result']
        result = result[0]
        hostid = result.get('hostid')
        print hostid

        delete_host = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.delete",
                "params": [
                    hostid
                ],
                "auth": "35a9525240fdc38b9c08d57b6f0618aa",
                "id": 1
            }
        )
        h = requests.post(self.url, data=delete_host, headers=self.header)
        h.text
        return 'OK'

    def update_hoststatus(self,ip,genber):
        for h in ip:
            get_zabbix_hostid = json.dumps({
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "ip": [
                            ip
                        ]
                    }
                },
                "auth": "35a9525240fdc38b9c08d57b6f0618aa",
                "id": 1
            })
            request = urllib2.Request(self.url, get_zabbix_hostid)
            for key in self.header:
                request.add_header(key, self.header[key])
            result = urllib2.urlopen(request)
            response = json.loads(result.read())
            result.close()
            result = response['result']
            result = result[0]
            hostid = result.get('hostid')
            update_host_status = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.update",
                    "params": {
                        "hostid": hostid,
                        "status": genber
                    },
                    "auth": "35a9525240fdc38b9c08d57b6f0618aa",
                    "id": 1
                }
            )
            h = requests.post(self.url, data=update_host_status, headers=self.header)
            h.text

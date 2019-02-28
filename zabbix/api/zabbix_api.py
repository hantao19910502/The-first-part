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
from web import  models


class zabbix_api:
    def __init__(self):
        self.url = 'http://192.168.10.61:8088/zbx/api_jsonrpc.php'
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
              "auth": "0b5647479be5b01c555cd1dc5b088b42",
              "id": 1
        })

        request = urllib2.Request(self.url,get_zabbix_hostid)
        for key in self.header:
            request.add_header(key, self.header[key])
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        result.close()
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
                "auth": "e40f54a7efb0671b54073832e51693de",
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
                "auth": "0b5647479be5b01c555cd1dc5b088b42",
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
                    "auth": "e40f54a7efb0671b54073832e51693de",
                    "id": 1
                }
            )
            h = requests.post(self.url, data=update_host_status, headers=self.header)
            h.text
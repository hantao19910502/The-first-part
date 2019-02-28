#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import json
import requests
import sys
import urllib2


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


login = zabbix_api()

username = raw_input('username:')
password = raw_input('password:')

print login.login(username,password)

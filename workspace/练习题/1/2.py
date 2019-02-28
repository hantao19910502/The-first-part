#!/usr/bin/env python
#_*_coding:utf-8_*_


#!/usr/local/bin/python 
#coding:utf-8 
  
import json 
import urllib2 
from urllib2 import URLError 
import sys 
from sys import argv
import xlrd
  
class ZabbixTools: 
    def __init__(self): 
        self.url = 'http://www.zabbix.org/api_jsonrpc.php' 
        self.header = {"Content-Type":"application/json"} 
          
          
          
    def user_login(self): 
        data = json.dumps({ 
                           "jsonrpc": "2.0", 
                           "method": "user.login", 
                           "params": { 
                                      "user": "admin", 
                                      "password": "zabbix" 
                                      }, 
                           "id": 0 
                           }) 
          
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
      
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Auth Failed, please Check your name and password:", e.code 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            self.authID = response['result'] 
            return self.authID 
        

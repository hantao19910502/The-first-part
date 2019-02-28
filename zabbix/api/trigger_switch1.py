#!/usr/bin/python

from flask import Flask,jsonify
from flask import request

app = Flask(__name__)
import json
import requests

import sys
import MySQLdb

import os


def  get_hostname(hostid):
     sql = "select ip from zabbix.interface where hostid='%s'"%(hostid)
     db = MySQLdb.connect("192.168.10.61","zabbix","zabbix","zabbix") 
     cursor = db.cursor()
     cursor.execute(sql)
     ip = cursor.fetchall()[0][0] 
     db.close()
     return  "%s"%(ip)

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
    result = result[0]
    triggerid = result.get("triggerid")
    return triggerid

def change_status(hostname, service_name, status):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    change = json.dumps(
                {
            "jsonrpc": "2.0",
            "method": "trigger.update",
            "params": {
                "hostid":get_hostid(hostname),
                "triggerid":get_trigger(hostname,service_name),
                "status": status
            },
            "auth": "e40f54a7efb0671b54073832e51693de",
            "id": 1
            }
            )

    e = requests.post(url, data=change, headers=headers)

def check_status(hostname,service_name):
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    change = json.dumps(
                {
                        "jsonrpc": "2.0",
                        "method": "trigger.get",
                        "params": {
                            "host": hostname,
                            "output": "extend",
                            "filter": {
                                      "description": [
                                         service_name 
                                      ]

                                  }
                },
                "auth": "e40f54a7efb0671b54073832e51693de",
                "id": 1
                }
                )
    e = requests.post(url, data=change, headers=headers)
    return e.text
@app.route('/api',methods=['POST','GET'])
def main():
    try:
        json_data = {}
        json_data['hostname'] = request.form['hostname']
        json_data['service_name']= request.form['service_name']
        json_data['action']= request.form['action']
        json_data['ip']  = get_hostname(get_hostid(json_data['hostname'])) 
        json_data['status'] = 0 
        url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
        headers = {'content-type': 'application/json'}
    
        f = open("./whilelist","r")
        whilelist = []
        for ip in f.readlines():
                ip = ip.strip('\n')
                whilelist.append(ip)
        f.close()

        ip = os.popen("/sbin/ifconfig eth0 | awk -F'[: ]+' 'NR==2{print $4}'").read()
        ip = ip.split("\n")
        whilelist.append(ip[0])


        print request.remote_addr,json_data['ip']
        if request.remote_addr != json_data['ip']:
            json_data['status'] = 1
    
        if  json_data['action'] != "start" and json_data['action'] != "stop" and json_data['action'] != "status": 
            json_data['status'] = 1

        if json_data['ip'] not  in whilelist:
            json_data['status'] = 0 

        if json_data['status'] == 1:
           result = {"status": 1,"msg": 'fail',"data":"Null"}
           return json.dumps(result)


        action = 0
        if json_data['action'] == "stop":
            action = 1

        if json_data['action'] == "status":
           check_status(json_data['hostname'],json_data['service_name'])
        else:
           change_status(json_data['hostname'], json_data['service_name'], action)

        


        tirgger_status=check_status(json_data['hostname'],json_data['service_name'])

        tirgger_status = json.loads(tirgger_status)
        tirgger_status = str(tirgger_status['result'][0]['status'])

        print tirgger_status,type(tirgger_status)
        print "1",type("1")
        test="enabled"
        if tirgger_status == "1":
           test="disable"
        status = 0
        msg = "success"
        result = {
                        "status": status,
                        "msg": msg,
                        "data":{
                                  "status":test,
                                  "hostname":"%s"%(json_data['hostname']),
                                  "servicename":"%s"%(json_data['service_name'])
                               }

                 }
        return json.dumps(result)
    except Exception, e:
        result = {"status": 1,"msg": 'fail',"data":"Null"}
        return json.dumps(result)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.errorhandler(404)
def errorhandler(e):
    return '1'
@app.route("/status", methods=["POST"])
def get_host_status():
    hostname = request.form['hostname']
    service_name = request.form['service_name'] 
    
    url = "http://192.168.10.61:8088/zbx/api_jsonrpc.php"
    headers = {'content-type': 'application/json'}
    change = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "trigger.get",
                "params": {
                    "host": hostname,
                    "output": "extend",
                    "filter": {
                              "description": [
                                  service_name
                              ]

                          }
        },
        "auth": "e40f54a7efb0671b54073832e51693de",
        "id": 1
        }
        )
    e = requests.post(url, data=change, headers=headers) 
    status=json.loads(e.text)
    status = status['result'][0]['status']
    return status
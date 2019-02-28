#!/usr/bin/env python
#_*_coding:utf-8_*_


import MySQLdb
#from confparse import *

def getmdb():
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456')
    cur=conn.cursor()
    slave_status_cur=cur.execute('select user,host from mysql.user')
    slave_status=cur.fetchall()
    columns=cur.description
    #print slave_status
    tmp = {}
    for (index,column) in enumerate(slave_status):
        tmp[columns[index][0]] = column
    cur.close
    print  tmp['host'],tmp['user']
getmdb()
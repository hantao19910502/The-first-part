#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = conn.cursor()

li =[
     ('3','hanzhiwei'),
     ('4','hanmeizhen'),
]
reCount = cur.executemany('insert into test1(id,name) values(%s,%s)',li)

conn.commit()
cur.close()
conn.close()

print reCount
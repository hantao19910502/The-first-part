#!/usr/bin/env python
#_*_coding:utf-8_*_


import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()

#sql = "delete from test1 where id = %s"
sql = "update test1 set name = %s where id = 1"
parms = ('100')
reCount = cur.execute(sql,parms)

sql = "update test1 set name = %s where id = 3"
parms = ('300')
reCount = cur.execute(sql,parms)

#提交sql的命令
coun.commit()
cur.close()
coun.close()
print reCount
#执行之前
#1    200
#3    200
#执行之后
#1    100
#3    300


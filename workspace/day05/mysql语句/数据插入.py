#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()

sql = "insert into  test1(id,name) values(%s,%s)"
parms = ('2','usa1')
reCount = cur.execute(sql,parms)
#Ìá½»sqlµÄÃüÁî
coun.commit()
cur.close()
coun.close()
print reCount
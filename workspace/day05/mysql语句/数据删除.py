#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()

#sql = "delete from test1 where id = %s"
sql = "delete from test1 where name = %s"
parms = ('alin')
reCount = cur.execute(sql,parms)
#Ìá½»sqlµÄÃüÁî
coun.commit()
cur.close()
coun.close()
print reCount
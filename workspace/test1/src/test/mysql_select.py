#!/usr/bin/env python
#_*_coding:utf-8_*_


import MySQLdb
con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')

conn = con.cursor()

#sql = "select * from test"
#sql = "insert into test(id) values(2)"
#sql = "delete from test where id = 1"
#sql = "update test set id = 2 where id = 1"

aa = conn.execute(sql)

con.commit()
conn.close()
con.close()

print aa
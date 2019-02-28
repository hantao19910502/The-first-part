#!/usr/bin/env python
#_*_coding:utf-8_*_


import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()           #以列表的样式展示
sql = "select * from test1"
parms = ('test1')
reCount = cur.execute(sql)
#reCount = cur.executemany(sql,parms)

data = cur.fetchone()    #一行的写入（写入第一行）
print data

data = cur.fetchone()    #写入第二行（不写第三行就不会写入内存）
print data
#cur.scroll(0,mode='absolute')    #返回到第一行（相对定位）
cur.scroll(-1,mode='relative')    #-1的意思执行晚上上一条退回一条语句（绝对定位）

data = cur.fetchone()    #写入第二行（不写第三行就不会写入内存）
print data

cur.close()
coun.close()



'''
#=============获取自增ID===================

import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()

sql = "insert into  media(address) values(%s)"
parms = ('/usr/bin/a.txt')
reCount = cur.execute(sql,parms)
#提交sql的命令
coun.commit()

print cur.lastrowid
cur.close()
coun.close()


#实验步骤：
#     1）自增ID
# ====1    /usr/bin/a.txt
# ====2    /usr/bin/a.txt
#=====3    /usr/bin/a.txt
#=====4    /usr/bin/a.txt
#     2）删除ID
#     3）在执行
#=====5    /usr/bin/a.txt
#=====6    /usr/bin/a.txt
#=====7    /usr/bin/a.txt

'''
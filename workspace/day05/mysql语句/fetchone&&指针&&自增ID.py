#!/usr/bin/env python
#_*_coding:utf-8_*_


import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()           #���б����ʽչʾ
sql = "select * from test1"
parms = ('test1')
reCount = cur.execute(sql)
#reCount = cur.executemany(sql,parms)

data = cur.fetchone()    #һ�е�д�루д���һ�У�
print data

data = cur.fetchone()    #д��ڶ��У���д�����оͲ���д���ڴ棩
print data
#cur.scroll(0,mode='absolute')    #���ص���һ�У���Զ�λ��
cur.scroll(-1,mode='relative')    #-1����˼ִ��������һ���˻�һ����䣨���Զ�λ��

data = cur.fetchone()    #д��ڶ��У���д�����оͲ���д���ڴ棩
print data

cur.close()
coun.close()



'''
#=============��ȡ����ID===================

import MySQLdb
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
cur = coun.cursor()

sql = "insert into  media(address) values(%s)"
parms = ('/usr/bin/a.txt')
reCount = cur.execute(sql,parms)
#�ύsql������
coun.commit()

print cur.lastrowid
cur.close()
coun.close()


#ʵ�鲽�裺
#     1������ID
# ====1    /usr/bin/a.txt
# ====2    /usr/bin/a.txt
#=====3    /usr/bin/a.txt
#=====4    /usr/bin/a.txt
#     2��ɾ��ID
#     3����ִ��
#=====5    /usr/bin/a.txt
#=====6    /usr/bin/a.txt
#=====7    /usr/bin/a.txt

'''
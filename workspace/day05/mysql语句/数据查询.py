#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb

#打开门
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')

#伸出手
#cur = coun.cursor()           #以列表的样式展示
cur = coun.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#已字典的样式展示


#拿东西
reCount = cur.execute('select * from test1')


data = cur.fetchall()
#拿回手
cur.close()
#关上门
coun.close()

#print reCount

print data



#print  columns
#=========已字典的方式展示
#({'id': 1L, 'name': '100'}, {'id': 3L, 'name': '300'}, {'id': 4L, 'name': 'hanmeizhen'})

#=======以列表的样式展示的结果
#((1L, '100'), (3L, '300'), (4L, 'hanmeizhen'))







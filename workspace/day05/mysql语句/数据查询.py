#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb

#����
coun = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test')

#�����
#cur = coun.cursor()           #���б����ʽչʾ
cur = coun.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#���ֵ����ʽչʾ


#�ö���
reCount = cur.execute('select * from test1')


data = cur.fetchall()
#�û���
cur.close()
#������
coun.close()

#print reCount

print data



#print  columns
#=========���ֵ�ķ�ʽչʾ
#({'id': 1L, 'name': '100'}, {'id': 3L, 'name': '300'}, {'id': 4L, 'name': 'hanmeizhen'})

#=======���б����ʽչʾ�Ľ��
#((1L, '100'), (3L, '300'), (4L, 'hanmeizhen'))







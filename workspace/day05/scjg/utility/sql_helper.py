#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb
from scjg import conf
class MySqLHelper(object):  
    def __init__(self):
        self.__conn = conf.dict_dl
    
    def Get_Dict(self,sql,params):
        #����Ҳ�������б�ķ�ʽ����������˳���ܷ����仯
        coun = MySQLdb.connect(*self.__conn)
        #coun = MySQLdb.connect(**self.__conn)
        cur = coun.cursor()           
        reCount = cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        coun.close()
        return data
    def Get_One(self,sql,params):
        coun = MySQLdb.connect(*self.__conn)
        cur = coun.cursor()           
        reCount = cur.execute(sql,params)
        data = cur.fetchone()
        cur.close()
        coun.close()
        return data
    
        
        
'''
helper = MySqLHelper()
sql = "select * from media where id = %s"
params = (6,)
simper = helper.Get_Dict(sql, params)
print simper
'''





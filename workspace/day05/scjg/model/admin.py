#!/usr/bin/env python
#_*_coding:utf-8_*_

from scjg.utility.sql_helper import MySqLHelper

class Admin(object):
    def __init__(self):
        self.helper = MySqLHelper()
    def get_One(self,id):
        sql = 'select * from text where id = %s'
        params = (5,)
        return  self.helper.Get_One(sql,params)
    def CheckValidate(self,username,password):
        sql = "select * from test1 where username = %s and password = %s"
        params = (username,password)
        return self.helper.Get_One(sql,params)
    
    
    
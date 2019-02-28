#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
class MyExcaption(Exception):
    def __init__(self,msg):
        self.error = msg
    def __str__(self, *args, **kwargs):
        return self.error
        #return 'gai dui xiang shi MyExcaption'
        
obj = MyExcaption('自定义错误信息')
print obj
'''

def hantao(user,password):
    if user == 'alex' and password == '123':
        return True
    else:
        return False

    
try:
    res = hantao('alex','456')
    if res:
        print '登入成功'
    else:
        #print '记入到数据库'
        #print '登入失败'
        raise Exception('登入失败')             #主动触发错误
except Exception,e:
    print  '记录日志到数据库'
    print e
#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
class MyExcaption(Exception):
    def __init__(self,msg):
        self.error = msg
    def __str__(self, *args, **kwargs):
        return self.error
        #return 'gai dui xiang shi MyExcaption'
        
obj = MyExcaption('�Զ��������Ϣ')
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
        print '����ɹ�'
    else:
        #print '���뵽���ݿ�'
        #print '����ʧ��'
        raise Exception('����ʧ��')             #������������
except Exception,e:
    print  '��¼��־�����ݿ�'
    print e
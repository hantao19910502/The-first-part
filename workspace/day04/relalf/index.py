#!/usr/bin/env python
#_*_coding:utf-8_*_

#�淶  xxxx/xxxx
#==================���淽��=========================
'''
from backend import account

data = raw_input('�������ַ��')
array = data.split('/')

if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logiout()
    
#���200�������ͻ�д200�У���ש�ķ�����̫�鷳�����ܡ�

'''
#======================����ķ���ȥʵ��========================

data = raw_input('�������ַ��')
array = data.split('/')
userspace = __import__('backend.'+array[0])
mode = getattr(userspace,array[0])
func = getattr(mode,array[1])
func()


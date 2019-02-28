#!/usr/bin/env python
#_*_coding:utf-8_*_

#规范  xxxx/xxxx
#==================常规方法=========================
'''
from backend import account

data = raw_input('请输入地址：')
array = data.split('/')

if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logiout()
    
#如果200个函数就会写200行，板砖的方法，太麻烦不可能。

'''
#======================反射的方法去实现========================

data = raw_input('请输入地址：')
array = data.split('/')
userspace = __import__('backend.'+array[0])
mode = getattr(userspace,array[0])
func = getattr(mode,array[1])
func()


#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
#函数
def foo(name):
    print name,'去砍柴'

foo('liyang')
foo('hanzhiwei')
foo('hanmeizhen')
'''
from argparse import Action


'''
def logic(username):
    if username == 'alex':
        return '登入成功'
    else:
        return '登入失败'
    
def detail(user):
    print user,'**********'

if __name__ == '__main__':
    user = raw_input('请输入姓名')
    
    raw = logic(user)    #检查是否成功
    if raw == '登入成功':
        detail(user)     #显示信息
    else:
        print '没奖金了'
'''
'''
def foo(name,action):
    print name,'去',action
    
foo('hantao','吃饭')
foo('hanzhiwei','喝水')
foo('hanmeizhen','打架')
'''


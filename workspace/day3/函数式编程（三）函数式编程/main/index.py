#!/usr/bin/env python
#_*_coding:utf-8_*_
from operator import itemgetter

#arg

def foo(name,where='北京',action='砍柴'):     #设置默认值（也可以不用）
    print name,'去',where,action
    
foo('hantao','吃饭')
foo('hanzhiwei','喝水')
foo('hanmeizhen','打架')
foo('hanliang')
foo('hanweimin',where='山东',action='泡妞')


'''
#*agrs
def show(*arg):
    for item in arg:
        print item 

show('hantao','hanzhiwei','hanmeizhen','hanliang','hanweimin')

#hanzhiwei
#hanmeizhen
#hanliang
#hanweimin
'''

'''
#**kargs  字典
def show(**kargs):
    for item in kargs.items():
        print item
show(name='hantao',age='26',salarg='9000')

#('age', '26')
#('name', 'hantao')
#('salarg', '9000')
'''

'''
#白外面的字典传进去
def show(**kargs):
    for item in kargs.items():
        print item
user_dict={'k1':123,'age':34}
show (**user_dict)

#('k1', 123)
#('age', 34)
'''

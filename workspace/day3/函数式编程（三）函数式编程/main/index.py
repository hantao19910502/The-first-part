#!/usr/bin/env python
#_*_coding:utf-8_*_
from operator import itemgetter

#arg

def foo(name,where='����',action='����'):     #����Ĭ��ֵ��Ҳ���Բ��ã�
    print name,'ȥ',where,action
    
foo('hantao','�Է�')
foo('hanzhiwei','��ˮ')
foo('hanmeizhen','���')
foo('hanliang')
foo('hanweimin',where='ɽ��',action='���')


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
#**kargs  �ֵ�
def show(**kargs):
    for item in kargs.items():
        print item
show(name='hantao',age='26',salarg='9000')

#('age', '26')
#('name', 'hantao')
#('salarg', '9000')
'''

'''
#��������ֵ䴫��ȥ
def show(**kargs):
    for item in kargs.items():
        print item
user_dict={'k1':123,'age':34}
show (**user_dict)

#('k1', 123)
#('age', 34)
'''

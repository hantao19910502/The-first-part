#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
#����
def foo(name):
    print name,'ȥ����'

foo('liyang')
foo('hanzhiwei')
foo('hanmeizhen')
'''
from argparse import Action


'''
def logic(username):
    if username == 'alex':
        return '����ɹ�'
    else:
        return '����ʧ��'
    
def detail(user):
    print user,'**********'

if __name__ == '__main__':
    user = raw_input('����������')
    
    raw = logic(user)    #����Ƿ�ɹ�
    if raw == '����ɹ�':
        detail(user)     #��ʾ��Ϣ
    else:
        print 'û������'
'''
'''
def foo(name,action):
    print name,'ȥ',action
    
foo('hantao','�Է�')
foo('hanzhiwei','��ˮ')
foo('hanmeizhen','���')
'''


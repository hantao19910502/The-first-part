#!/usr/bin/env python
#_*_coding:utf-8_*_

class A:
    def __init__(self):
        print 'I am A'
    def save(self):
        print '___A_____'
class B():
    def __init__(self):
        print 'I am B'
    def save(self):
        print '__B___'
class C(B,A):                 #�̳е�˳���Ǹ�������
    def __init__(self):
        print 'I am C'
t1 = C()
t1.save()
#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
class A:
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method from A'
class B(A):
    def __init__(self):
        print 'this is B'
class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from ----C-------'
class D(B,C):
    def __init__(self):
        print 'This is D'

c= D()
c.save()

#This is D
#save method from A
'''


class A(object):                  #���ĵķ���
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method f rom A'
class B(A):
    def __init__(self):
        print 'this is B'
class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from ----C-------'
class D(B,C):
    def __init__(self):
        print 'This is D'

c= D()
c.save()

#This is D
#save method from ----C-------
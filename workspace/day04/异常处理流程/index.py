#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
try:
    data = raw_input('�������ַ��')
    array = data.split('/')
    userspace = __import__('backend.'+array[0])
    mode = getattr(userspace,array[0])
    func = getattr(mode,array[1])
    func()
except (ImportError,AttributeError),e:
    print e
    print '404'
'''



try:
    data = raw_input('�������ַ��')
    array = data.split('/')
    userspace = __import__('backend.'+array[0])
    mode = getattr(userspace,array[0])
    func = getattr(mode,array[1])
    func()
except ImportError,e:
    print 1,e
    print '404'
except AttributeError,e:
    print 2,e
    print '404'
except Exception,e:            #���۳���ʲô���󶼹��˵�
    print 3,e
    print '4041'
else:                          #û�г���ִ�е�
    print 'û�г���'
finally:                        #�����������ִ��
    print '�����������ִ��'



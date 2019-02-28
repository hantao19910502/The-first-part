#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
try:
    data = raw_input('请输入地址：')
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
    data = raw_input('请输入地址：')
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
except Exception,e:            #无论出现什么错误都过滤掉
    print 3,e
    print '4041'
else:                          #没有出错执行的
    print '没有出错'
finally:                        #无论正常与否都执行
    print '无论正常与否都执行'



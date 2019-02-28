#!/usr/bin/env python
#_*_coding:utf-8_*_

#task.car.baoma.kaiche()
import sys
try:
    aa = raw_input('你想要看一下故事情节吗:')
    if aa  ==  'yes' or aa == 'y':
        print 'person/Information'
        while True:
            data = raw_input('Please input your urladdress:')
            array = data.split('/')
            userspace = __import__('task.'+array[0])
            mode = getattr(userspace,array[0])
            func = getattr(mode,array[1])
            #func()
        
    else:
        sys.exit('就这么愉快的结束把')
except ImportError,e:
    print '404'
except NameError,e:
    print '404'
except TypeError,e:
    print '404'


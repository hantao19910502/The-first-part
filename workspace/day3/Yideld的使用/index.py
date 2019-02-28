#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
print range(10)
print xrange(10)

for item in xrange(10):
    print item
'''


#yield的使用方法
'''
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
re = foo()
for item in re:
    print item
'''

#yield的原理
def AlexReadlines():
    seek=0
    while True:
        with open('C:/tmp/temp.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return 
print AlexReadlines()
for item in AlexReadlines():
        print item,    









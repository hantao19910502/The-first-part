#!/usr/bin/env python
#_*_coding:utf-8_*_

#三元运算
'''
temp = None
if 1>3:
    print 'gt'
else:
    print 'lt'

result='gt' if 1>3 else 'lt'
print result

#lt
#lt
'''

#lambda表达式
#正常
def  foo(x,y):
    return x + y
print foo(3,5)
#lambda表达式
temp = lambda x,y,z:x+y+z 
print temp(3,5,3)







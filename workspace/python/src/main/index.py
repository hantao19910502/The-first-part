#!/usr/bin/env python
#_*_coding:utf-8_*_

name = raw_input('Please your name:')
#age = raw_input('Age:')
age = input('Age:')

print  type(age)

if age >30:
    msg = 'You are too fuching old'
else:
    msg = 'You are still quit young,go hook up some girls'


print '''
Please your infromation:%s
        your name:%s
        your age:%s
----------------------------
%s
'''% (name,name,age,msg)



5  re = [1,2,3,4,5]
1  del re[0]   re = [1,3,4,5]
2  del re[1]   re = [1,3,5]
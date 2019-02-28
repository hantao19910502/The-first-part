#!/usr/bin/env python
#!_*_codding:utf-8_*_

import sys,os
from pickle import dump
phote = 5000
food = 3000
computer = 10000

print '''
--------------------
        phote:%s
        food:%s
        computer:%s
--------------------
''' % (5000,3000,10000)

memary1 = input('You have memory:')

shop1 = input('You want to buy:')
if shop1 == 'phote':
    shop1 = 5000
elif shop1 == 'food':
    shop1 = 3000
else:
    shop1 = 10000
#os.remove('menu')
f=file('menu','w')
f.truncate()
f.close()
while memary1 >= shop1:
        memary1 = memary1 - shop1
        print memary1,shop1
        f=file('menu','a')
        f.write(str(shop1))
        f.write('\n')
        shop1 = input('You want to buy:')
else:
        #sys.exit()
        f.write(str(memary1))
        f.write('\n')
        f.close()
        f = file('menu','r')
        for line in f.readlines():
                print line,
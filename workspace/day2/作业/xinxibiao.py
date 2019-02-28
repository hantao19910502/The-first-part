#!/usr/bin/env python
#_*_coding:utf-8_*_
#########grep����####################

'''
import re
while True:
    aa = raw_input('Your name:')
    f = file('list','rb')
    new_file = file('%s.bak' % 'ceshi','wb')
    for line in f.readlines():
        m = re.search(aa,line) 
        if m != None:
           HH = line.strip('\n').split()
           none = HH[0]
           tow = HH[1]
           th = HH[2]
           mey = HH[3]
           print none,tow,th,mey

'''

'''
import sys,os

phote = 5000
food = 3000
computer = 10000
from pickle import dump

print '''
'''
--------------------
        phote:%s
        food:%s
        computer:%s
--------------------
'''
''' % (5000,3000,10000)

memary1 = input('You have memory:')
shop1 = input('You want to buy:')
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




import sys,os

def foo():
    f = file('list','r')
    for line in f.readlines():
        aa = line.strip('\n').split()
        username = raw_input('Input your name:')
        if aa[0] == username :
            print aa
        elif aa[2] == username:
            print aa
        else:
            sys.exit()
foo()

'''


import re
def foo():
    f = file('list','r')
    aa = raw_input('aa:')
    for line in f.readlines():
        bb = ''.join(line.split())
        print bb
        dd = cmp(bb,aa)
        print dd
        #print cmp('hantao19910502shandong6000','hantao')
        
foo()

'''
print cmp('hantao19910502shandong6000','xxx')
'''
        
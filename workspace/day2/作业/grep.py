#!/usr/bin/env python
#_*_coding:utf-8_*_


import re,sys
def foo():
    while True:
        aa = raw_input('Your name:')
        f = file('list','rb')
        new_file = file('%s.bak' % 'ceshi','wb')
        for line in f.readlines():
            if aa == 'exit':
                sys.exit()
            m = re.search(aa,line) 
            if m != None:
                HH = line.strip('\n').split()
                none = HH[0]
                tow = HH[1]
                th = HH[2]
                mey = HH[3]
                print none,tow,th,mey
if __name__ == '__main__':
    foo()
else:
    print "Sorry,you are f"
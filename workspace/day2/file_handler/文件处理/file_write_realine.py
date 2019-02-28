#!/usr/bin/env python
#_*_coding:utf-8_*_

FilePath = "C:/tmp/aa.txt"
#f = file(FilePath,'r')

f = file(FilePath,'w+')
f.write('hantao')
f.close()
f = file(FilePath,'r+b')
for h in f.readline():
    print h
#!/usr/bin/env python
#_*_coding:utf-8_*_

def fun(i):
     if i==1:
         return 1
     return i*fun(i-1)
 
print fun(3)
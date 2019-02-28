#!/usr/bin/env python
#_*_coding:utf-8_*_

a=1
b=1
for h in range(1,21,2):
     print '%d %d'%(a,b),
     a += b
     b += a
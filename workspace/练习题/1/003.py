#!/usr/bin/env python
#_*_coding:utf-8_*_

#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math
num = 1
while True:
    if math.sqrt(num + 100) - int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 168) - int(math.sqrt(num + 168)) == 0:
           print  num
           break
    num+=1
print    num          



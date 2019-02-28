#!/usr/bin/env python
#_*_coding:utf-8_*_

#创建异步进程

from multiprocessing import Pool
import time
def f(x):
    #print x*x
    time.sleep(3)
    return x*x

pool = Pool(processes=4)
res_list = []

for h in range(10):
    res = pool.apply_async(f,[h,])


    print '========',h
    res_list.append(res)
    
for r in res_list:
    print '----',r.get(timeout=0.5)
#multiprocessing.TimeoutError  超时报错
#===================
#print pool.map(f.range(10))
    
'''
输出结果：
======== 0
======== 1
======== 2
======== 3
======== 4
======== 5
======== 6
======== 7
======== 8
======== 9
---- 0
---- 1
---- 4
---- 9
---- 16
---- 25
---- 36
---- 49
---- 64
---- 81
'''
    
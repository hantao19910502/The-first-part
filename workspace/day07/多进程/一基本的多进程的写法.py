#!/usr/bin/env python
#_*_coding:utf-8_*_
#²¢ÐÐ
from multiprocessing import Pool
n = range(10)
def f(n):
    print  n*n
    return n*n

if __name__ == '__main__':
    p = Pool(2)
    print p.map(f,n)
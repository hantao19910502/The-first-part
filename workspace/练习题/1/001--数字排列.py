#!/usr/bin/env python
#_*_coding:utf-8_*_

cnt=0
for h in range(1,5):
    for k in range(1,5):
        for j in range(1,5):
            if h != k and h !=j and k !=j:
                print h*100+k*10+j
                cnt+=1
print cnt
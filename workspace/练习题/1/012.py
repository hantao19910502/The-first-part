#!/usr/bin/env python
#_*_coding:utf-8_*_


from math import sqrt 
def main():
    for i in range(101,201):
         flag = 1
         k = int(sqrt(i))
         for j in range(2,k+1):
             if i%j == 0:
                 flag = 0
                 break
         if flag == 1:
             print '%d'%(i),
     
if __name__ == '__main__':
     main()
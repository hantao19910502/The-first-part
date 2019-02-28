#!/usr/bin/env python
#_*_coding:utf-8_*_

def FOO():
    '''打印老狗
    '''
    Bar()
    print '我也是'    #ctrl 

def Bar():
    '''打印老狗
    '''
    print '我爱你'    #ctrl

if __name__ == '__main__':
    FOO()
else:
    print '滚吧'
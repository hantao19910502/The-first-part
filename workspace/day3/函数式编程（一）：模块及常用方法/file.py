#!/usr/bin/env python
#_*_coding:utf-8_*_
import sys,os

#打印相对路径和绝对路经 的方法
print __file__     #和sys.argv[0]相似都是相对路径
print sys.argv[0] 
print os.path.realpath(__file__)  #绝对路径（全路径）

#打印文件的描述的属性（描述对象的作用）
print __doc__

def foo():
    '测试'
    print '文件'
# print foo.__doc__   #打印出描述
foo()               #打印函数内容

#None
#测试
#文件

#!/usr/bin/env python
#_*_coding:utf-8_*_


'''
 ������20��
  ��Ŀ��һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룻�����£�������
 ��������10�����ʱ�������������ף���10�η�����ߣ�
'''
s = 100.
h = 50.0
for i in range(2,11):
     s += 2*h
     h /= 2
print "the sum length of path:%f"%s
print "the last height is:%f"%h
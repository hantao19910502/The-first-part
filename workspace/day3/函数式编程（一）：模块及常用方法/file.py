#!/usr/bin/env python
#_*_coding:utf-8_*_
import sys,os

#��ӡ���·���;���·�� �ķ���
print __file__     #��sys.argv[0]���ƶ������·��
print sys.argv[0] 
print os.path.realpath(__file__)  #����·����ȫ·����

#��ӡ�ļ������������ԣ�������������ã�
print __doc__

def foo():
    '����'
    print '�ļ�'
# print foo.__doc__   #��ӡ������
foo()               #��ӡ��������

#None
#����
#�ļ�

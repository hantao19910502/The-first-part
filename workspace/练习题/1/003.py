#!/usr/bin/env python
#_*_coding:utf-8_*_

#��Ŀ��һ��������������100����һ����ȫƽ�������ټ���168����һ����ȫƽ���������ʸ����Ƕ��٣�

import math
num = 1
while True:
    if math.sqrt(num + 100) - int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 168) - int(math.sqrt(num + 168)) == 0:
           print  num
           break
    num+=1
print    num          



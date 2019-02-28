#!/usr/bin/env python
#_*_coding:utf-8_*_


#输入某年某月某日，判断这一天是这一年的第几天？
import datetime
import time
dtstr = str(raw_input('Enter the datetime:(20151215):'))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr =dtstr[:4] +'0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print (int((dt-another_dt).days) + 1)


print datetime.datetime.now() 
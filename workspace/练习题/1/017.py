#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
  ��Ŀ������һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ���
'''

import string

def main():
    s = raw_input("Enter you want to input:")
    letter = 0
    space = 0
    digit = 0
    other = 0
    for h in s: 
        if h.isalpha():
            letter+=1
        elif h.isspace():
            space+=1
        elif h.isdigit():
            digit+=1
        else:
            other +=1
    print 'There are %d letters,%d spaces,%d digits and %d other characters in your string.'%(letter,space,digit,other)
 
if __name__ == '__main__':
       main()    
            
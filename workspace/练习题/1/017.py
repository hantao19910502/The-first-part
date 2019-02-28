#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
  题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
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
            
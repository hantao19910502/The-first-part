#!/usr/bin/env python
#_*_coding:utf-8_*_

from View import *
def Login():
    html = open('C:\Users\hantao\workspace\day11\View\login.html','r')
    html = html.read()
    return html
def Logout():
    return 'logout'
    
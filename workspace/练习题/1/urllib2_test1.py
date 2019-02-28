#!/usr/bin/env python
#_*_coding:utf-8_*_

import urllib2 
req = urllib2.Request('http://www.pythontab.com') 
response = urllib2.urlopen(req) 
the_page = response.read()
print the_page
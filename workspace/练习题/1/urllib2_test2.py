#!/usr/bin/env python
#_*_coding:utf-8_*_

import urllib 
import urllib2 
url = 'http://www.pythontab.com' 
values = {'name' : 'Michael Foord', 
          'location' : 'pythontab', 
          'language' : 'Python' } 
data = urllib.urlencode(values) 
req = urllib2.Request(url, data) 
response = urllib2.urlopen(req) 
print response
the_page = response.read()
print the_page
    
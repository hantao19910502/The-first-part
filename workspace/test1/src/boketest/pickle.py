#!/usr/bin/env python
#_*_coding:utf-8_*_

import pickle

data = {'k1':123,'k2':'hello'}

p_str = pickle.dumps(data)
print p_str

'''
import json
from _mysql import result

data = {'k1':123456,'k2':'hello'}
j_str = json.dumps(data)
print j_str

with open('C:/tmp/result.json','w') as fp:
        json.dump(data,fp)
'''
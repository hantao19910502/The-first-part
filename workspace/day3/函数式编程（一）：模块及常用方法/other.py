#!/usr/bin/env python
#_*_coding:utf-8_*_

from file import demo   #默认是导入一次，第二次导入的时候需要reload才行
from file import demo
reload(demo) 
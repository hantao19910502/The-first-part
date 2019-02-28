#!/usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=50)
    
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    user_type = models.ForeignKey('UserType')
class UserGroup(models.Model):
    GroupName = models.CharField(max_length=50)
    user = models.ManyToManyField('UserInfo')

class Asset(models.Model):
    hostname = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('UserGroup')
    def __unicode__(self):
        temp = u"当前Asset序列(%s,%s)"%(self.hostname,self.ip)
        return temp
    
    
    
    
    
    
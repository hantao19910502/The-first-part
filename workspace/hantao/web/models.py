#!/usr/bin/env python
#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=50)

class UserInfo(models.Model):
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Gender=models.BooleanField(default = False)
    Age=models.IntegerField(default=19)
    memo = models.TextField(default = 'xxxxxx')
    CreateDate=models.DateField(default= '2017-04-07')
    '''
    外键一对多
    '''
    typeId=models.ForeignKey('UserType')
class Group(models.Model):
    name = models.CharField(max_length=50)
class User(models.Model):
    '''
    外键多对多
    '''
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    group_relation=models.ManyToManyField('Group')
    
class Args(models.Model):
    '''
        字段可不可以为空
    '''
    name  = models.CharField(max_length=50,null=True)
    no_nmae = models.CharField(max_length=50,null=False)
    
class Asset(models.Model):
    hostname = models.CharField(max_length=50)
    '''
    自动更新创建时间
    '''
    create_date = models.DateField(auto_now_add=True)
    '''
    自动添加创建时间
    '''
    update_date = models.DateField(auto_now=True)

class Updata_1(models.Model): 
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
       
#!/usr/bin/env  python
#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.


class Host(models.Model):
    
    HostName = models.CharField(max_length=256)
    IP = models.GenericIPAddressField(max_length=1)
 
    class Meta:
        verbose_name = '用户名称'
        verbose_name_plural = 'IP列表'
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('HostName', 'IP')
    search_fields = ('HostName', 'IP')    
    list_filter = ('HostName', 'IP')
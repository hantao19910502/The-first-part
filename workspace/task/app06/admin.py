#!/usr/bin/env  python
#coding:utf-8


from django.contrib import admin

# Register your models here.

from app06.models import  Host,UserInfoAdmin
 

    
admin.site.register(Host,UserInfoAdmin)


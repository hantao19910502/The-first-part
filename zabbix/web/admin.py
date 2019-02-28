#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin

# Register your models here.

from  models import Asset,UserType,UserInfo,AssetAdmin,UserTypeAdmin,UserInfotAdmin



admin.site.register( Asset, AssetAdmin )
admin.site.register( UserType, UserTypeAdmin )
admin.site.register( UserInfo, UserInfotAdmin )

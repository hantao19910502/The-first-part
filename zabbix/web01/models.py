#!/usr/bin/env  python
#coding:utf-8
from django.db import models
from django.contrib import admin
# Create your models here.
class Asset(models.Model):
    filename = models.CharField(max_length=256)
    file_path = models.CharField(max_length=256)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = '文件名'
        verbose_name_plural = '文件路径'
class AssetAdmin(admin.ModelAdmin):
    list_display = ('filename', 'file_path')
    search_fields = ('filename', 'file_path')
    list_filter = ('filename', 'file_path')


class UserType(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = '用户类型'
class UserTypeAdmin(admin.ModelAdmin):
    list_display = (['name'])
    search_fields = (['name'])
    list_filter = (['name'])





class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    typeId = models.ForeignKey('UserType')
    class Meta:
        verbose_name = '用户名'
        verbose_name_plural = '密码'
class UserInfotAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username', 'password')
    list_filter = ('username', 'password')

#============================开服项目================================
class User(models.Model):
    username = models.CharField(max_length=30)

class GameProject(models.Model):
    proj_name = models.CharField(max_length=30)         #三国1、三国2、航海王
    codename = models.CharField(max_length=30)          #hhw 、sg2
    user =  models.ManyToManyField('User')
    iconimage = models.ImageField(upload_to='img')      #项目图片


class GamePlat(models.Model):
    gameproject = models.ForeignKey('GameProject')
    plat_name = models.CharField(max_length=30)         #安卓应用宝、安卓360、苹果应用宝、苹果360
    code_name = models.CharField(max_length=30)         #android_yyb、android_360、appstore_yyb、yyb
    basegroup_id = models.CharField(max_length=30)      #40001000、40002000


class GameInfo(models.Model):
    group = models.ForeignKey(GamePlat)                #hhw-android、sanguo-appstore
    server_name = models.CharField(max_length=30)       #白马将军、江东赴会
    server_id = models.CharField(max_length=30)         #23区
    serveropen_date = models.CharField(max_length=30)   #100000、110000
    serveropen_time = models.CharField(max_length=30)   #20170818、20170608
    is_recall = models.CharField(max_length=30)         #0、1

class gameproject_name(models.Model):
    gameproject_name = models.CharField(max_length=30)
    gameproject_name_chinese = models.CharField(max_length=100)

class gameplat_gameid(models.Model):
    gameplat_game_name = models.CharField(max_length=100)
    gameplat_game_id = models.CharField(max_length=100)

class plat_name_id(models.Model):
    gameplat_game_name = models.CharField(max_length=100)
    gameplat_game_name_chinese = models.CharField(max_length=100)

class ServerInfo(models.Model):
    gameid = models.CharField(max_length=30)            #basegroup_id+server_id 40001023
    server_data = {}
    status = models.CharField(max_length=30)            #0、1
    log    = models.TextField(max_length=30)
    last_time = models.DateField()


#!/usr/bin/env  python
#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from Tkinter import Image


class PlatGroup(models.Model):
    proj_name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    basegroup_id = models.IntegerField()
    image = models.ImageField(upload_to='img')
class YunYingInput(models.Model):
    server_name =  models.CharField(max_length=20)
    server_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    is_recall = models.TextField(default = '0')
    
    group = models.ForeignKey('Adapter')
    
class Adapter(models.Model):
    name =  models.CharField(max_length=20)
    group = models.CharField(max_length=20)

class GameInfo(models.Model):
    def __init__(self):
        GameInfo_basegroup = models.ForeignKey('PlatGroup')
        GameInfo_server_id = models.ForeignKey('YunYingInput')
    def save(self):
        gameid = self.GameInfo_basegroup.basegroup_id + self.GameInfo_server_id.server_id

    
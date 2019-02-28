#!/usr/bin/env  python
#coding:utf-8

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('姓名', max_length=64)
    age = models.SmallIntegerField('年龄')
    choices = (
        (1, '男'),
        (2, '女'),
        (3, '未知')
    )
    sex = models.SmallIntegerField('性别', choices=choices)
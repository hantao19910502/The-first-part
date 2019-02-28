from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    
class UserGroup(models.Model):
    GroupName = models.CharField(max_length=50)
    user = models.ManyToManyField('UserInfo')
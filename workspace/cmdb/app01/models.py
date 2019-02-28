from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Test(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Grouptask(models.Model):
    groupname = models.CharField(max_length=100)    
    groupbase = models.CharField(max_length=100)

class Host(models.Model):
    HostName = models.CharField(max_length=100)    
    host_group = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    
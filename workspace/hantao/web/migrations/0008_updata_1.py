# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_asset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updata_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.UserType'),
            preserve_default=False,
        ),
    ]
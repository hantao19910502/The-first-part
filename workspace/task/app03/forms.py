#!/usr/bin/env python
#_*_coding:utf-8_*_

from django import forms
from pip._vendor import ipaddress

class Alogin(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    date = forms.DateTimeField(required=True)
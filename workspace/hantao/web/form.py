#!/usr/bin/env python
#_*_coding:utf-8_*_


from django import forms
from pip._vendor.pkg_resources import require

class Alogin(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
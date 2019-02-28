#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

# Create your views here.


from app03 import forms

def index(request):
    
    obj = forms.Alogin()
    #global errorobj
    if request.method == 'POST':
        checkForm = forms.Alogin(request.POST)
        checkResult = checkForm.is_valid()
        if checkResult:
            return  HttpResponse("验证成功")
        else:
            print checkForm.errors
            errorobj=checkForm.errors
    return render_to_response('app03/index.html',{'data':obj,'error':errorobj})
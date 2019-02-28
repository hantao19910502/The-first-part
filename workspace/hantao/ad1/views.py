from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def login(request):
    return HttpResponse('login')
def logout(request):
    return HttpResponse('logout')
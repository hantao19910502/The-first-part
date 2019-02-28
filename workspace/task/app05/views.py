#!/usr/bin/env  python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from app05 import models
from django.utils.safestring import mark_safe
from app05 import html_help
def index(request,page):
    #操作数据库进行分页
    per_item = request.COOKIES.get('pager_num',10)
    per_item = int(per_item)
    try:
        page = int(page)
    except Exception,e:
        page = 1
    #每页显示几个
    #per_item = 30
    #总页数
    all_count= models.Host.objects.all().count()
    pageobj = html_help.perinfo(page,all_count,per_item)
    Count= models.Host.objects.all()[pageobj.start:pageobj.end].count()
    result = models.Host.objects.all()[pageobj.start:pageobj.end]
    all = divmod(all_count,per_item)
    all_page_count = pageobj.all_page
    page_string = html_help.Pager(page, all_page_count)
    
    
    ret = {'data':result,'count':Count,'page':page_string}
    
    response = render_to_response('app05/index.html',ret)
    response.set_cookie('pager_num',per_item)
    
    return response
    
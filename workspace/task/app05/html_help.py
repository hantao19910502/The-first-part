#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from app05 import models

class perinfo:
    def __init__(self,count_page,all_page_count,page_item):
        self.Count_page = count_page
        self.All_page_count = all_page_count
        self.Page_item = page_item
    @property
    def start(self):
        #start = (page - 1)*per_item
        return    (self.Count_page -1)* self.Page_item   
    @property
    def end(self):
        #end = page*per_item
        return self.Count_page*self.Page_item
    @property
    def all_page(self):
        '''
        all = divmod(count,per_item)
        if all[1] == 0:
            all_page_count = all[0]
        else:
            all_page_count = all[0] + 1
        '''
        all = divmod(self.All_page_count,self.Page_item)
        if all[1] == 0:
            all_page_count = all[0]
        else:
            all_page_count = all[0] + 1
        return all_page_count
    
    
    
    
def Pager(page,all_page_count):

    page_html = []
    
    first_page = '<a href="%d">首页</a>'%(1)
    page_html.append(first_page)
    if page <= 1:
        prev_page = '<a href="#">上一页</a>'
    else:
        prev_page = '<a href="%d">上一页</a>'%(page -1)
    #上一页
    #prev_page = '<a href="%d">上一页</a>'%(page -1)
    page_html.append(prev_page)
    begin = page -5
    end = page + 5
    if all_page_count <11:
        begin = 0
        end = all_page_count
    else:
        if page <6:
            begin=0
            end = 11
        else:
            if page +6 <all_page_count:
                begin=page -6
                end = page + 5
            else:
                begin = all_page_count - 11 
                end = all_page_count
    
    for h in range(begin,end): 
        #当前页
        if page == h + 1:
            a_html = '<a class="selected" href="%d">%d</a>'%(h+1,h+1)
        else:
            a_html = '<a  href="%d">%d</a>'%(h+1,h+1)
        page_html.append(a_html)
    #上一页    
    next_page = '<a href="%d">下一页</a>'%(page +1)
    page_html.append(next_page)
    
    end_page = '<a href="%d">尾页</a>'%(all_page_count)
    page_html.append(end_page)
    
    page = mark_safe(''.join(page_html))
    return page
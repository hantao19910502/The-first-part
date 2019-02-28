#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.shortcuts import render,render_to_response,redirect,HttpResponse

class RequestExeute(object):
     
    def process_request(self,request):
        print "1.process_request"
        #return HttpResponse('404')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print "1.process_view"
    def process_exception(self, request, exception):
        print '1.process_excepction'
     
    def process_response(self, request, response):
        print '1.process_response'
        return response
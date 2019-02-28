#!/usr/bin/env python
#_*_coding:utf-8_*_
from wsgiref.simple_server import make_server
from Controller.access import  *
from Controller.Admin import *
url = (
       ('/index/',Index),
       ('/manage/',Manage),
       ('/login/',Login),
       ('/logout/',Logout),
)

def RunServer(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    useURi = environ['PATH_INFO']
    func =None
    for item  in url:
        if item[0] == useURi:
            func = item[1]
            break
    if func:
        result = func()
    else:
        result= '404'
    return result


if __name__ == "__main__":
    httpd = make_server('',8000,RunServer)
    print "Servering HTTP on port 8000 ..."
    httpd.serve_forever()

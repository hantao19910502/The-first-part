
"""hantao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import index,Add,Delete,Update,Get,Updata_add,Updata_delete,Updata_updata,Updata_get,Assetlist,login,Alogins
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    #url(r'^list/(\w*)', list),    
    #url(r'^list/(?P<name>\d*)/$', list),
    #url(r'^list/(?P<name>\d*)/$', list,{'id':222}),
    url(r'^add/(?P<name>\w*)/$', Add),
    url(r'^delete/(?P<id>\w*)/$', Delete),
    url(r'^update/(?P<id>\w*)/(?P<hostname>\w*)/$', Update),
    url(r'^get/(?P<id>\w*)/$', Get),
    url(r'^updata1_add/(?P<name>\w*)/(?P<sex>\w*)/(?P<job>\w*)/$', Updata_add),
    url(r'^updata1_delete/(?P<id>\w*)/$', Updata_delete),
    url(r'^updata1_updata/(?P<id>\w*)/(?P<name>\w*)$', Updata_updata),
    url(r'^updata1_get/(?P<id>\w*)$', Updata_get),
    url(r'^assetlist/$', Assetlist),
    url(r'^login/$', login),
    url(r'^alogin/$', Alogins),
]

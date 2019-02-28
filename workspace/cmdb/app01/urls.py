#!/usr/bin/env python
#_*_coding:utf-8_*_
"""cmdb URL Configuration

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

from django.conf.urls import url ,include
from django.contrib import admin
from app01 import views
from app01 import models
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = ('url','UserName', 'Password')

# ViewSets define the view behavior.
class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = TestSerializer


# Serializers define the API representation.
class GrouptaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Grouptask
        fields = ('url','groupname', 'groupbase')

# ViewSets define the view behavior.
class GrouptaskViewSet(viewsets.ModelViewSet):
    queryset = models.Grouptask.objects.all()
    serializer_class = GrouptaskSerializer
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tests', TestViewSet)
router.register(r'Grouptasks', GrouptaskViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #单独定义一个api请求
    url(r'^addgroup/', views.addGroup),
    url(r'^addhost/', views.addHost),
    url(r'^', include(router.urls)),
    url(r'^index/', views.index),
]

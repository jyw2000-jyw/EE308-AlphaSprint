"""test_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^login/', views.get),
    path('users/insert', views.insertUsers, name="insertusers"), #执行用户信息添加
    url(r'get/', views.userInfo),
    url(r'commit/', views.commit),
    url(r'commt/', views.test),
    url(r'star/',views.youwantcommit),
    url(r'page/',views.pageget)
]

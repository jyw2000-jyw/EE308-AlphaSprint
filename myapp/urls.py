from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #url(r'^login/',views.LoginView.as_view()),
    path('users/', views.get, name="get"),
]


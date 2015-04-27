from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uname>[a-zA-z]+)/$', views.detail, name='detail'),
    url(r'^(?P<uname>[a-zA-z]+)/rating/$', views.rating, name='rating'),
]
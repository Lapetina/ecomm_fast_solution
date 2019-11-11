# coding=utf-8

from django.urls import path, re_path
from . import views

app_name = 'catalo'

urlpatterns = [
    #path(r'^$', views.product_list, name='product_list'),
    path('', views.product_list, name='product_list'),
    #path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path('^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    #path(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
    re_path('produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]

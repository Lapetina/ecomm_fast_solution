# coding=utf-8

from django.contrib import *

from catalog.models import Product, Category

#admin.site.register([Product, Category])
admin.site.register(Product)
admin.site.register(Category)

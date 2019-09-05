# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title':'Django E-Commerce'
    }
    return render(request, 'index.html', context)
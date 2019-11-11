"""ecomm_fast_solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
    #path(r'^produtos/$', views.product_list, name='product_list'),
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from catalog import views as catalog_views


urlpatterns = [
    path(r'', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls', namespace='catalo')),
    path('admin/', admin.site.urls),
]

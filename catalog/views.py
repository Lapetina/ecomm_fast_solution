from django.shortcuts import render

from .models import Product, Category
# Create your views here.


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    ca_tegory = Category.objects.get(slug=slug)
    context = {
        'current_category': ca_tegory,
        'product_list': Product.objects.filter(category=ca_tegory),
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

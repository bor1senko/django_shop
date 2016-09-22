from django.shortcuts import render
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Category, Product, BooleanProperty, StringProperty
from my_function import SortProperty


def home_page(request):
    category = Category.objects.all()
    content = list()
    for item in Category.objects.all():
        e = Product.objects.filter(category__exact=item)
        content.append([item, e])
    return render(request, 'task/home_page.html', {'content': content, 'category': category,})

def cart(request):
    return render(request, 'task/cart.html')

def product_view(request,option=None, product_id=1):
    category = Category.objects.all()
    product = Product.objects.get(id=product_id)
    if option == 'specif':
        fields = dict()
        fields =SortProperty(fields, BooleanProperty.objects.filter(product__exact=product))
        fields =SortProperty(fields, StringProperty.objects.filter(product__exact=product))
        a =dict()
        a[1] = 1
        a[2] = [1,2,3]
        a['1'] = [4,5,6]
        return render(request, 'task/view_product_s.html', {'a': a, 'product': product, 'category': category, 'fields': fields,})
    else:
        return render(request, 'task/view_product_c.html', {'product': product, 'category': category, })

def category_view(request):
    category = Category.objects.all()
    return render(request, 'task/view_category.html',  {'category': category,})


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
    content = Product.objects.filter(title__icontains=q)
    category = Category.objects.all()
    return render(request, 'task/search.html', {'q': q, 'content': content, 'category': category, })

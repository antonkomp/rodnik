from django.shortcuts import render
from django.db.models import F
from .models import PageView


def entrance_url(url):
    entrance = PageView.objects.filter(url=url)
    entrance.update(views=F('views') + 1)


def index(request):
    entrance_url('index')
    return render(request, 'index.html')


def product1(request):
    entrance_url('product1')
    return render(request, 'product1.html')


def product2(request):
    entrance_url('product2')
    return render(request, 'product2.html')


def product3(request):
    entrance_url('product3')
    return render(request, 'product3.html')


def product4(request):
    entrance_url('product4')
    return render(request, 'product4.html')


def product5(request):
    entrance_url('product5')
    return render(request, 'product5.html')


def product6(request):
    entrance_url('product6')
    return render(request, 'product6.html')


def product7(request):
    entrance_url('product7')
    return render(request, 'product7.html')


def product8(request):
    entrance_url('product8')
    return render(request, 'product8.html')


def product9(request):
    entrance_url('product9')
    return render(request, 'product9.html')


def product10(request):
    entrance_url('product10')
    return render(request, 'product10.html')

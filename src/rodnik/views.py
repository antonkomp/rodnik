from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def product1(request):
    return render(request, 'product1.html')


def product2(request):
    return render(request, 'product2.html')


def product3(request):
    return render(request, 'product3.html')


def product4(request):
    return render(request, 'product4.html')


def product5(request):
    return render(request, 'product5.html')


def product6(request):
    return render(request, 'product6.html')


def product7(request):
    return render(request, 'product7.html')


def product8(request):
    return render(request, 'product8.html')


def product9(request):
    return render(request, 'product9.html')


def product10(request):
    return render(request, 'product10.html')


def my_custom_page_not_found_view(request, exception, template_name='error404.html'):
    return render(request, template_name)


def my_custom_error_view(request, *args, **argv):
    return render(request, 'error500.html', status=500)

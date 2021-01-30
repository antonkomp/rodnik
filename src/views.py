from django.shortcuts import render
from django.db.models import F
from rodnik.models import PageView


def entrance_url(url):
    entrance = PageView.objects.filter(url=url)
    entrance.update(views=F('views') + 1)


def my_custom_page_not_found_view(request, exception, template_name='error404.html'):
    entrance_url('error')
    return render(request, template_name)


def my_custom_error_view(request, *args, **argv):
    return render(request, 'error500.html', status=500)

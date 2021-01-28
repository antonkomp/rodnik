from django.shortcuts import render


def my_custom_page_not_found_view(request, exception, template_name='error404.html'):
    return render(request, template_name)


def my_custom_error_view(request, *args, **argv):
    return render(request, 'error500.html', status=500)

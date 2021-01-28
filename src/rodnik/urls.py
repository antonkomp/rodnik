from django.urls import path

from .views import index, product1, product2, product3, product4, product5, product6,\
                    product7, product8, product9, product10

urlpatterns = [
    path('', index, name='index'),
    path('product1/', product1, name='product1'),
    path('product2/', product2, name='product2'),
    path('product3/', product3, name='product3'),
    path('product4/', product4, name='product4'),
    path('product5/', product5, name='product5'),
    path('product6/', product6, name='product6'),
    path('product7/', product7, name='product7'),
    path('product8/', product8, name='product8'),
    path('product9/', product9, name='product9'),
    path('product10/', product10, name='product10'),
]

from django.urls import path

from catalog.views import contacts, home, products, add_product

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<pk>/', products, name='products'),
    path('add_product/', add_product, name='add_product')
]

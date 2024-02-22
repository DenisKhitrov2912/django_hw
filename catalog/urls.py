from django.urls import path

from catalog.views import contacts, home, products, add_product, product_list

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', products, name='products'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list')
]

from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import ContactTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductsListView, \
    BlogWritingCreateView, BlogWritingDetailView, BlogWritingListView, BlogWritingUpdateView, BlogWritingDeleteView, \
    ProductUpdateView, category_list_view

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products'),
    path('products/edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_edit'),
    path('add_product/', never_cache(ProductCreateView.as_view()), name='add_product'),
    path('products_list/', ProductsListView.as_view(), name='product_list'),
    path('blogwrite/', never_cache(BlogWritingCreateView.as_view()), name='blogwrite'),
    path('blogwrite/<int:pk>', BlogWritingDetailView.as_view(), name='blogwrite_read'),
    path('blogwrite/readall', BlogWritingListView.as_view(), name='blogwrite_readall'),
    path('blogwrite/edit/<int:pk>', never_cache(BlogWritingUpdateView.as_view()), name='blogwrite_edit'),
    path('blogwrite/delete/<int:pk>', never_cache(BlogWritingDeleteView.as_view()), name='blogwrite_delete'),
    path('categories/', category_list_view, name='categories'),
]

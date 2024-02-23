from django.urls import path

from catalog.views import ContactTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductsListView, \
    BlogWritingCreateView, BlogWritingDetailView, BlogWritingListView, BlogWritingUpdateView, BlogWritingDeleteView, \
    ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('products_list/', ProductsListView.as_view(), name='product_list'),
    path('blogwrite/', BlogWritingCreateView.as_view(), name='blogwrite'),
    path('blogwrite/<int:pk>', BlogWritingDetailView.as_view(), name='blogwrite_read'),
    path('blogwrite/readall', BlogWritingListView.as_view(), name='blogwrite_readall'),
    path('blogwrite/edit/<int:pk>', BlogWritingUpdateView.as_view(), name='blogwrite_edit'),
    path('blogwrite/delete/<int:pk>', BlogWritingDeleteView.as_view(), name='blogwrite_delete')
]

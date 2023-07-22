
from django.urls import path

from .apps import CatalogConfig
from .views import (
    ContactsView,
    ProductListView,
    HomeView, CategoryListView, ProductByCategoryView, ProductDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/', ProductByCategoryView.as_view(), name='product_by_category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]


from django.urls import path

from .apps import CatalogConfig
from .views import (
    ContactsView,
    ProductListView,
    HomeView, CategoryListView, ProductByCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/<int:pk>/', ProductByCategoryView.as_view(), name='product_by_category'),
]

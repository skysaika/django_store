
from django.urls import path

from .apps import CatalogConfig
from .views import (
    ContactsView,
    ProductListView,
    HomeView, CategoryListView, ProductByCategoryView, ProductDetailView, ProductCreateView, ProductUpdateView,
    ProductDeleteView, toggle_activity
)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/', ProductByCategoryView.as_view(), name='product_by_category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]

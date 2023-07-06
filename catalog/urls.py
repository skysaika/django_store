from django.urls import path

from .apps import CatalogConfig
from .views import home, contacts, product_list

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts')
]

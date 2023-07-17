
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('create', BlogPostCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>', ..., name='view'),
    # path('edit/<int:pk>', ..., name='update'),
    # path('delete/<int:pk>', ..., name='delete'),
]

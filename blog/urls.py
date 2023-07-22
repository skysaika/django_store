
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),  # создание поста в blogpost_form
    path('', BlogPostListView.as_view(), name='list'),  # список постов в blogpost_list
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='view'),  # детали одной поста в blogpost_detail
    path('edit/<int:pk>', BlogPostUpdateView.as_view(), name='edit'),  # редактирование поста
    path('delete/<int:pk>', BlogPostDeleteView.as_view(), name='delete'),  # подтверждение и удаление
]

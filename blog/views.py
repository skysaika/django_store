from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published', 'view_count']
    success_url = reverse_lazy('blogpost_list')

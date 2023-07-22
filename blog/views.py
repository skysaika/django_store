from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    """Контроллер создания поста"""
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published', 'view_count']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Метод для формы валидности присваивает слаг"""
        if form.is_valid():
            new_blogpost = form.save()
            new_blogpost.slug = slugify(new_blogpost.title)
            new_blogpost.save()

        return super().form_valid(form)


class BlogPostListView(ListView):
    """Контроллер списка постов"""
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        """Метод для выведения только опубликованных постов"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    """Контроллер карточки одного поста"""
    model = BlogPost

    def get_object(self, queryset=None):
        """Метод для увеличения просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published', 'view_count',]
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Метод для формы валидности присваивает слаг"""
        if form.is_valid():
            new_blogpost = form.save()
            new_blogpost.slug = slugify(new_blogpost.title)
            new_blogpost.save()

        return super().form_valid(form)
    def get_success_url(self):
        """Метод для пользователя на просмотр этой статьи после ред-ния"""
        return reverse('blog:view', args={self.kwargs.get('pk')})


class BlogPostDeleteView(DeleteView):
    """Контроллер удаления поста"""
    model = BlogPost
    success_url = reverse_lazy('blog:list')


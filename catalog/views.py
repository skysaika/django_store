from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Product, Category


class HomeView(TemplateView):
    """Контроллер домашней страницы, показывает 3 случайных товара"""
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_objects = Product.objects.filter(in_stock=True).order_by('?')[:3] # 3 товара в наличии в случ.порядке
        context['object_list'] = product_objects
        context['title'] = 'Главная'
        return context

class CategoryListView(ListView):
    """Контроллер страницы со списком категорий"""
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        """Метод возвращает все категории"""
        queryset = Category.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список всех категорий'
        return context


class ProductListView(ListView):
    """Контроллер страницы со всеми товарами"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 10 # на странице 10 товаров

    def get_queryset(self):
        """Метод фильтрует товары по категориям"""
        category = self.request.GET.get('category', None)
        if category:
            queryset = Product.objects.filter(category__title__icontains=category)
        else:
            queryset = Product.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context

class ProductByCategoryView(ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Product.objects.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        context['title'] = f'Товары категории {category.title}'
        return context

class ContactsView(TemplateView):
    """Контроллер для контактов и обратной связи"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        if self.request.method == 'POST':
            context.update(self.request.POST.dict())
        return context

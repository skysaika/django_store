from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Product, Category, Version


class HomeView(TemplateView):
    """Контроллер домашней страницы"""
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_objects = Product.objects.filter(in_stock=True).order_by('?')[:3] # 3 товара в наличии в случ.порядке
        context_data['object_list'] = product_objects
        context_data['title'] = 'Главная'
        return context_data

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
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список всех категорий'
        return context_data


class ProductListView(ListView):
    """Контроллер страницы со всеми товарами"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 10 # если больше 10 товаров на странице, переход на новую

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        if category:
            queryset = Product.objects.filter(category__title__icontains=category)
        else:
            queryset = Product.objects.all()
        return queryset


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Вся продукция'
        return context_data

class ProductByCategoryView(ListView):
    """Товары по категориям"""
    template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        """Метод фильтрует товары по категориям"""
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Product.objects.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        context_data['title'] = f'Товары категории {category.title}'
        context_data['category_id'] = category.id  # add category_id to template's context
        return context_data

# ljltkfnm
class VersionListView(ListView):
    """Контроллер версий продукта"""
    model = Version
    extra_context = {
        'title': 'Список активных версий',
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только активные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active_version=True)
        return queryset



class ContactsView(TemplateView):
    """Контроллер для контактов и обратной связи"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Контакты'
        if self.request.method == 'POST':
            context_data.update(self.request.POST.dict())
        return context_data

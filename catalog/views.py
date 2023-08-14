from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm
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
    # template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 10 # если больше 10 товаров на странице, переход на новую

    def get_queryset(self):
        """Метод фильтрует объекты Product по полю category, независимо от регистра символов"""
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
        """
            Получает контекстные данные для шаблона.

            :param kwargs: дополнительные параметры контекста
            :return: словарь контекстных данных
        """
        context_data = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        context_data['title'] = f'Товары категории {category.title}'
        context_data['category_id'] = category.id  # add category_id to template's context
        return context_data


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


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'catalog/product_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context_data['pk'] = pk

        return context_data


class ProductCreateView(CreateView):
    """Контроллер формы создания продукта"""
    model = Product
    form_class = ProductForm  # форм класс
    # fields = ['title', 'description', 'image', 'category', 'price', 'in_stock']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """Контроллер формы редактирования продукта"""
    model = Product
    form_class = ProductForm
    # fields = ['title', 'description', 'image', 'category', 'price', 'in_stock']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    """Контроллер удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:category_list')


def toggle_activity(request, pk):
    """Контроллер смены статуса продукта в наличии/не в наличии"""
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.in_stock:
        product_item.in_stock = False
    else:
        product_item.in_stock = True

    product_item.save()

    return redirect(reverse('catalog:product_list'))

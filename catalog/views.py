from django.shortcuts import render

from catalog.models import Product, Category


def base(request):
    context = {}
    return render(request, 'catalog/base.html', context)


def home(request):
    template = 'catalog/home.html'
    product_objects = Product.objects.filter(in_stock=True)[:3]
    context = {
        'object_list': product_objects,
        'title':'Главная'
    }
    return render(request, template, context)

def product_list(request):
    template = 'catalog/product_list.html'
    product_objects = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'object_list': product_objects,
        'title':'Категории',
        'categories': categories
    }
    return render(request, template, context)


def contacts(request):
    template = 'catalog/contacts.html'
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        context.update(request.POST.dict())
    return render(request, template, context)

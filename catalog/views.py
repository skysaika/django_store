from django.shortcuts import render

from catalog.models import Product, Category


def base(request):
    context = {}
    return render(request, 'catalog/base.html', context)



def home(request):
    template = 'catalog/home.html'
    product_objects = Product.objects.filter(in_stock=True).order_by('?')[:3]
    context = {
        'object_list': product_objects,
        'title':'Главная'
    }
    return render(request, template, context)


def product_list(request):
    template = 'catalog/product_list.html'
    product_objects = Product.objects.all()
    context = {
        'object_list': product_objects,
        'title':'Каталог',
    }
    return render(request, template, context)

def category_tablets(request, pk):
    category_item = Category.objects.get(pk=pk)
    product_objects = Product.objects.filter(category_id=pk)
    context = {
        'object_list': product_objects,
        'title': f'Планшеты: {category_item.name} )',
    }
    return render(request, 'catalog/tablets.html', context)



def contacts(request):
    template = 'catalog/contacts.html'
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        context.update(request.POST.dict())
    return render(request, template, context)

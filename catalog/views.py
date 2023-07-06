from django.shortcuts import render

from catalog.models import Product

def base(request):
    product_list = Product.objects.all()
    context = {
            'object_list': product_list
    }
    return render(request, 'catalog/base.html', context)



def home(request):
    template = 'catalog/home.html'
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, template, context)

def about(request):
    template = 'catalog/about.html'
    return render(request, template, {})

def contacts(request):
    template = 'catalog/contacts.html'
    context = {}
    if request.method == 'POST':
        context.update(request.POST.dict())
    return render(request, template, context)

from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания продукта"""
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'category', 'price', 'in_stock']

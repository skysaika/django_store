from django import forms

from catalog.models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования продукта"""
    # version = forms.ModelChoiceField(queryset=Version.objects.all(), label='Версия продукта')
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'category', 'price', 'in_stock',]

    def clean_title(self):
        """Проверяет название продукта на наличие запрещенных слов.
        Если в названии запрещенное слово -> forms.ValidationError
        """
        title = self.cleaned_data['title']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in title.lower():
                raise forms.ValidationError("Нельзя добавлять запрещенные слова в название продукта.")
        return title

    def clean_description(self):
        """
        Проверяет описание продукта на наличие запрещенных слов.
        Если в описании запрещенное слово -> forms.ValidationError
        """
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError("Нельзя добавлять запрещенные слова в описание продукта.")
        return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

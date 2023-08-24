from autoslug import AutoSlugField
from django.conf import settings
from django.db import models



from catalog.models.category import Category

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    in_stock = models.BooleanField(default=True, verbose_name='в наличии')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f"Название: {self.title}. \n" \
               f"Категория: {self.category}. \n" \
               f"Описание: {self.description}. \n" \
               f"Цена: {self.price}. \n" \


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)

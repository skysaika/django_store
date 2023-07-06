from autoslug import AutoSlugField
from django.db import models

from catalog.models.category import Category

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):

    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    in_stock = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        return f"Name: {self.title}. \n" \
               f"Category: {self.category}. \n" \
               f"Description: {self.description}. \n" \
               f"Price: {self.price}. "

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)

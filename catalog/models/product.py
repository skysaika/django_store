from autoslug import AutoSlugField
from django.db import models

from catalog.models.category import Category

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):

    title = models.CharField(max_length=200, verbose_name='наименование')
    # slug = AutoSlugField(populate_from='title', unique=True, max_length=255, verbose_name='URL')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f"Наименование товара: {self.title}. " \
               f"Категория: {self.category}. " \
               f"Цена: {self.price}. " \
               f"Дата создания: {self.created_date}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)

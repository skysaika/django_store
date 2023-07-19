from django.db import models
from slugify import slugify

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)
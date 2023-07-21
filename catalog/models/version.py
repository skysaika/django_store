from django.db import models

from catalog.models import Product

NULLABLE = {'blank': True, 'null': True}

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_active_version = models.BooleanField(default=False, verbose_name='активный')

    def __str__(self):
        return f'{self.product} {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('number',)
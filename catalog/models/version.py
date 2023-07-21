from django.db import models

from catalog.models import Product

NULLABLE = {'blank': True, 'null': True}

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active_version = models.BooleanField(default=False, verbose_name='активный')

    def __str__(self):
        return f'{self.product} {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_name',)
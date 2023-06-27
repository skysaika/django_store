from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

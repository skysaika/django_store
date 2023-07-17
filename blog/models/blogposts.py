from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog', verbose_name='Превью', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f"Заголовок: {self.title}"


    class Meta:
        verbose_name = 'статья блога'
        verbose_name_plural = 'статьи блога'
        ordering = ['-created']


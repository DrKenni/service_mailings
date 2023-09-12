from django.db import models

from users.models import NULLABLE


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE,)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='превью')
    creation_date = models.DateField(auto_now=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

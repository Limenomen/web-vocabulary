from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Содержание', blank=True)
    tag = models.ManyToManyField('core.Tag', verbose_name='Связанные теги', blank=True, related_name='articles')
    author = models.ForeignKey(User, verbose_name='Автор', blank=True, null=True, on_delete=models.SET_NULL)
    media = models.FileField('Файл', blank=True, null=True, upload_to='media')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Tag(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


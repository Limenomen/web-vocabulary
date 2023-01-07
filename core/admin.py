from django.contrib import admin
from core import models


@admin.register(models.Article)
class Article(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'tag')


@admin.register(models.Tag)
class Article(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render

from core import models


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ArticleList(ListView):
    queryset = models.Article.objects.order_by('name')


class ArticleDetail(DetailView):
    model = models.Article

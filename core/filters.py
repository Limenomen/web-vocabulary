import django_filters
from django_filters import FilterSet
from core import models


class ArticleFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    tag = django_filters.ModelMultipleChoiceFilter(queryset=models.Tag.objects.all())

    class Meta:
        model = models.Article
        fields = ('name', 'tag')

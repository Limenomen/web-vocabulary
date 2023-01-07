from django.views.generic import TemplateView, ListView, DetailView, View

from core import models, forms, filters


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ArticleList(ListView):
    queryset = models.Article.objects.order_by('name')

    def get_filters(self):
        return filters.ArticleFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = forms.ArticleSearch
        return context


class ArticleDetail(DetailView):
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article: models.Article = self.get_object()
        context['tags'] = article.tag.all()
        return context

from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = models.Article
    form_class = forms.ArticleCreate

    def form_valid(self, form):
        result = super().form_valid(form)

        # добавим автора статьи
        self.object.author = self.request.user
        self.object.save(update_fields=['author'])

        # если было прикреплено изображение, то создадим объект
        if media := form.cleaned_data.get('media'):
            models.Media.objects.create(file=media, name=self.object.name, article=self.object)

        return result

    def get_success_url(self):
        return reverse('core:article-list')


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = models.Article
    form_class = forms.Article

    def get_success_url(self):
        return reverse('core:article-detail', kwargs={'pk': self.object.pk})
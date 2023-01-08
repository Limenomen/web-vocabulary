from django import forms
from core import models


class ArticleSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    tag = forms.ModelMultipleChoiceField(label='теги', queryset=models.Tag.objects.all(), required=False)


class Article(forms.ModelForm):

    class Meta:
        model = models.Article
        exclude = ['author', 'tag']


class ArticleCreate(Article):
    media = forms.ImageField(label='Изображение', required=False)


class MediaCreate(forms.ModelForm):

    class Meta:
        model = models.Media
        exclude = ['article']


class TagCreate(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = '__all__'

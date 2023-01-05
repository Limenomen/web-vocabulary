from django import forms
from core import models


class ArticleSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    tag = forms.ModelMultipleChoiceField(label='теги', queryset=models.Tag.objects.all(), required=False)

from django import forms
from django.forms import inlineformset_factory

from .models import Quotes, QuoteSources


class QuoteSourcesForm(forms.ModelForm):
    """ Экземпляр формы для модели Источников """
    class Meta:
        model = QuoteSources
        fields = ['name', 'type', 'author']

class QuotesForm(forms.ModelForm):
    """ Экземпляр формы для модели Цитат """
    class Meta:
        model = Quotes
        fields = ['quote', 'weight', 'source']

SourceFormSet = inlineformset_factory(
    QuoteSources,  # Родительская модель (напрямую не связана с тем, что мы хотим)
    Quotes, # Дочерняя модель
    fields=('name', 'type', 'author'),
    extra=1,  # Показывает 1 пустую форму
    can_delete=False
)
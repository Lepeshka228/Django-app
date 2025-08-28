from django import forms
from django.forms import inlineformset_factory

from .models import Quote


class QuoteForm(forms.ModelForm):
    """ Форма для заполнения табл quotes """
    class Meta:
        model = Quote
        fields = ['quote', 'weight', 'source', 'type', 'author']

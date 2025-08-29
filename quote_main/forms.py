from django import forms
from django.forms import inlineformset_factory

from .models import Quote


class QuoteForm(forms.ModelForm):
    """ Форма для заполнения табл quotes """
    class Meta:
        model = Quote
        fields = ['quote', 'weight', 'source', 'type', 'author']
        widgets = {
            'quote': forms.Textarea(attrs = {"class": "form-control", 'placeholder': 'Цитата...'}),
            'source': forms.TextInput(attrs = {"class": "form-control", 'placeholder': 'Источник...'}),
            'weight': forms.Select(attrs = {"class": "form-control", 'placeholder': 'Ваша оценка...'}),
            'author': forms.TextInput(attrs = {"class": "form-control", 'placeholder': 'Автор...'}),
            'type': forms.Select(attrs = {"class": "form-control", 'placeholder': 'Тип...'})
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

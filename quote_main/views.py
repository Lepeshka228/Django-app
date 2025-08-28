from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from django.forms import formset_factory

from quote_main.models import Quotes, QuoteSources

from quote_main.forms import QuotesForm, SourceFormSet

import random

SESSION_KEY = 'voted_quotes'

def index(request):
    """
    Вьюшка главной страницы, здесь выводим случайную цитату(взвешенную)
    Так-же возможность добавлять свою цитату
    """

    random_quote = random_quote_func(Quotes)

    quote_form = QuotesForm
    quote_source = QuoteSources
    inline_form = SourceFormSet

    context: dict[str, str] = {
        'title': 'Цитатник',
        'quote': random_quote,
        'quote_form': quote_form,
        'quote_source': quote_source,
        'form': inline_form
    }

    return render(request, 'main/index.html', context)


def top_ten(request):
    """ Вьюшка страницы с топ-10 цитат - сортировка по лайкам, дизлайкам, просмотрам """
    quotes = Quotes.objects.all()

    context: dict[str, str] = {
        'title': 'Топ 10 цитат',
        'quotes': quotes
    }

    return render(request, 'main/top_ten.html', context)


def random_quote_func(model):
    # все объекты из БД
    all_quotes = model.objects.all()

    # Взвешенный список объектов
    weighted_list_of_quotes = []
    for quote in all_quotes:
        weighted_list_of_quotes.extend([quote] * quote.weight)
    
    # Случайный объект из взвешенного списка
    if weighted_list_of_quotes:
        random_quote = random.choice(weighted_list_of_quotes)
    else:
        random_quote = None    # если список пустой по каким-то причинам
    return random_quote


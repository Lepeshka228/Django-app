from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from quote_main.models import Quote

from quote_main.forms import QuoteForm

import random

SESSION_KEY = 'voted_quotes'

def index(request):
    """
    Вьюшка главной страницы, здесь выводим случайную цитату(взвешенную)
    Так-же возможность добавлять свою цитату
    """
    
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.full_clean()
            obj.save()
            messages.success(request, 'Цитата добавлена!')
            return redirect('main/index.html')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = QuoteForm()

        random_quote = random_quote_func(Quote)

        context = {
            'title': 'Цитатник',
            'quote': random_quote,
            'form': form
        }

        return render(request, 'main/index.html', context)


def top_ten(request):
    """ Вьюшка страницы с топ-10 цитат - сортировка по лайкам, дизлайкам, просмотрам """
    quotes = Quote.objects.all()

    context = {
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


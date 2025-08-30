import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from quote_main.models import Quote

from quote_main.forms import QuoteForm

from .services import random_quote_func



def index(request):
    """
    Вьюшка главной страницы, здесь выводим случайную цитату(взвешенную)
    Так-же возможность добавлять свою цитату
    """
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Цитата добавлена!')
            return redirect('quote_main:index')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = QuoteForm()

    # получаем случайную цитату
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

from django.http import HttpResponse
from django.shortcuts import render

from quote_main.models import Quotes


def index(request):

    # получаю случайную цитату
    quote = Quotes.objects.select_related('source').order_by('?').first()

    context: dict[str, str] = {
        'title': 'Цитатник',
        'quote': quote
    }

    return render(request, 'main/index.html', context)

def top_ten(request):

    quotes = Quotes.objects.all()

    context: dict[str, str] = {
        'title': 'Топ 10 цитат',
        'quotes': quotes
    }

    return render(request, 'main/top_ten.html', context)
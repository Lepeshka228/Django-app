import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def random_quote_func(model):
    """ Выводит случайную цитату quote из модели с учетом веса weight """

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

def get_client_ip(request):
    """ Получает ip пользователя из запроса """

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


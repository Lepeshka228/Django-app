import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from quote_main.models import Quote, LikeDislike

from quote_main.forms import QuoteForm

from .services import random_quote_func, get_client_ip



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
    """ Вьюшка страницы с топ-10 цитат - сортировка по лайкам """
    top_ten_quotes = Quote.objects.order_by("-likes")[:10]

    context = {
        'title': 'Топ 10 цитат',
        'quotes': top_ten_quotes
    }

    return render(request, 'main/top_ten.html', context)

@require_POST
def like_dislike_proc(request):
    """ Обрабатывает лайк и дизлайк """
    quote_id = request.POST.get('quote_id')
    vote_type = request.POST.get('vote_type')
    
    quote = get_object_or_404(Quote, id=quote_id)
    client_ip = get_client_ip(request)

    try:
        vote, created = LikeDislike.objects.get_or_create(
            quote=quote,
            client_ip=client_ip,
            defaults={'vote_type': vote_type}
        )
        if created:
            if vote_type == 'like':
                quote.likes += 1
            elif vote_type == 'dislike':
                quote.dislikes += 1
            quote.save()
            
            # Возвращаем обновленные счетчики
            return JsonResponse({
                'status': 'success',
                'message': 'Голос зафиксирован.',
                'likes': quote.likes,
                'dislikes': quote.dislikes
            })
        else:
            return JsonResponse({'status': 'error', 'message': 'Пользователь уже голосовал.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'Ошибка.'})

from django.http import HttpResponse
from django.shortcuts import render

# переменная request хранит в себе все данные запроса 
# httpresponse возвращает все данные ответа 
def index(request):

    context: dict[str, str] = {
        'title': 'Цитатник',
        'name_of_quote': 'Это великая цитата великого философа, которая навсегда останется в наших умах',
        'count_of_views': 2,
        'type_of_source': 'Книга',
        'name_of_source': 'Государство',
        'author_of_source': 'Платон'
    }

    return render(request, 'main/index.html', context)

def top_ten(request):

    context: dict[str, str] = {
        'title': 'Топ 10 цитат',
    }

    return render(request, 'main/top_ten.html', context)
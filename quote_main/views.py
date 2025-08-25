from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# переменная request хранит в себе все данные запроса 
# httpresponse возвращает все данные ответа 
def index(request):

    context: dict[str, str] = {
        'title': 'Цитатник',
        'content': 'Здесь будет показываться цитата'
    }

    return render(request, 'main/base.html', context)

def top_ten(request):
    return HttpResponse('top_ten')
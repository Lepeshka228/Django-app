from django.urls import path

from quote_main import views

app_name = 'quote_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('top_ten/', views.top_ten, name='top_ten'),
    path('vote/', views.like_dislike_proc, name='like_dislike_proc')
]

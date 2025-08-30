from django.core.exceptions import ValidationError
from django.db import models


class Quote(models.Model):
    """ Модель единственной и главной таблицы - содержит и цитаты и источник в одном """

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    quote = models.TextField(unique=True, verbose_name='Цитата')
    weight = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Вес', default=3)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    source = models.CharField(max_length=100, verbose_name='Название источника')
    TYPE_CHOICE = [
        ('film', 'Фильм'),
        ('book', 'Книга'),
        ('song', 'Песня'),
        ('serial', 'Сериал'),
        ('life', "Из жизни")
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, verbose_name='Тип')
    author = models.CharField(max_length=100, verbose_name='Автор', blank=True)
    
    def __str__(self):
        return f'{self.quote[:20]} - {self.source}, {self.author}'
    
    def clean(self):
        # уберём лишние пробелы сначала и конца
        if self.quote:
            self.quote = self.quote.strip()
        if self.source:
            self.source = self.source.strip()

        list_of_quote_obj = Quote.objects.filter(quote__iexact=self.quote)  # вернет все элементы с данной цитатой
        list_of_source_obj = Quote.objects.filter(source__iexact=self.source)    # вернет все элементы с данным источником

        if self.pk:
            list_of_quote_obj = list_of_quote_obj.exclude(pk=self.pk)
            list_of_source_obj = list_of_source_obj.exclude(pk=self.pk)

        if list_of_quote_obj.exists():
            raise ValidationError({'quote': 'Такая цитата уже существует.' })
        if list_of_source_obj.count() >= 3:
            raise ValidationError({'source': 'У этого источника уже есть 3 цитаты. Придётся выбрать другой'})

class LikeDislike(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    client_ip = models.CharField(max_length=100)
    TYPE_CHOICE = [
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('none', 'none')
    ]
    vote_type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    class Meta:
        unique_together = ('quote', 'client_ip')
        db_table = 'likes_dislikes'
    def __str__(self):
        return f'{self.client_ip} проголосовал в {self.quote}'


from django.db import models

class QuoteSources(models.Model):
    """ Модель источника цитаты - название, тип, автор """

    TYPE_CHOICE = [
        ('film', 'Фильм'),
        ('book', 'Книга'),
        ('song', 'Песня'),
        ('serial', 'Сериал')
    ]
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, verbose_name='Тип')
    author = models.CharField(max_length=100, verbose_name='Автор', blank=True)

    class Meta:
        db_table = 'sources'
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

    def __str__(self):
        return f"{self.name} ({self.author})"


class Quotes(models.Model):
    """ Модель цитаты - цитата, вес, лайки, дизлайки, просмотры, источник(внеш.кл.)"""

    WEIGHT_CHOICE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    quote = models.TextField(unique=True, verbose_name='Цитата')
    weight = models.IntegerField(choices=WEIGHT_CHOICE, verbose_name='Вес', default=3)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    source = models.ForeignKey(QuoteSources, on_delete=models.CASCADE, verbose_name='Источник')

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Цитату'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.quote


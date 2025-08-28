from django.db import models


class Quote(models.Model):
    """ Модель единственной и главной таблицы - содержит и цитаты и источник в одном """

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Цитату'
        verbose_name_plural = 'Цитаты'

    quote = models.TextField(unique=True, verbose_name='Цитата')
    weight = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Вес', default=3)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    name = models.CharField(max_length=100, verbose_name='Название источника')
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
        return f'{self.quote[:20]} - {self.author}'
    
    def clean(self):
        pass

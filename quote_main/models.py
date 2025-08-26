from django.db import models

class QuoteSources(models.Model):
    """ Модель источника цитаты - название, тип, автор """

    # типы источников
    TYPE_CHOICE = (
        ('film', 'Фильм'),
        ('book', 'Книга'),
        ('song', 'Песня')
    )
    # название источника
    name = models.CharField(max_length=100)
    # тип источника
    type = models.CharField(max_length=20, 
                            choices=TYPE_CHOICE)
    # автор источника
    author = models.CharField(max_length=100)

    class Meta:
        db_table = 'sources'

    def __str__(self):
        return self.name


class Quotes(models.Model):
    """ Модель цитаты - цитата, вес, лайки, дизлайки, просмотры, источник(внеш.кл.)"""

    WEIGHT_CHOICE = (1, 2, 3, 4, 5)

    quote = models.TextField(unique=True)
    weight = models.IntegerField(choices=WEIGHT_CHOICE)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    views = models.IntegerField()
    source = models.ForeignKey(to='QuoteSources', verbose_name='Источник')

    class Meta:
        db_table = 'quotes'




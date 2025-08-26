from django.db import models

class QuoteSources(models.Model):
    """ Модель источника цитаты - название, тип, автор """

    # типы источников
    TYPE_CHOICE = [
        ('film', 'Фильм'),
        ('book', 'Книга'),
        ('song', 'Песня')
    ]
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

    # WEIGHT_CHOICE = (1, 2, 3, 4, 5)

    quote = models.TextField(unique=True)
    weight = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    views = models.IntegerField()
    source = models.ForeignKey(QuoteSources, on_delete=models.CASCADE)

    class Meta:
        db_table = 'quotes'

    def __str__(self):
        return self.quote


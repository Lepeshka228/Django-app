from django.apps import AppConfig


class QuoteMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quote_main'
    verbose_name = 'Показ цитаты'    # для корректного отображения в админке
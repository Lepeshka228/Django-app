from django.contrib import admin

from quote_main.models import Quotes, QuoteSources

# admin.site.register(Quotes)
# admin.site.register(QuoteSources)

@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote', 'weight', 'source']
    fields = ['quote', 'weight', 'source']

@admin.register(QuoteSources)
class QuoteSourcesAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'author']
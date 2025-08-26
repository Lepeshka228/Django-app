from django.contrib import admin

from quote_main.models import Quotes, QuoteSources

# admin.site.register(Quotes)
# admin.site.register(QuoteSources)

class SourcesInline(admin.StackedInline):
    model = QuoteSources
    extra = 2    # кол-во пустых форм для добавления


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    fields = ['quote', 'weight', 'source', 'author']
    inlines = [SourcesInline]

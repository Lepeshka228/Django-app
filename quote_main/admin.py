from django.contrib import admin

from quote_main.models import Quote

# admin.site.register(Quotes)
# admin.site.register(QuoteSources)

@admin.register(Quote)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote', 'weight', 'source', 'type', 'author']
    fields = ['quote', 'weight', 'source', 'type', 'author']

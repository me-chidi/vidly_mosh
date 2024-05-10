from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Checkout
# Register your models here.

class DurationFilter(admin.SimpleListFilter):
    title = 'duration'
    parameter_name = 'duration'

    def lookups(self, request, model_admin):
        return [
            ('<30', 'less than 30days'),
            ('<60', 'less than 60days'),
            ('<90', 'less than 90days'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<30':
            return queryset.filter(duration__lt=30)
        
        elif self.value() == '<60':
            return queryset.filter(duration__lt=60)
        
        elif self.value() == '<90':
            return queryset.filter(duration__lt=90)
        

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'payment_status', 'duration']
    list_filter = ['payment_status', DurationFilter]
    list_per_page = 10
    search_fields = ['id']
    exclude = ('date_created',)



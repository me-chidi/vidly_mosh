from django.contrib import admin
from .models import Checkout, CheckoutItem
from django.contrib.contenttypes.admin import GenericTabularInline
from movies.models import Movie, Genre
# Register your models here.

class CheckoutItemInline(GenericTabularInline):
    min_num = 1
    max_num = 5
    model = CheckoutItem
    autocomplete_fields = ['content_type']

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id',  'date_created']
    inlines = [CheckoutItemInline] 
    search_fields = ['content_type']
    exclude = ('date_created',)


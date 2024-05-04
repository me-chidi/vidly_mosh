from django.contrib import admin
from .models import Checkout
# Register your models here.

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'payment_status', 'duration']
    search_fields = ['id']
    exclude = ('date_created',)

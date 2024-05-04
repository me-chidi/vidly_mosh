from django.contrib import admin
from .models import CustomCheckoutItem
from checkout.models import Checkout
from checkout.admin import CheckoutItemInline, CheckoutAdmin

# Register your models here.
class CustomCheckoutItemInline(CheckoutItemInline):
    autocomplete_fields = ['movie']
    model = CustomCheckoutItem

class CustomCheckoutAdmin(CheckoutAdmin):
    inlines = [CustomCheckoutItemInline]

admin.site.unregister(Checkout)
admin.site.register(Checkout, CustomCheckoutAdmin)
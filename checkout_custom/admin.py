from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import CustomCheckoutItem
from checkout.models import Checkout
from checkout.admin import CheckoutAdmin

# Register your models here.
class CustomCheckoutInline(GenericTabularInline):
    autocomplete_fields = ['movie', 'checkout']
    model = CustomCheckoutItem
    min_num = 1
    max_num = 5
    # exclude = ('checkout',)

class CustomCheckoutAdmin(CheckoutAdmin):
    inlines = [CustomCheckoutInline]


admin.site.unregister(Checkout)
admin.site.register(Checkout, CustomCheckoutAdmin)
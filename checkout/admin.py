from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_id', 'date_created', 'successful', 'date_end')
    # to be fixed when i have an idea on how to call the database
    # during runtime
    exclude = ('movie_id',)

admin.site.register(Order, OrderAdmin)

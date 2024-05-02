from django.contrib import admin
from .models import Genre, Movie

# Register your models here.

#TL; registered these models/tables to be 
#viewable by only the admin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    #TL; defs the columns to be displayed 
    
class MovieAdmin(admin.ModelAdmin):
    #TL; defs the cols to be excluded data type is tuple
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate', 'genre')

#after that you register the models
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
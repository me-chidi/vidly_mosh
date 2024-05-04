from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import urlencode, format_html
from .models import Genre, Movie

# Register your models here.

#TL; registered these models/tables to be 
#viewable by only the admin
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'movies_count']
    search_fields = ['name']
    #TL; defs the columns to be displayed 

    @admin.display(ordering='movies_count')
    def movies_count(self, genre):
        url = (
            reverse('admin:movies_movie_changelist')
            + '?'
            + urlencode({
                'genre_id': str(genre.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, genre.movies_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            movies_count=Count('movie')
        ) 
    

@admin.register(Movie)    
class MovieAdmin(admin.ModelAdmin):
    #TL; defs the cols to be excluded data type is tuple
    autocomplete_fields = ['genre']
    exclude = ('date_created',)
    list_display = ['title', 'release_year', 'number_in_stock', 'daily_rate', 'genre']
    search_fields = ['title__istartswith', 'year']
    list_per_page = 10
    list_editable = ['number_in_stock', 'daily_rate']

    def genre(self, genre):
        url = (
            reverse('admin:movie_movie_changelist')
            + '?'
            + urlencode({
                'genre_id': str(genre.id)
            })
        )
        return format_html('<a href="{}"></a>', url, genre.name)
    
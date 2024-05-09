from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count, Min, Max
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
    


class YearFilter(admin.SimpleListFilter):
    title = 'release year'
    parameter_name = 'release_year'

    def lookups(self, request, model_admin):
        #using the model_admin for the queryset
        qs = model_admin.get_queryset(request)
        yeardict = qs.aggregate(
            max_year=Max('release_year'), min_year=Min('release_year'))
        ub = yeardict['max_year'] 
        lb = yeardict['min_year'] 
        # change this value as you see fit for customizations
        rng = 5
        # +1 to account for the values of YRNG >= .5 
        YRNG = (ub - lb) // rng + 1
        for i in range(YRNG):
            inc = i * rng
            ub_ = lb + inc + rng
            yield (f'>={lb+inc}&<={ub_}', f'{lb+inc}-{ub_}') 

    def queryset(self, request, queryset):
        yeardict= queryset.aggregate(
            max_year=Max('release_year'), min_year=Min('release_year'))
        ub = yeardict['max_year'] 
        lb = yeardict['min_year'] 
        # change this value as you see fit for customizations
        rng = 5
        YRNG = (ub - lb) // rng + 1
        for i in range(YRNG):
            inc = i * rng
            ub_ = lb + inc + rng
            if self.value() == f'>={lb+inc}&<={ub_}':
                return queryset.filter(release_year__gte=lb+inc, release_year__lte=ub_)

@admin.register(Movie)    
class MovieAdmin(admin.ModelAdmin):
    actions = ['clear_stock']
    autocomplete_fields = ['genre']
    exclude = ('date_created',)
    search_fields = ['title__icontains', 'year']
    list_display = ['title', 'release_year', 'number_in_stock', 'daily_rate', 'genre']
    list_per_page = 10
    list_editable = ['number_in_stock', 'daily_rate']
    list_filter = ['genre', YearFilter]

    @admin.action(description='Clear stock')
    def clear_stock(self, request, queryset):
        updated_count = queryset.update(number_in_stock=0)
        self.message_user(
            request,
            f'{updated_count} movies were successfully updated',
            messages.SUCCESS
        )

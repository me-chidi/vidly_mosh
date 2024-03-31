from django.db import models
from tastypie.resources import ModelResource
#tastypie uses django version 4.2 max so the project
#had to be downgraded from 5.0 to 4.2.8
from movies.models import Movie

# Create your models here.
#movie resource is used to define the concept of a movie for our apis
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']



from typing import Iterable
from django.db import models
from movies.models import Movie
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class order(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    successful = models.CharField(max_length=1)
    date_end = models.DateTimeField()

    def __str__(self):
        return self.id

    # TL; since datetimefield is not a variable in normal terms 
    # calling this functions save a value to it
    def clean(self):
        if not self.date_end:
            self.date_end = self.date_created + timedelta(days=1)

    def save(self, **kwargs):
        self.clean
        return super().save(**kwargs)



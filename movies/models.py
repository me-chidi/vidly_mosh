from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
   title = models.CharField(max_length=255)
   release_year = models.IntegerField()
   number_in_stock = models.IntegerField()
   daily_rate = models.FloatField()
   #TL; creating a rship with the Genre class e.g one-to-one rship
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   #TL; set the default time to the ref timzone.now not the fxn
   #so that it takes the time of when data is inputted not 
   #time of the migration
   date_created = models.DateTimeField(default=timezone.now)

   def __str__(self):
       return self.title
from django.db import models
from movies.models import Movie
from checkout.models import CheckoutItem

# Create your models here.

class CustomCheckoutItem(CheckoutItem):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


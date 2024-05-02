from django.shortcuts import render, get_object_or_404
from movies.models import Movie

# Create your views here.
def index(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'checkout/index.html', {'movie': movie})


def payment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'checkout/payment.html', {'movie': movie})



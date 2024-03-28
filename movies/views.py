from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # Movie.objecs.filter(release_year=1984)
    # Movie.objects.get(id=1) 
    #TL; defines a view fxn for an endpoint with movies in the name 
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})
    # render this page with this template and context
    # (context meaning variables??)

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
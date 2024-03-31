from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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

def detail(request, movie_id) :
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
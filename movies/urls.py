from django.urls import path
from . import views

#this gives the url tag a reference point
#to avoid continuously name spacing your urls
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
]
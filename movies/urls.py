from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies/index'),
    path('<int:movies_id>', views.detail, name='movies/detail'),
]
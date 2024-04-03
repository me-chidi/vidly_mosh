from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('<int:movie_id>', views.index, name='index'),
    path('payment/<int:movie_id>', views.payment, name='payment'),
]
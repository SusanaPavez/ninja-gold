from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('juegos/' , views.juego),
    path('reset/', views.reset),
]
from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.all_genres),
    path('recommend/', views.movies_recommend)
]

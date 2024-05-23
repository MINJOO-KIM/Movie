from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.all_genres),
    path('recommend/', views.movies_recommend),
    path('<int:movie_id>/', views.movie_detail),
    path('ai-recommend/', views.ai_recommend),
]

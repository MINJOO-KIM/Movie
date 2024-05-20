from django.urls import path
from . import views

urlpatterns = [
    path('platforms/', views.all_platforms),
]

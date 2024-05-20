from django.urls import path
from . import views

urlpatterns = [
    path('platforms/', views.all_platforms),
    path('parties/', views.parties),
    path('parties/<int:party_id>/join/', views.join_party),
]

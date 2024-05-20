from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_page),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
]


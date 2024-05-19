from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = None
    first_name = None
    last_name = None
    email = None
    is_staff = None
    is_active = None
    is_superuser = None
    last_login = None
    date_joined = None

    username = models.CharField(max_length=100, primary_key=True)
    password = models.TextField()
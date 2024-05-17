from django.db import models
from otts.models import Platform

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Director(models.Model):
    name = models.CharField(max_length=200)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    poster_url = models.CharField(max_length=500)
    overview = models.TextField()

    directors = models.ManyToManyField(Director, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    platforms = models.ManyToManyField(Platform, related_name='movies')
    
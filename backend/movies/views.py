from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Movie

from .serializers import GenreSerializer, MovieListSerializer

import random
# Create your views here.
@api_view(['GET'])
def all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(instance=genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def movies_recommend(request):
    # best_movie = request.GET.get('best-movie')
    # recommended = request.GET.get('recommended').split(',')
    # genres = request.GET.get('genres', '-1').split(',')
    # directors = request.GET.get('directors', '-1').split(',')
    # actors = request.GET.get('actors', '-1').split(',')

    
    # recommended = -1 : 영화를 추천받은 내역이 없다
    # genres = -1 : 선호하는 장르가 없다
    # directors = -1 : 선호하는 감독이 없다
    # actors = -1 : 선호하는 배우가 없다

    # print(best_movie)
    # print(recommended)
    # print(genres)
    # print(directors)
    # print(actors)


    # random 추천 기능
    last_id = Movie.objects.last().id
    movie_id_list = random.sample(range(1, last_id), 5)
    movies = Movie.objects.filter(pk__in=movie_id_list)
    serializer = MovieListSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)

        response_data = {
            'movieId': movie.id,
            'posterUrl': movie.poster_url,
            'title': movie.title,
            'genres': [genre.get('name') for genre in movie.genres.all().values()],
            'directors': [director.get('name') for director in movie.directors.all().values()],
            'actors': [actor.get('name') for actor in movie.actors.all().values()][:10],
            'rating': movie.rating,
            'overview': movie.overview,
            'platforms': [platform.get('name') for platform in movie.platforms.all().values()]
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response({"message": "Invalid Movie ID"}, status=status.HTTP_404_NOT_FOUND)
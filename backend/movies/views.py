from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


from .models import Genre, Movie
from .serializers import GenreSerializer
from .functions import *

from openai import OpenAI


# Create your views here.
@api_view(['GET'])
def all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(instance=genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

    
@api_view(['GET'])
def movies_recommend(request):
    movie_title_input = request.GET.get('best-movie', None)
    # 필수 파라미터 미입력 시 400
    if movie_title_input == None:
        return Response({"message":"best-movie is required"},
                        status=status.HTTP_400_BAD_REQUEST)
    

    # 선택 파라미터 및 필수 파라미터 활용해 필터링 정보 만들기
    filtering_infos = make_filtering_infos(request, movie_title_input)
    print(filtering_infos)
    response_data = recommend_movies(filtering_infos)
    return Response(response_data, status=status.HTTP_200_OK)



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
            'rating': round(movie.rating, 1),
            'overview': movie.overview,
            'platforms': [platform.get('name') for platform in movie.platforms.all().values()]
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Movie.DoesNotExist:
        return Response({"message": "Invalid Movie ID"}, status=status.HTTP_404_NOT_FOUND)


# Chat GPT 기반 영화 추천
@api_view(['GET'])
def ai_recommend(request):
    OPEN_AI_API_KEY = settings.OPEN_AI_API_KEY
    client = OpenAI(api_key=OPEN_AI_API_KEY)

    query = request.GET.get('q')
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role': 'user', 'content': f'영화는 반드시 5개만 추천해줘. 추천 결과는 TMDB 의 영화 id 를 []에 담아 이것만 보여줘. 추천 요청 : {query}'}],
    )

    try:
        recommended_movie_ids = response.choices[0].message.content
        recommended_movie_ids = list(map(int, recommended_movie_ids[1:-1].split(',')))
        response_data = []
        for movie_id in recommended_movie_ids:
            movie = find_movie_in_tmdb_and_save(movie_id)
            response_data.append({
                'movieId': movie.id,
                'title': movie.title,
                'posterUrl': movie.poster_url
            })

        return Response(response_data, status=status.HTTP_200_OK)
    
    except:
        movies = random_recommend(recommended_movie_ids)
        response_data = []
        for movie in movies:
            response_data.append(
                {'movieId': movie.id,
                 'title': movie.title,
                 'posterUrl': movie.poster_url}
            )
        return Response(response_data, status=status.HTTP_200_OK)
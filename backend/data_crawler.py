import requests
import os
import json

# Django 환경 불러오기
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommend.settings')
import django

# Django 초기화
django.setup()

# Django 사용
from django.conf import settings
from movies.models import Genre, Movie, Actor, Director
from otts.models import Platform

# DisneyPlus : 337
# Watcha : 97
# Netflix : 8

def api_request(url):
    return requests.get(url, headers={'Authorization': settings.TMDB_API_TOKEN})

def add_genres():
    url = 'https://api.themoviedb.org/3/genre/movie/list?language=ko'
    response = api_request(url)
    genres = json.loads(response.text).get('genres')

    for genre in genres:
        Genre(name=genre.get('name')).save()

disney_plus = 'DisneyPlus'
watcha = 'Watcha'
netflix = 'Neflix'
def add_platforms():
    Platform(name=disney_plus).save()
    Platform(name=watcha).save()
    Platform(name=netflix).save()

def add_movies(provider_id, page):
    providers = {
        8: netflix,
        97: watcha,
        337: disney_plus
    }
    # DisneyPlus : 337
    # Watcha : 97
    # Netflix : 8
    url = f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={page}&sort_by=popularity.desc&watch_region=KR&with_watch_providers={provider_id}'
    response = api_request(url)

    data = json.loads(response.text)
    for result in data.get('results'):
        movie_id = result.get('id')
        movie_title = result.get('title')
        add_movie(movie_id, movie_title, providers.get(provider_id))



def add_movie(movie_id, movie_title, platform_name):
    # 같은 제목의 영화가 이미 있으면 플랫폼 정보만 추가
    platform = Platform.objects.get(name=platform_name)
    if Movie.objects.filter(title=movie_title).exists():
        movie = Movie.objects.get(title=movie_title)
        if movie.platforms.contains(platform):
            return
        else:
            movie.platforms.add(platform)
            return
        
    # DB에 존재하지 않는 영화일 때
    # response status code 를 통해 판단
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=ko-KR&append_to_response=credits'
    response = api_request(url)
    
    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            # 영화 정보
            movie = Movie(title=data.get('title'),
                        poster_url=data.get('poster_path'),
                        rating=data.get('vote_average'),
                        overview=data.get('overview'))

            movie.save()
            # 장르 정보 추가
            for genre in data.get('genres'):
                genre_obj = Genre.objects.filter(name=genre.get('name'))[0]
                movie.genres.add(genre_obj)

            # 배우 정보 저장 및 추가
            for cast in data.get('credits').get('cast'):
                if Actor.objects.filter(name=cast.get('name')).exists():
                    actor = Actor.objects.get(name=cast.get('name'))
                else:
                    actor = Actor(name=cast.get('name'))
                    actor.save()
                movie.actors.add(actor)

            # 감독 정보 저장 및 추가
            for crew in data.get('credits').get('crew'):
                if crew.get('job') == 'Director':
                    if Director.objects.filter(name=crew.get('name')).exists():
                        director = Director.objects.get(name=crew.get('name'))
                    else:
                        director = Director(name=crew.get('name'))
                        director.save()
                    movie.directors.add(director)

            # OTT 플랫폼 정보
            movie.platforms.add(platform)

            print(movie_id, ": SUCCESS")
        except:
            print(f'{movie_id} : FAIL')
    else:
        print(f'{movie_id} : NOT EXIST')

# 사전 실행 함수
# add_genres()
# add_platforms()


# DisneyPlus : 337
# Watcha : 97
# Netflix : 8
# provider_ids = [337, 97, 8]
# for provider_id in provider_ids: 
#     for page in range(1, 10 + 1): # 페이지 조절을 통해 다른 정보들도 수집 가능
#         add_movies(provider_id, page)
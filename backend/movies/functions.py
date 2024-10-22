# 동적 쿼리
from django.db.models import Q
from functools import reduce
import operator

# 사용자 정의 함수
from django.conf import settings
import sqlite3

# 레벤슈타인 거리 라이브러리
from Levenshtein import distance


# 랜덤 라이브러리
import random

# TMDB 요청 및 응답 데이터 가공에 필요한 라이브러리
import requests
import json

# 환경변수 사용
from django.conf import settings

from .models import Movie, Actor, Director, Genre
from otts.models import Platform

FILTERING_KEYS = ['genres_ids', 'director_names', 'actor_names', 'recommended_movie_ids']

def levenshtein_distance(str1, str2):
    return distance(str1, str2)

# DB 자원 관련 함수들
def get_connection():
    conn = sqlite3.connect(settings.DATABASES.get('default').get('NAME'))
    conn.create_function("calc_distance", 2, levenshtein_distance)
    return conn

def close(conn, cursor):
    cursor.close()
    conn.close()


# 입력받은 제목과 최대한 유사한 제목의 영화 찾기
def find_movie(movie_title_input):
    conn = get_connection()
    cursor = conn.cursor()

    space_removed_title = movie_title_input.replace(' ', '')
    cursor.execute(f"""
                    SELECT id
                    FROM movies_movie 
                    WHERE REPLACE(title, ' ', '') LIKE '%{space_removed_title}%'
                    ORDER BY calc_distance(REPLACE(title, ' ', ''), '{space_removed_title}')
                    LIMIT 1
                   """)
  
    result = cursor.fetchone()
    close(conn, cursor)

    if result == None: return None
    return Movie.objects.get(id=result[0])

# 감독명을 이용해 DB에서 가장 유사한 감독 조회
def find_director(director_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
                   SELECT name
                   FROM movies_director
                   ORDER BY calc_distance(REPLACE(name, ' ', ''), '{director_name}')
                   LIMIT 1
                   """)

    result = cursor.fetchone()
    close(conn, cursor)
    return result
    
# 배우명을 이용해 DB에서 가장 유사한 배우 조회
def find_actor(actor_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
                SELECT name
                FROM movies_actor
                ORDER BY calc_distance(REPLACE(name, ' ', ''), '{actor_name}')
                LIMIT 1
                """)

    result = cursor.fetchone()
    close(conn, cursor)
    return result


# 영화 객체로부터 속한 장르 아이디, 연출한 감독, 출연한 배우 정보 추출
def get_infos_from_movie(movie_obj):
    genre_ids = list(map(lambda data: data.get('id'), 
                         list(movie_obj.genres.all().values('id'))))
    director_names = list(map(lambda data: data.get('name'), 
                              list(movie_obj.directors.all().values('name'))))
    actor_names = list(map(lambda data: data.get('name'),
                           list(movie_obj.actors.all().values('name')[:10])))

    return {FILTERING_KEYS[0]:genre_ids, 
            FILTERING_KEYS[1]:director_names, 
            FILTERING_KEYS[2]:actor_names,
            FILTERING_KEYS[3]:[movie_obj.id]}


# HTTP 요청 파라미터로부터 선호 장르, 감독, 배우 정보 추출
def get_infos_from_request(request):
    genre_strs = request.GET.get('genres', None)
    director_strs = request.GET.get('directors', None)
    actor_strs = request.GET.get('actors', None)

    if director_strs == "":
        director_strs = None

    if actor_strs == "":
        actor_strs = None

    genre_ids = []
    if genre_strs == "":
        genre_strs = None
        
    if genre_strs != None:
        genre_ids = list(map(int, genre_strs.replace(' ', '').split(',')))

    found_director_names = []
    if director_strs != None:
        director_names = director_strs.replace(' ', '').split(',')
        for director_name in director_names:
            director = find_director(director_name)
            if director != None:
                found_director_names.append(director[0])


    found_actor_names = []
    if actor_strs != None:
        actor_names = actor_strs.replace(' ', '').split(',')
        for actor_name in actor_names:
            actor = find_actor(actor_name)
            if actor != None:
                found_actor_names.append(actor[0])

    return {
        FILTERING_KEYS[0]: genre_ids,
        FILTERING_KEYS[1]: found_director_names,
        FILTERING_KEYS[2]: found_actor_names
    }


# 요청 파라미터들을 활용해서 필터링 정보 만들기
def make_filtering_infos(request, movie_title_input):
    movie = find_movie(movie_title_input)
    infos = {FILTERING_KEYS[0]:[],
             FILTERING_KEYS[1]:[],
             FILTERING_KEYS[2]:[],
             FILTERING_KEYS[3]:[]}
    if movie != None:
        infos = get_infos_from_movie(movie)
    
    info2 = get_infos_from_request(request)
    infos.get(FILTERING_KEYS[0]).extend(info2.get(FILTERING_KEYS[0]))
    infos.get(FILTERING_KEYS[1]).extend(info2.get(FILTERING_KEYS[1]))
    infos.get(FILTERING_KEYS[2]).extend(info2.get(FILTERING_KEYS[2]))
    

    recommended = request.GET.get('recommended', None)
    if recommended != None and recommended != "":
        infos.get(FILTERING_KEYS[3]).extend(list(map(int, recommended.replace(' ', '').split(','))))

    return infos



def make_filter_query(genre_ids=[], director_names=[], actor_names=[]):
    filters = []
    if len(genre_ids) > 0:
        filters.append(Q(genres__id__in=genre_ids))
    
    if len(director_names) > 0:
        filters.append(Q(directors__name__in=director_names))
    
    if len(actor_names) > 0:
        filters.append(Q(actors__name__in=actor_names))

    combined_filter = reduce(operator.and_, filters, Q())
    return combined_filter


def random_recommend(recommended_movie_ids=[]):
    last_id = Movie.objects.all().last().id
    results = set()
    while len(results) < 5:
        movie_id_list = random.sample(range(1, last_id), 2)
        movies = Movie.objects.filter(id__in=movie_id_list).exclude(id__in=recommended_movie_ids).all()
        for movie in movies:
            results.add(movie)
            if len(results) >= 5: break
        if len(results) >= 5: break
    return results


# 영화 추천 함수
def recommend_movies(filtering_infos):
    genre_ids = filtering_infos.get(FILTERING_KEYS[0])
    director_names = filtering_infos.get(FILTERING_KEYS[1])
    actor_names = filtering_infos.get(FILTERING_KEYS[2])
    recommended_movie_ids = filtering_infos.get(FILTERING_KEYS[3])

    # 필터링 정보가 아예 생성되지 않았을 때
    if len(genre_ids) == 0 and len(director_names) == 0 and len(actor_names) == 0 and len(recommended_movie_ids) == 0:
        # 랜덤으로 추천
        movies = random_recommend(recommended_movie_ids)
        response_data = []
        for movie in movies:
            response_data.append(
                {'movieId': movie.id,
                 'title': movie.title,
                 'posterUrl': movie.poster_url}
            )
        return response_data
    else:
        response_data = []
        # 장르, 감독, 배우 정보 전부 활용
        filter_options = make_filter_query(genre_ids, director_names, actor_names)
        results = set()
        movies = Movie.objects.filter(filter_options).exclude(
            id__in=recommended_movie_ids).order_by('-rating')
        for movie in movies:
            if len(results) >= 5:break
            results.add(movie)
        

        # 장르, 감독 정보 활용
        if len(results) < 5:
            filter_options = make_filter_query(genre_ids, director_names)
            movies = Movie.objects.filter(filter_options).exclude(
                id__in=recommended_movie_ids).order_by('-rating')
            for movie in movies:
                if len(results) >= 5:break
                results.add(movie)

        # 장르, 배우 정보 활용
        if len(results) < 5:
                    filter_options = make_filter_query(genre_ids, actor_names=actor_names)
                    movies = Movie.objects.filter(filter_options).exclude(
                        id__in=recommended_movie_ids).order_by('-rating')
                    for movie in movies:
                        if len(results) >= 5:break
                        results.add(movie)



        # 장르 정보 활용
        if len(results) < 5:
            filter_options = make_filter_query(genre_ids)
            movies = Movie.objects.filter(filter_options).exclude(
                id__in=recommended_movie_ids).order_by('-rating')
            for movie in movies:
                if len(results) >= 5:break
                results.add(movie)

        for result in results:
            response_data.append({
                'movieId': result.id,
                'title': result.title,
                'posterUrl': result.poster_url,
            })
        
        return response_data
    


def find_movie_in_tmdb_and_save(movie_id):
    TMDB_API_TOKEN = settings.TMDB_API_TOKEN
    # detail 정보 요청
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?',
                        headers={'Authorization': f'Bearer {TMDB_API_TOKEN}'},
                        params={'language':'ko-KR',
                                'append_to_response':'credits'})
    

    movie_info = json.loads(response.text)
    if Movie.objects.filter(title=movie_info.get('title')).exists():
        return Movie.objects.filter(title=movie_info.get('title'))[0]


    movie = Movie(title=movie_info.get('title'),
                  poster_url=movie_info.get('poster_path'),
                  rating=movie_info.get('vote_average'),
                  overview=movie_info.get('overview'))
    
    movie.save()

    
    # 장르 정보 추가
    for genre in movie_info.get('genres'):
        genre_obj = Genre.objects.filter(name=genre.get('name'))[0]
        movie.genres.add(genre_obj)


    # 배우 정보 저장 및 추가
    for cast in movie_info.get('credits').get('cast'):
        if Actor.objects.filter(name=cast.get('name')).exists():
            actor = Actor.objects.get(name=cast.get('name'))
        else:
            actor = Actor(name=cast.get('name'))
            actor.save()
        movie.actors.add(actor)


    # 감독 정보 저장 및 추가
    for crew in movie_info.get('credits').get('crew'):
        if crew.get('job') == 'Director':
            if Director.objects.filter(name=crew.get('name')).exists():
                director = Director.objects.get(name=crew.get('name'))
            else:
                director = Director(name=crew.get('name'))
                director.save()
            movie.directors.add(director)


    # OTT 플랫폼 정보 추가
    response = requests.get('https://api.themoviedb.org/3/movie/479718/watch/providers',
                            headers={'Authorization':f'Bearer {TMDB_API_TOKEN}'},
                            params={'movie_id':movie_id})
    
    kr_ott_platforms = json.loads(response.text).get('results').get('KR').get('flatrate')

    for ott_platform in kr_ott_platforms:
        # DisneyPlus : 337
        # Watcha : 97
        # Netflix : 8
        provider_id = ott_platform.get('provider_id')
        if provider_id not in (337, 97, 8): continue

        if provider_id == 337:
            platform_obj = Platform.objects.get(id=1)
        elif provider_id == 97:
            platform_obj = Platform.objects.get(id=2)
        else:
            platform_obj = Platform.objecst.get(id=3)

        movie.platforms.add(platform_obj)

    return movie


def find_movie_id_from_title(movie_title):
    TMDB_API_TOKEN = settings.TMDB_API_TOKEN
    # detail 정보 요청
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?',
                        headers={'Authorization': f'Bearer {TMDB_API_TOKEN}'},
                        params={'language':'ko-KR',
                                'query': movie_title})
    
    return json.loads(response.text).get('results')[0].get('id')
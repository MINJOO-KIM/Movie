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

from .models import Movie

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

    genre_ids = []
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
    if recommended != None:
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


def random_recommend(recommended_movie_ids):
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
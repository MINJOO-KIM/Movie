from rest_framework import serializers
from .models import Genre, Movie, Actor, Director
from otts.models import Platform


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    movieId = serializers.IntegerField(source='id')
    posterUrl = serializers.CharField(source='poster_url')

    class Meta:
        model = Movie
        fields = ('movieId', 'posterUrl')

# 영화 디테일 정보는 조작해야 할 것이 많아 직접 딕셔너리로 만드는 게 나을 수 있다.
# class MovieSerializer(serializers.ModelSerializer):
#     class GenreListSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Genre
#             fields = ('name',)

#     class ActorListSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Genre
#             fields = ('name',)

#     class DirectorListSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Director
#             fields = ('name',)

#     class PlatFormListSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Platform
#             fields = ('name',)

#     movieId = serializers.IntegerField(source='id')
#     posterUrl = serializers.CharField(source='poster_url')
#     genres = GenreListSerializer(read_only=True, many=True)
#     actors = ActorListSerializer(read_only=True, many=True)
#     directors = DirectorListSerializer(read_only=True, many=True)
#     platforms = PlatFormListSerializer(read_only=True, many=True)

#     class Meta:
#         model = Movie
#         fields = ('movieId', 'posterUrl', 'title',
#                   'genres', 'directors', 'actors',
#                   'rating', 'overview', 'platforms')

#     def to_representation(self, instance):
#         """
#         주,조연 포함 출연 배우가 너무 많아 제한된 숫자로 응답할 필요가 있다.
#         하지만 이 경우 유저가 선호하는 배우가 아니라 같이 영화에 출연한 다른 배우들만 응답할 우려가 있음.
#         """
#         ret = super().to_representation(instance)
#         ret['actors'] = self.ActorListSerializer(instance=instance.actors.all()[:5], many=True).data
#         return ret
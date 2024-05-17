from rest_framework import serializers
from .models import Genre, Movie

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
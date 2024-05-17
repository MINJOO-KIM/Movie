from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Genre

from .serializers import GenreSerializer
# Create your views here.
@api_view(['GET'])
def all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(instance=genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
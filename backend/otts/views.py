from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Platform
from .serializers import PlatformListSerializer

# Create your views here.
@api_view(['GET'])
def all_platforms(request):
    platforms = Platform.objects.all()
    serializer = PlatformListSerializer(instance=platforms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
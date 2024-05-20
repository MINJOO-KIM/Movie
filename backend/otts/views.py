from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Platform, Party
from .serializers import PlatformListSerializer, PartyCreateSerializer, PartyListSerializer

from accounts.utils import validate_token

# Create your views here.
@api_view(['GET'])
def all_platforms(request):
    platforms = Platform.objects.all()
    serializer = PlatformListSerializer(instance=platforms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def parties(request):

    if request.method == 'POST':
        result = validate_token(request)
        if not result[0]: return result[1]

        user = request.user
        if not Platform.objects.filter(id=request.data.get('platform')).exists():
            return Response({"message": "Invalid Platform Id"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        platform = Platform.objects.get(id=request.data.get('platform'))
        serializer = PartyCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            party = serializer.save(owner=user, platform=platform)
            return Response({"partyId": party.id},
                            status=status.HTTP_200_OK) 

    elif request.method == 'GET':
        party_list = Party.objects.all()
        serializer = PartyListSerializer(party_list, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

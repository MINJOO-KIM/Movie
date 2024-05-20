from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from otts.models import Party
from otts.serializers import MyPagePartyListSerializer

import json
# Create your views here.
User = get_user_model()

@api_view(['POST'])
def signup(request):
    data = json.loads(request.body)
    print(data)
    username = data.get('username')

    # username 이 중복되는 경우
    if User.objects.filter(username=username).exists():
        print("뭐가 문제지")
        return Response({"message" : "Duplicate username"},
                        status=status.HTTP_409_CONFLICT)
    
    # 비밀번호 암호화
    password = data.get('password')
    encryted_password = make_password(password)

    # 유저 정보 저장
    user = User(username=username, password=encryted_password)
    user.save()

    return Response({"message":"Success"},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    # 잘못된 username 인 경우
    if not User.objects.filter(username=username).exists():
        return Response({"message":"Invalid username",
                         "wrong":1},
                         status=status.HTTP_400_BAD_REQUEST)
    

    saved_user = User.objects.get(username=username)
    # 잘못된 비밀번호인 경우
    if not check_password(password, saved_user.password):
        return Response({"message": "Invalid password",
                         "wrong": 2},
                        status=status.HTTP_400_BAD_REQUEST)
    
    token = Token.objects.get_or_create(user=saved_user)[0]
    return Response({"message":"Success",
                     "key":token.key},
                     status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    key = token[6:]
    Token.objects.get(key=key).delete()

    return Response({"message":"OK"},
                    status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_page(request):
    user = request.user

    own_parties = Party.objects.filter(owner=user)
    participate_parteis = Party.objects.filter(participants=user).exclude(id__in=own_parties)

    serializer1 = MyPagePartyListSerializer(instance=own_parties, many=True)
    serializer2 = MyPagePartyListSerializer(instance=participate_parteis, many=True)

    return Response({
        "own": serializer1.data,
        "participate": serializer2.data
    }, status=status.HTTP_200_OK)
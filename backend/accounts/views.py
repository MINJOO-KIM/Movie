from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
# Create your views here.
User = get_user_model()
@api_view(['POST'])
def signup(request):
    data = json.loads(request.body)
    username = data.get('username')

    # username 이 중복되는 경우
    if User.objects.filter(username=username).exists():
        return Response({"message" : "Duplicate username"},
                        status=status.HTTP_409_CONFLICT)
    
    # 비밀번호 암호화
    password = data.get('password')
    encryted_password = make_password(password)

    # 유저 정보 저장
    user = User(username, password=encryted_password)
    user.save()

    return Response({"message":"Success"},
                    status=status.HTTP_200_OK)
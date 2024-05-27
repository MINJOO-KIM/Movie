from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

def validate_token(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if token == None:
        return (False, Response({"detail": "Authorization header is empty"},
                                status=status.HTTP_401_UNAUTHORIZED))

    key = token[6:]
    if not Token.objects.filter(key=key).exists():
        return (False, Response({"detail": "Invalid Token"},
                                status=status.HTTP_401_UNAUTHORIZED))
    
    return (True, get_user_from_token(key))


def get_user_from_token(key):
    token = Token.objects.get(key=key)
    return token.user


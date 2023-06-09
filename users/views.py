
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserAuthorizeSerializer


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthorizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, creted = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.create(username=username, password=password)
        return Response(data={'user_id': user.id})

# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = UserCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = User.objects.create_user(
#             username = serializer.validated_data['username'],
#             password = serializer.validated_data['password'],
#             is_active= serializer.validated_data['is_active'],
#         )
#         return Response(data={'user_id': user.id})
#
#
# @api_view(['Post'])
# def confirm_api_view(request):
#     serializer = User(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response()
#
# @api_view(['POST'])
# def authorization_view(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         """AUTHENTICATE USER"""
#         user = authenticate(username=username, password=password)
#         """RETURN TOKEN"""
#         if user is not None:
#             token_, _ = Token.objects.get_or_create(user=user)
#             return Response(data={'key': token_.key})
#
#         """ERROR"""
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
from django.shortcuts import render
from rest_framework import viewsets

from common import models
from . import serializers

import json

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.authtoken.models import Token
from . import permission


# Create your views here.


 # 등록 기능
class RegistGenericView(generics.GenericAPIView):
    serializer_class = serializers.AuthUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user = user)
        return Response(
            {
                "user": serializers.LoginUserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key,
            }
        )

 # 유저 로그인 확인 후 유저 정보 제공
class UserAuthAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        users = models.UsersAdditionalInfo.objects.select_related('user_info').filter(user_info=self.request.user)
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data[0])
 # 유저 로그인 기능
class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "user": serializers.InfoSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key,
            }
        )
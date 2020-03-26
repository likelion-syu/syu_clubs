from django.shortcuts import render
from rest_framework import viewsets

from common import models
from . import serializers

# Create your views here.


class AuthUserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthUserSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
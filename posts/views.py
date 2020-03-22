from django.shortcuts import render
from rest_framework import viewsets

from common import models
from . import serializers
# Create your views here.


class PostsViewset(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
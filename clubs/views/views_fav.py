from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from ..serializers import serializers_fav

# Create your views here.


# TODO : 로그인한 사람의 모든 관심 동아리 목록
# TODO : 로그인한 사람의 관심 동아리에 추가 put
# TODO : 로그인한 사람의 관심 동아리에서 삭제 delet

# VIEWSET을 customermize
# serializer : foreign key를 어떻게 다루는지.
# join in django models.

class Clubs_favViewset(viewsets.ModelViewSet):
    queryset = models.RelInterestClubs.objects.all()
    serializer_class = serializers_fav.Club_favSerializer


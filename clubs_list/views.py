from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from . import serializers
# Create your views here.


class Clubs_listViewset(viewsets.ModelViewSet):
    queryset = models.Clubs.objects.all()
    serializer_class = serializers.Club_listSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['club_name', 'club_type']
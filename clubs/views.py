from django.shortcuts import render
from rest_framework import viewsets

from common import models
from . import serializers
# Create your views here.


class ClubsViewset(viewsets.ModelViewSet):
    queryset = models.Clubs.objects.all()
    serializer_class = serializers.ClubSerializer

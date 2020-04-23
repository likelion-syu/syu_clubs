from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from ..serializers import serializers_club
# Create your views here.


class ClubsViewset(viewsets.ModelViewSet):
    queryset = models.Clubs.objects.all()
    serializer_class = serializers_club.ClubSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search','')
        if search:
            qs = qs.filter(club_name=search)
        return qs   
    
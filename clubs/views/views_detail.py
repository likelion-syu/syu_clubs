from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from ..serializers import serializers_detail
# Create your views here.


class Clubs_detailViewset(viewsets.ModelViewSet):
    queryset = models.Clubs.objects.all()
    serializer_class = serializers_detail.Club_detailSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search','')
        if search:
            qs = qs.filter(club_name=search)
        return qs   
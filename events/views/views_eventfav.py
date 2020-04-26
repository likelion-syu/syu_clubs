from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from ..serializers import serializers_eventfav
# Create your views here.

class event_favViewset(viewsets.ModelViewSet):
    serializer_class = serializers_eventfav.Club_eventfavSerializer
    queryset = models.RelInterestClubs.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(user = self.request.user)
        else:
            qs = qs.none()

        return qs
   
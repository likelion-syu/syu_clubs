from django.shortcuts import render
from rest_framework import viewsets, permissions
from user.permission import IsRAuthenticated


from common import models
from . import serializers
# Create your views here.


class ClubsViewset(viewsets.ModelViewSet):
    permission_classes=[IsRAuthenticated]
    queryset = models.Clubs.objects.all()
    serializer_class = serializers.ClubSerializer

from django.shortcuts import render
from rest_framework import viewsets, permissions


from common import models
from . import serializers
# Create your views here.


class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Messages.objects.all()
    serializer_class = serializers.MessageSerializer

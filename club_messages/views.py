from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from common import models
from . import serializers

# Create your views here.


class MessageViewset(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = serializers.MessageSerializer


class MessageDetailViewset(APIView):
    def get(self, request, receive_user, format=None):
        queryset = Messages.objects.filter(receive_user=33)
        serializer_class = serializers.MessageSerializer
        return Response(serializer.data)

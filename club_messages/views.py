from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from common import models
from . import serializers

# Create your views here.


class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Messages.objects.all()
    serializer_class = serializers.MessageSerializer


class MessageDetailViewset(APIView):
    queryset=''
    def get(self, request, send_user, format=None):
        queryset = models.Messages.objects.filter(receive_user=request.user.id,send_user=send_user)
        serializer = serializers.MessageSerializer(queryset,many=True)
        serializer_class = serializers.MessageSerializer
        return Response(serializer.data)

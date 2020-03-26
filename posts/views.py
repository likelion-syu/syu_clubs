from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from common import models
from . import serializers

from rest_framework import status
from rest_framework import filters

class PostsViewSet(APIView):
    
    def get(self, request, format=None):
        qs = self.queryset.filter(is_deleted=0).order_by('-date')[0:7]
        serializer = self.PostSerializer(qs, many=True)
        return Response(serializer.data)
    

class PostDetailViewSet(APIView):
    # post_id라고 해야하는지 잘 모르겠음
    def get(self, request, id, format=None):
        queryset = Post.objects.order_by('-date').all()
        serializer = PostSerializer(queryset, many=False)
        filter_backends = (filters.DjangoFilterBackend,)    
        filter_fields = ('post_id',)
        return Response(serializer.data)
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

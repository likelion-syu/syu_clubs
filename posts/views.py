from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from common import models
from . import serializers

class PostsViewSet(APIView):
    
    def get(self, request, format=None):
        qs = self.queryset.filter(is_deleted=0).order_by('-date')[0:7]
        serializer = self.PostSerializer(qs, many=True)
        return Response(serializer.data)
    

<<<<<<< HEAD
class PostDetailViewSet(APIView):
    # post_id라고 해야하는지 잘 모르겠음
    def get(self, request, id, format=None):
        queryset = Post.objects.get(id=post_id)
        serializer = PostSerializer(queryset, many=False)
        return Response(serializer.data)
=======
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
>>>>>>> 9a03f7b97cc8aa93c3f0ba322dd0aab9032081a3

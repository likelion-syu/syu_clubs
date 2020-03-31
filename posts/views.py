from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
#from common import models
from common.models import Posts
from .serializers import PostSerializer

from rest_framework import status
from rest_framework import filters
#동아리별 활동 목록
class PostsViewSet(APIView):
    def get(self, request, format=None):
        #qs = self.queryset.filter(is_deleted=0).order_by('-date')[0:7]
        qs = Posts.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    
    
#동아리별 활동 상세페이지
class PostDetailViewSet(APIView):
    # post_id라고 해야하는지 잘 모르겠음
    def get(self, request, post_id, format=None):
        queryset = Posts.objects.get(post_id=post_id)
        serializer = PostSerializer(queryset, many=False)
        # filter_backends = (filters.DjangoFilterBackend,)    
        # filter_fields = ('post_id',)
        return Response(serializer.data)

    def put(self, request, post_id, format=None)
        qs = Posts.objects.get(post_id=post_id)
        serializer = PostSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("수정할 수 없습니다.")

    def delete(self, request, post_id, format=None)
        post = Posts.objects.get(post_id=post_id)
        post.delete()
    return Response("삭제완료")
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
#글 수정기능
# class PostEdit(APIView):
#     def get(self, request, id, format=None):
#         queryset = Post.objects.get(post_id=post_id)
#         if queryset.user==request.user.email:
#             serializer = PostSerializer(queryset, many=False)
#             return Response(serializer.data)

#     def post(self, request, id, format=None):
#         post = Post.objects.get(post_id=post_id)
#         post.post_title_img_url = request.data['post_title_img_url']
#         post.post_content = request.data['post_content']
#         post.post_title = request.data['post_title']
#         post.category = Category.objects.get(name=request.data['category'])
#         post.link = request.data['link']
#         post.save()
#         return Response("Post edited")
#공지목록
class NoticeViewSet(APIView):
    def get(self, request, id, format=None):
        queryset = Posts.objects.filter(is_noticed=id)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
=======
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
>>>>>>> 88cd620ddb63bb1a43fe4191690b5b8242d34626

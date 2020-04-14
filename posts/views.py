from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
#권한설정
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permission import IsAdminUserOrReadOnly, IsOwnerOrReadOnly
#from common import models
from common.models import Posts
from .serializers import PostSerializer,PostDetailSerializer, addPost
from rest_framework import status
from rest_framework import filters
from django.http import Http404

#동아리별 활동 목록
class PostsViewSet(APIView):
    def get(self, request, format=None):
        #qs = self.queryset.filter(is_deleted=0).order_by('-date')[0:7]
        qs = Posts.objects.all() #나중에 is_deleted = 0 필터 넣어야함
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data) 
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():  
            serializer.save(user=request.user)     
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#공지등록포스트목록
class NoticedPosts(APIView):
    def get(self, request, format=None):
        qs = Posts.objects.filter(is_notice=1)  #나중에 is_deleted = 0 필터 넣어야함
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data) 

#동아리별 활동,공지 상세페이지
class PostDetailViewSet(APIView):
    # 매개변수를 post_id라고 해야하는지 잘 모르겠음
    def get(self, request, post_id, format=None):
        queryset = Posts.objects.get(post_id=post_id)
        serializer = PostDetailSerializer(queryset, many=False)
        return Response(serializer.data)

    def put(self, request, post_id, format=None):
        qs = Posts.objects.get(post_id=post_id)
        serializer = PostDetailSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("수정할 수 없습니다.")

    def delete(self, request, post_id, format=None):
        qs = Posts.objects.get(post_id=post_id)
        if request.user == qs.user:
            serializer = PostDetailSerializer(qs, many=False)
            qs.is_deleted = 1
            print("함수")
        return Response("삭제완료")

#원격 브랜치가 만들어지는지 보려고 일부러 수정중입니다 흑흑
#프로젝트가 끝나면 전과할거심..



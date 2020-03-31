#from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.views import APIView

# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.pagination import PageNumberPagination
# from common import models
# from . import serializers
# # 한페이지당 게시물 수 제한
# class PostPagination(PageNumberPagination):
#     page_size = 7
    
# class PostsViewset(viewsets.ModelViewSet):
#     queryset = models.Posts.objects.all().order_by('post_id')
#     serializer_class = serializers.PostSerializer
#     pagination_class = PostPagination
    
#     # 목록에서 permission받은 유저만 create가능
#     @action(detail = False method="post")
#     # @permission_classes(permissions.)
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
#     # 포스트 목록 모든 유저 접근가능
#     @action(detail=False method="get")
#     def public_list(self, request):
#         qs = self.queryset.filter(is_deleted=0)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     @action(detail=False method="get")

# # 이건 필요 없겠지
# class PostDetailViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Posts.objects.all()
#     serializer_class = serializers.PostSerializer
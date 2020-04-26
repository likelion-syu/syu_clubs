from django.urls import path, include
from django.conf.urls import url
from . import views

from rest_framework import routers

#router = routers.DefaultRouter()

#router.register('', views.PostsViewSet)

urlpatterns = [
    #path('', include(router.urls)), 
    path('', views.PostsViewSet.as_view()),
    #동아리 공지 목록
    path('notice', views.NoticedPosts.as_view()),
    #동아리 상세페이지
    path('detail/<int:post_id>/', views.PostDetailViewSet.as_view(),name='post_detail'), 
]

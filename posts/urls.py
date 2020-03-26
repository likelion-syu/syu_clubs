from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('', views.PostsViewset)

urlpatterns = [
    path('', include(router.urls)),
    # 
    url(r'^api/post/$', views.PostViewSet.as_view(), name="post"),
    url(r'^api/post/(?P<id>\d+)/$', views.PostDetailViewSet.as_view(), name="postdetail"),
]

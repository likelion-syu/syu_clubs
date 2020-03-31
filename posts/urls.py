from django.urls import path, include
from django.conf.urls import url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

#router.register('', views.PostsViewset)

urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
    
    url(r'^api/posts/', views.PostsViewSet.as_view(), name="post"),
    url(r'^(?P<post_id>\d+)/$', views.PostDetailViewSet.as_view(), name="postdetail"),
=======
    # 
    url(r'^api/posts/$', views.PostsViewSet.as_view(), name="post"),
    url(r'^api/posts/(?P<post_id>\d+)/$', views.PostDetailViewSet.as_view(), name="postdetail"),
>>>>>>> 88cd620ddb63bb1a43fe4191690b5b8242d34626
]

from django.urls import path, include
from django.conf.urls import url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

#router.register('', views.PostsViewset)

urlpatterns = [
    #path('', include(router.urls)),
    
    url(r'^', views.PostsViewSet.as_view(), name="post"),
    url(r'^(?P<post_id>\d+)/$', views.PostDetailViewSet.as_view(), name="postdetail"),
]

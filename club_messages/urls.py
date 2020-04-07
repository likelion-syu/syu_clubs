from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', views.MessageViewset)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/messages/$', views.MessageViewset.as_view(), name='message'),
    url(r'^api/messages/(?P<receive_user>\d+)/$', views.MessageDetailViewset.as_view(), name='messagedetail'),
]
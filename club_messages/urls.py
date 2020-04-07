from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', views.MessageViewset)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/messages/$', views.MessageViewset, name='message'),
    url(r'^/detail/(?P<send_user>\d+)/$', views.MessageDetailViewset.as_view(), name='messagedetail'),
]
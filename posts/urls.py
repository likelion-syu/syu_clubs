from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('posts', views.PostsViewset)

urlpatterns = [
    path('board/', include(router.urls)),
]
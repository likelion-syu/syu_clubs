from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('club', views.ClubsViewset)

urlpatterns = [
    path('union/', include(router.urls)),
]
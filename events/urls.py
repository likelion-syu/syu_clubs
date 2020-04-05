from django.urls import path, include

from .views import views_event
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', views_event.Club_eventViewset)


urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include

from .views import views_event, views_eventfav
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', views_event.eventViewset)
router.register('fav', views_eventfav.event_favViewset)


urlpatterns = [
    path('', include(router.urls)),
]
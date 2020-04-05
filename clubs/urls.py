from django.urls import path, include

from .views import views_club, views_fav

from rest_framework import routers

router = routers.DefaultRouter()

router.register('list', views_club.ClubsViewset)
router.register('fav', views_fav.Clubs_favViewset)

urlpatterns = [
    path('', include(router.urls)),
]
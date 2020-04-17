from django.urls import path, include

from .views import views_club, views_fav, views_detail

from rest_framework import routers

router = routers.DefaultRouter()

router.register('list', views_club.ClubsViewset)
router.register('fav', views_fav.Clubs_favViewset)
router.register('detail', views_detail.Clubs_detailViewset)

urlpatterns = [
    path('', include(router.urls)),
]
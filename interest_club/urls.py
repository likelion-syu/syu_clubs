from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import InterestClubViewSet

router = DefaultRouter()
router.register('', InterestClubViewSet)

urlpatterns = [
    path('', include(router.urls))
]
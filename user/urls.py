from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

# router.register('', views.AuthUserViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('regist', views.RegistGenericView.as_view(), name="regist"),
    path('auth', views.UserAuthAPIView.as_view(), name="auth"),
    path('login', views.LoginAPI.as_view(), name="login"),
    
]
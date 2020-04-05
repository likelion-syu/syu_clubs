"""syu_clubs_api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
import rest_framework.urls
import posts.urls


urlpatterns = [
    # 모든 주소를 우선 client 쪽으로 연결 시킴
    url(r'^$', TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/clubs/', include('clubs.urls')),

    path('api-auth/', include(rest_framework.urls)), # logout dropdown

    path('api/interest-club/', include('interest_club.urls')),
    path('api-token-auth/', obtain_auth_token),

    path('api/club-ask/', include('club_asks.urls')),

    path('api/users/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

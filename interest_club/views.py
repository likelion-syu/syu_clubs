from common.models import RelInterestClubs
from .serializers import InterestClubSerializer
from rest_framework import viewsets
from .pagination import MyPagination

from rest_framework.authentication import SessionAuthentication, TokenAuthentication #####
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser #####

class InterestClubViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication] #####
    permission_classes = [IsAdminUser] #####
    
    queryset = RelInterestClubs.objects.all().order_by('-updated_at')
    serializer_class = InterestClubSerializer
    
    pagination_class = MyPagination

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user)
        else:
            qs = qs.none()

        return qs

        if memo.likes.filter(id = user.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            memo.likes.remove(user) #likes 컬럼에서 해당 유저를 지운다.
            message = 'You disliked this'
        else:
            memo.likes.add(user)
            message = 'You liked this'
            
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
from common import models
from .serializers import ClubAskSerializer
from rest_framework import viewsets
from .pagination import MyPagination

class ClubAskViewSet(viewsets.ModelViewSet):

    queryset = models.Posts.objects.all()
    serializer_class = ClubAskSerializer
    
    pagination_class = MyPagination

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user)

        else:
            qs = qs.none()

        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
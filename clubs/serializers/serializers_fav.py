from rest_framework import serializers
from common import models

class clubSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Clubs
        fields = '__all__'

class Club_favSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    club = clubSerializer()
    class Meta:
        model = models.RelInterestClubs
        fields ='__all__'


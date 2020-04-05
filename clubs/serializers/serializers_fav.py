from rest_framework import serializers
from common import models

class Club_favSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    user_name = serializers.ReadOnlyField(source='user.username')
    club_id = serializers.ReadOnlyField(source='clubs.club_id')
    class Meta:
        model = models.RelInterestClubs
        fields ='__all__'


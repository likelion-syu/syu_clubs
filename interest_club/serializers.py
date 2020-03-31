from common.models import RelInterestClubs
from common import models
from rest_framework import serializers


class InterestClubSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = RelInterestClubs
        fields = "__all__"


class InterestClubSerializer(serializers.ModelSerializer):
    club_name = serializers.ReadOnlyField(source='club.club_name')
    user_name = serializers.ReadOnlyField(source = 'user.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = RelInterestClubs
        fields = [
            'url',
            'club',
            'club_name',
            'user_name',
            'created_at',
            'updated_at',
        ]
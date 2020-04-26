from rest_framework import serializers
from common import models


class Club_eventSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ClubEvents
		fields = '__all__'

class ClubsSerializer(serializers.ModelSerializer):
    club_events = Club_eventSerializer(many=True)
    class Meta:
        model = models.Clubs
        fields = '__all__'

class Club_eventfavSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    club = ClubsSerializer()
    class Meta:
        model = models.RelInterestClubs
        fields ='__all__'

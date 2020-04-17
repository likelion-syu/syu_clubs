from rest_framework import serializers
from common import models


class Club_eventSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ClubEvents
		fields = '__all__'

class Club_eventfavSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    club = Club_eventSerializer()
    class Meta:
        model = models.RelInterestClubs
        fields ='__all__'
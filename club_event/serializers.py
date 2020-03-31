from rest_framework import serializers
from common import models


class Club_eventSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ClubEvents
		fields = '__all__'

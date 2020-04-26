from rest_framework import serializers
from common import models

class Club_eventSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = models.ClubEvents
		fields = '__all__'
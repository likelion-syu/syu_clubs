from rest_framework import serializers
from common import models


class ClubSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = models.Clubs
		fields = '__all__'

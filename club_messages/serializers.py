from rest_framework import serializers
from common import models


class MessageSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = models.Messages
		fields = '__all__'

from rest_framework import serializers
from common.models import Messages


class MessageSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = Messages
		fields = '__all__'

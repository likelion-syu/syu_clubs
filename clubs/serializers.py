from rest_framework import serializers
from common import models


class ClubSerializer(serializers.ModelSerializer):
	club_img_url = serializers.ImageField(use_url=True)
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = models.Clubs
		fields = '__all__'
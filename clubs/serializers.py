from rest_framework import serializers
from . import models


class ClubSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Clubs
		fields = '__all__'
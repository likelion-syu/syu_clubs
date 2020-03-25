from rest_framework import serializers
from common import models


class Club_listSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Clubs
		fields = '__all__'

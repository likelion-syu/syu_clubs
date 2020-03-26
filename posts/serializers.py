from rest_framework import serializers
from common import models



class UserSerializer(serializers.ModelSerializer):
	username= serializers.ReadOnlyField()
	email=serializers.ReadOnlyField()
	class Meta:
		model = models.User
		fields = ["username", "email"]

class PostSerializer(serializers.ModelSerializer):
	post_title_img_url = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	user = UserSerializer()


	class Meta:
		model = models.Posts
		fields = '__all__'

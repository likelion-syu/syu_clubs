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
	user = serializers.ReadOnlyField(source='user.username')
	is_notice = serializers.IntegerField(write_only = True)
	is_deleted = serializers.IntegerField(write_only = True)
	
	# user = serializers.CharField(source='user.username')
	# user = UserSerializer()


	class Meta:
		model = models.Posts
		fields = '__all__'

from rest_framework import serializers
from common import models


class PostSerializer(serializers.ModelSerializer):
	post_title_img_url = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
<<<<<<< HEAD
	user = serializers.ReadOnlyField(source='user.username')
	is_notice = serializers.IntegerField(write_only = True)
	is_deleted = serializers.IntegerField(write_only = True)
	
=======
	# user = serializers.CharField(source='user.username')


>>>>>>> 9a03f7b97cc8aa93c3f0ba322dd0aab9032081a3
	class Meta:
		model = models.Posts
		fields = '__all__'
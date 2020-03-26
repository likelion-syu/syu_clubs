from rest_framework import serializers
from common import models


class PostSerializer(serializers.ModelSerializer):
	post_title_img_url = serializers.ImageField(use_url=True)
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	user = serializers.ReadOnlyField(source='user.username')
	is_notice = serializers.IntegerField(write_only = True)
	is_deleted = serializers.IntegerField(write_only = True)
	
	class Meta:
		model = models.Posts
		fields = '__all__'
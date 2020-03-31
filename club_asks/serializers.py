from common.models import Posts
from common import models
from rest_framework import serializers


class ClubAskSerializer(serializers.ModelSerializer):

    club_name = serializers.ReadOnlyField(source='club.club_name')
    user_name = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Posts
        fields = [
            'url',
            'category',
            'club_name',
            'user_name',
            'post_title',
            'post_content',
            'post_title_img_url',
            'created_at',
            'updated_at',
        ]


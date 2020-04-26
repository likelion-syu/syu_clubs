from rest_framework import serializers
from common import models

class Club_detailSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	club_type = serializers.ReadOnlyField( source = 'club_type.club_type_id' )
	club_events = serializers.ReadOnlyField ( source = 'ClubEvents.club_event_id' )
	Posts = serializers.ReadOnlyField( source = 'Posts.post_title')
	class Meta:
		model = models.Clubs
		fields = '__all__'
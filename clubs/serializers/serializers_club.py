from rest_framework import serializers
from common import models
class RelClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RelInterestClubs
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	club_type = serializers.ReadOnlyField( source = 'club_type.club_type_name' )
	club_events = serializers.ReadOnlyField ( source = 'ClubEvents.club_event_id' )
	Posts = serializers.ReadOnlyField( source = 'Posts.post_title')
	rel_clubs = RelClubSerializer(many=True)
	rel_count = serializers.SerializerMethodField()
	class Meta:
		model = models.Clubs
		fields = '__all__'
	def get_rel_count(self, obj):
		return obj.rel_clubs.count()
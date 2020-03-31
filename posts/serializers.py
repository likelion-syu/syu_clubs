from rest_framework import serializers
from common import models


class PostSerializer(serializers.ModelSerializer):
	#post_title_img_url = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	user = serializers.ReadOnlyField(source='user.username')
	is_notice = serializers.IntegerField(write_only = True)
	is_deleted = serializers.IntegerField(write_only = True)
	
	# user = serializers.CharField(source='user.username')
	class Meta:
		model = models.Posts
		fields = '__all__'
'''
class CommentSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	user = serializers.ReadOnlyField(source='user.username')
	is_deleted = serializers.IntegerField(write_only = True)
    class Meta:
        model = replies
        fields = '__all__'
'''
#
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    # reply = RecursiveSerializer(many=True, read_only=True)
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'product', 'parent', 'body', 'reply')
    
    def get_reply(self, instance):
    	# recursive
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data
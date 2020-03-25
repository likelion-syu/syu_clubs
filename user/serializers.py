from rest_framework import serializers
from common import models



class AuthUserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = ['date_joined', 'password', 'is_active', 'is_staff', 'is_superuser', 'username', 'email', 'last_login']

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
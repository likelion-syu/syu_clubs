from rest_framework import serializers
from common import models
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



class AuthUserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = ['date_joined', 'password', 'is_active', 'is_staff', 'is_superuser', 'username', 'email', 'last_login']
        extra_kwargs = {
        'password': {'write_only': True}
        }

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email']

class UserSerializer(serializers.ModelSerializer):
    user_info = InfoSerializer()
    class Meta:
        model = models.UsersAdditionalInfo
        fields = '__all__'

# class LoginUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ['id', 'username', 'email']
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
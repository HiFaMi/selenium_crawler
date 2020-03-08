from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'user_email',
            'like',
        )


class UserAuthSerializer(AuthTokenSerializer):

    def validate_username(self, value):
        if User.objects.filter(username=value).exists() is False:
            raise serializers.ValidationError("없는 사용자 입니다.")
        return value


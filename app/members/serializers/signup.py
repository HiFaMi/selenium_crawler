from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    password_check = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'user_email',
            'password',
            'password_check'
        )
        extra_kwargs = {'password': {'write_only': True}}

        def validate_username(self, value):
            if User.objects.filter(username=value).exists():
                return serializers.ValidationError("이미 있는 사용자 입니다.")
            return value

        def validate_password(self, value):
            if len(value) < 8:
                return serializers.ValidationError("비밀번호는 8자리 이상 가능 합니다.")

        def create(self, validated_data):

            if validated_data['password'] != validated_data['password_check']:
                return serializers.ValidationError("두 비밀번호가 같지 않습니다.")

            return validated_data

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ChangePasswordSerializer(serializers.ModelSerializer):

    check_password = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = (
            'password',
            'check_password'
        )

    def create(self, validated_data):

        if len(validated_data['password']) < 8:
            raise serializers.ValidationError("비밀번호는 8글자 이상이여야 합니다.")

        if validated_data['password'] != validated_data['password_check']:
            raise serializers.ValidationError("두 비밀번호가 같지 않습니다.")

        return validated_data

from rest_framework import serializers

from .models import PostPicture


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPicture
        fields = (
            'pk',
            'post_user',
            'post_picture',
            'post_likes'
        )

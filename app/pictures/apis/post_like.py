from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers.auth import UserSerializer
from pictures.models import PostPicture
from ..serializers import PostSerializer

User = get_user_model()


class PostLike(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = User.objects.get(pk=request.user.id)
        post = PostPicture.objects.get(pk=pk)

        if post.post_likes.filter(pk=user.id).exists():
            post.post_likes.remove(user)

        else:
            post.post_likes.add(user)

        # context = {
        #     'user': UserSerializer(user).data,
        #     'post': PostSerializer(post).data
        # }

        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)


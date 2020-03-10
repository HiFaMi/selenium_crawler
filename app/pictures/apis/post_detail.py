from rest_framework import generics, permissions

from pictures.models import PostPicture
from pictures.serializers import PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = PostPicture.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

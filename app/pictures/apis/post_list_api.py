from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from ..pagination_class import LargeResultsSetPagination, StandardResultsSetPagination
from ..serializers import PostSerializer
from ..models import PostPicture


class PostList(APIView):
    def get(self, request):
        post = PostPicture.objects.all()
        serializer = PostSerializer(post, many=True)

        return Response(serializer.data)


class PostListPagination(generics.ListAPIView):
    queryset = PostPicture.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

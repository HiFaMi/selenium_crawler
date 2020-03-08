from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from ..pagination_class import StandardResultsSetPagination, PaginationHandlerMixin
from ..serializers import PostSerializer
from ..models import PostPicture


class PostList(APIView, PaginationHandlerMixin):
    pagination_class = StandardResultsSetPagination
    serializer_class = PostSerializer

    def get(self, request, format=None, *args, **kwargs):
        post = PostPicture.objects.all()
        page = self.paginate_queryset(post)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)

        else:
            serializer = self.serializer_class(post, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListPagination(generics.ListAPIView):
    queryset = PostPicture.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

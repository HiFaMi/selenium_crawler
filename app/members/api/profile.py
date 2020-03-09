from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from ..serializers.auth import UserSerializer


class AuthProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)


class AuthProfileGeneric(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

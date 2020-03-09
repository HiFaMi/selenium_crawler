from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from ..serializers.auth import UserAuthSerializer, UserSerializer


class AuthToken(APIView):

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
            'user': UserSerializer(user).data
        }

        return Response(data)


class AuthTokenGeneric(generics.GenericAPIView):
    serializer_class = UserAuthSerializer

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'token-key': token.key,
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        }

        return Response(data)

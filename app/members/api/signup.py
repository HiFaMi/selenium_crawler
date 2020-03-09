from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.signup import SignupSerializer

User = get_user_model()


class ApiSignUp(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            User.objects.create_user(
                username=serializer.validated_data['username'],
                user_email=serializer.validated_data['user_email'],
                password=serializer.validated_data['password']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SignUpGeneric(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def get_object(self):
        return self.request.user
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from ..serializers.change_password import ChangePasswordSerializer
from ..serializers.auth import UserSerializer

User = get_user_model()


class ChangePassword(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = User.objects.get(pk=request.user.id)

        serializer = ChangePasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data['password'])
        user.save()

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

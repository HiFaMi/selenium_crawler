from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

User = get_user_model()


class AuthDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        token = Token.objects.get(user=request.user)
        user = User.objects.get(pk=request.user.pk)

        token.delete()
        user.delete()

        data = {
            'alter': "해당 user 삭제"
        }

        return Response(data, status=status.HTTP_204_NO_CONTENT)

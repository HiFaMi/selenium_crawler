from rest_framework import permissions, status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthLogout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        token = Token.objects.get(user=request.user)

        token.delete()

        data = {
            'alter': "로그아웃 되셨습니다."
        }

        return Response(data, status=status.HTTP_204_NO_CONTENT)



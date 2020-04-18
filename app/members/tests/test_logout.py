from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


class LogoutTest(TestCase):

    def test_logout(self):
        client = APIClient()
        User.objects.create_user(
            username='test',
            user_email='test@gmail.com',
            password='testpassword'
        )

        user = User.objects.first()

        token, _ = Token.objects.get_or_create(user=user)

        client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = client.post(reverse('members-api:api-logout'))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, {'alter': "로그아웃 되셨습니다."})

    def test_logout_fail(self):
        client = APIClient()

        response = client.post(reverse('members-api:api-logout'))

        self.assertEqual(response.status_code, 401)

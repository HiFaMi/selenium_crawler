from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from members.serializers.auth import UserAuthSerializer

User = get_user_model()


class LoginTest(TestCase):

    def test_login_api(self):
        User.objects.create_user(
            username='test',
            user_email='test@gmail.com',
            password='testpassword'
        )

        client = Client()

        response = client.post(reverse('members-api:api-login'),
                               data={
                                   'username': 'test',
                                   'password': 'testpassword'
                               })

        self.assertEqual(response.status_code, 200)

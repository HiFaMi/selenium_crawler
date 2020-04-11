from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from members.serializers.signup import SignupSerializer

User = get_user_model()

EXACT_DATA = {
    'username': 'test',
    'user_email': 'test_email@gmail.com',
    'password': 'testpassword',
    'password_check': 'testpassword'
}

FALSE_USERNAME_DATA = {
    'username': '',
    'user_email': 'test_email@gmail.com',
    'password': 'testpassword',
    'password_check': 'testpassword'
}

FALSE_USER_EMAIL_DATA = {
    'username': 'test',
    'user_email': 'test_emailgmail.com',
    'password': 'testpassword',
    'password_check': 'testpassword'
}

FALSE_PASSWORD_DATA = {
    'username': 'test',
    'user_email': 'test_email@gmail.com',
    'password': '',
    'password_check': 'testpassword'
}

FALSE_PASSWORD_CHECK_DATA = {
    'username': 'test',
    'user_email': 'test_email@gmail.com',
    'password': 'testpassword',
    'password_check': ''
}

FALSE_PASSWORD_AND_PASSWORD_CHECK_DATA = {
    'username': 'test',
    'user_email': 'test_email@gmail.com',
    'password': 'testpass',
    'password_check': 'testpassword'
}



class SignupTest(TestCase):

    def test_apiview_signup(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'), data=EXACT_DATA)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.last().username, 'test')
        self.assertEqual(User.objects.last().user_email, 'test_email@gmail.com')

    def test_apiview_signup_is_valid_username_fail(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'), data=FALSE_USERNAME_DATA)

        serializer = SignupSerializer(data=FALSE_USERNAME_DATA)

        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, 400)

    def test_apiview_signup_is_valid_user_email_fail(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'), data=FALSE_USER_EMAIL_DATA)

        serializer = SignupSerializer(data=FALSE_USER_EMAIL_DATA)

        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, 400)

    def test_apiview_signup_is_valid_password_fail(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'), data=FALSE_PASSWORD_DATA)

        serializer = SignupSerializer(data=FALSE_PASSWORD_DATA)

        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, 400)

    def test_apiview_signup_is_valid_password_check_fail(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'), data=FALSE_PASSWORD_CHECK_DATA)

        serializer = SignupSerializer(data=FALSE_PASSWORD_CHECK_DATA)

        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, 400)

    # def test_generics_signup(self):
    #     client = Client()
    #     response = client.post(reverse('members-api:api-signup-generic'), data=EXACT_DATA)
    #
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(User.objects.last().username, 'test')
    #     self.assertEqual(User.objects.last().user_email, 'test_email@gmail.com')


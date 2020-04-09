from django.test import TestCase, Client
from django.urls import reverse


class SignupTest(TestCase):

    def test_apiview_signup(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup'),
                               data={
                                   'username': 'test',
                                   'user_email': 'test_email@gmail.com',
                                   'password': 'testpassword',
                                   'password_check': 'testpassword'
                               })

        self.assertEqual(response.status_code, 201)

    def test_generics_signup(self):
        client = Client()
        response = client.post(reverse('members-api:api-signup-generic'),
                               data={
                                   'username': 'test',
                                   'user_email': 'test_email@gmail.com',
                                   'password': 'testpassword',
                                   'password_check': 'testpassword'
                               })
        self.assertEqual(response.status_code, 201)

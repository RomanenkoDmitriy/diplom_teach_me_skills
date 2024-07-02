from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from custom_user.models import CustomUser

from custom_user.forms import UserChangeForm

from importlib import import_module


class CustomUserTestCase(TestCase):
    def setUp(self):

        self.client = Client()
        self.user1 = CustomUser.objects.create_superuser(username='admin', password='q11111111', is_staff=True,
                                                         is_active=True)
        self.user2 = CustomUser.objects.create_user('user', '<EMAIL>', '<PASSWORD>', phone_number='123134234242423333',
                                                    address='test_adders')

        self.data_registration = {'username': 'test', 'password1': 'q11111111', 'password2': 'q11111111'}
        self.data_authentication = {'username': 'test', 'password': 'q11111111'}
        self.data_profile = {'email': 'test_email2@mail.ru', 'phone_number': '1231342342424238888888888'}

    def test_registration_user(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = self.client.post(reverse('registration'), data=self.data_registration)
        user = CustomUser.objects.filter(username=self.data_registration['username']).first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.username, self.data_registration['username'])

    def test_authentication_user(self):
        response_get = self.client.get(reverse('authenticate'))
        response_post = self.client.post(reverse('authenticate'), data=self.data_authentication)

        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_post.status_code, 200)  # ToDo

    def test_profile(self):
        self.client.force_login(self.user1)
        with (
            patch('custom_user.my_requests.get_request', return_value={'phone_numbers': ''}),
            patch('custom_user.my_requests.post_request',
                  return_value={'phone_numbers': '11111111111111111111'})):
            form = UserChangeForm
            form.email = self.data_profile['email']
            form.phone_number = self.data_profile['phone_number']
            response_get = self.client.get(reverse('profile'))
            response_post = self.client.post(reverse('profile'), data=self.data_profile)

            self.assertEqual(response_get.status_code, 200)
            self.assertEqual(response_post.status_code, 302)
            # self.assertEqual(self.user1.email, self.data_profile['email'])
            # self.assertEqual(self.user1.phone_number, self.data_profile['phone_number'])

from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client


class TestProfileView(TestCase):
    """
    Test profile views

    1. Set up the scenario
    2. Test update profile functionality
    3. Test delete profile functionality

    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin', 'admin@email.com', 'adminpass')

    def test_update_profile(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/profile/', data={'full_name': 'test update name', 'bio': 'test update bio'})
        self.assertEqual(response.status_code, 200)

    def test_delete_profile(self):
        self.client.login(username='admin', password='adminpass')
        user_to_delete = User.objects.get(username='admin')
        response = self.client.get(f'/profile/delete_profile/{user_to_delete}')
        self.assertRedirects(response, '/')

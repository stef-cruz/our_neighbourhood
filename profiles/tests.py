from django.contrib.auth import get_user_model
from django.test import TestCase



class TestProfileView(TestCase):
    """
    Test profile views - Happy path

    def profile
    1. Set up the scenario
    2. Check update profile functionality
    3. Assert

    def delete_profile
    Using the same scenario:
    1. Check delete profile functionality
    2. Assert

    """

    @classmethod
    def setUp(self):
        super().setUpClass()
        username = 'testuser'
        password = 'testpass'

        User = get_user_model()
        self.user = User.objects.create_user(username, password=password)

        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_update_profile(self):
        # Update profile
        self.response = self.client.post('/profile/', data= {'full_name': '', 'bio': 'test update bio'})
        print(self.response)
        # Assert response 200
        self.assertEqual(self.response.status_code, 200)


    def test_delete_profile(self):
        # Delete profile
        self.response = self.client.get('/profile/delete_profile/')

        # Assert it was deleted
        self.assertEqual(self.response.status_code, 404)


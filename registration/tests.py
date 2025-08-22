from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpass')

    def test_profile_creation_on_user_creation(self):
        # Ensure that a profile is created when a user is created
        profile = Profile.objects.get(user=self.user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, self.user)

    def test_profile_exists(self):
        # Ensure that the profile exists after user creation
        exists = Profile.objects.filter(user=self.user).exists()
        print(f"Profile exists for user: {self.user.username}")
        self.assertTrue(exists)

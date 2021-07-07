from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_email_successfull(self):
        """Test create user email successfull"""
        email = "chiencool334@gmail.com"
        password = "TestCase123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test create user email is normalized"""
        email = "chiencool334@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'tesst123456')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test create user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'tesst123456')

    def test_create_new_superuser(self):
        """Test create superuser with email"""
        email = "chien334@gmail.com"
        user = get_user_model().objects.create_superuser(
            email,
            'chien334'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

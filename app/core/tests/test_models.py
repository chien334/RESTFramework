from typing import ClassVar
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_email_successfull(sefl):
        """Test create user email successfull"""
        email = "chiencool334@gmail.com"
        password ="TestCase123"
        user=get_user_model().objects.create(email=email,password=password)
        sefl.assertEqual(user.email, email)
        sefl.assertTrue(user.check_password(password))
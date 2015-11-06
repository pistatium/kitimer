# coding: utf-8

from django.test import TestCase

from .models import User


class UserTest(TestCase):
    def test_create_user(self):
        user = User()
        user.name = "テスト"  # multibyte characters
        user.slack_name = "hoge"
        user.icon_url = "http://example.com/img.jpg"
        user.save()

        saved = User.objects.all()
        self.assertEqual(len(saved), 1)
        saved_user = saved[0]
        self.assertEqual(saved_user.name, "テスト")
        self.assertEqual(saved_user.slack_name, "hoge")
        self.assertEqual(saved_user.icon_url, "http://example.com/img.jpg")
        self.assertTrue(saved_user.access_key)

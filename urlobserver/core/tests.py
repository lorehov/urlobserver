"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class MainTest(TestCase):

    def test_url_add(self):
        pass

    def test_check_urls(self):
        pass

    def test_subscriber_add(self):
        pass

    def test_subscriber_suspend(self):
        pass

    def test_subscriber_activate(self):
        pass

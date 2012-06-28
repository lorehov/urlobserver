"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from urlobserver.core.models import Worker
from urlobserver.core.utils import make_request


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class MainTest(TestCase):

    def test_subscription_add(self):
        pass

    def test_urls_check(self):
        pass

    def test_subscriber_suspend(self):
        pass

    def test_subscriber_activate(self):
        pass

    def test_url_update_failed(self):
        pass

class UtilsTest(TestCase):
    """
    Install tinyproxy locally for this kind of test and
    make sure remote service http://statuscoder.com/ is available
    """

    def setUp(self):
        self.worker = Worker.objects.create(domain_name='localhost',
                                            instance_id='1234')

    def test_make_request(self):
        resp = make_request(self.worker, 'http://statuscoder.com/200')
        self.assertEqual(resp, {'content': '', 'status_code': 200, 'instance_id': '1234'})
        resp = make_request(self.worker, 'http://statuscoder.com/403')
        self.assertEqual(resp, {'content': '', 'status_code': 403, 'instance_id': '1234'})

    def tearDown(self):
        self.worker.delete()

# -*- coding: utf-8 -*-
from django.test import TestCase
from django.conf import settings
from urlobserver.ec2_management.utils import get_user_data



class UtilsTest(TestCase):

    def test_get_uerdata(self):
        user_data = get_user_data()
        self.assertTrue(user_data.startswith('#!/bin/bash\n'))
        self.assertTrue(settings.EC2_SSH_PUBLIC_KEYS[0] in user_data)
        self.assertTrue(settings.EC2_ALLOWED_IPS[0] in user_data)

# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.test import TestCase
from currencies.models import RateSource


class RateSourceModelTestCase(TestCase):
    def test_instance_default_values(self):
        instance = RateSource()
        self.assertIsNone(instance.last_poll)
        self.assertIsNone(instance.remote_ts)

        self.assertRaises(ValidationError, instance.save)

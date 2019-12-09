# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.test import TestCase
from currencies.models import RateSource
from django.db import IntegrityError


class RateSourceModelTestCase(TestCase):
    def test_default_values(self):
        instance = RateSource()
        self.assertIsNone(instance.last_poll)
        self.assertIsNone(instance.remote_ts)

    def test_empty_constraint(self):
        instance = RateSource()
        self.assertRaises(IntegrityError, instance.save)

    def test_unique_constraint(self):
        x = RateSource(abbr='ABC')
        y = RateSource(abbr='ABC')

        x.save()
        self.assertRaises(IntegrityError, y.save)

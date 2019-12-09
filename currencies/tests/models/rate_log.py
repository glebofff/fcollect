# -*- coding: utf-8 -*-
from django.test import TestCase

from currencies.common import CurrencyCode
from currencies.models import RateLog, RateSource
from django.db import IntegrityError


class RateLogModelTestCase(TestCase):
    def test_default_values(self):
        log = RateLog()
        self.assertIsNone(log.ts)
        self.assertEqual(log.base, CurrencyCode.USD)

    def test_negative_constraint(self):
        log = RateLog()
        self.assertRaises(IntegrityError, log.save)

    def test_source_not_null_constraint(self):
        log = RateLog(rate=1)
        self.assertRaises(IntegrityError, log.save)

    def test_unique_constraint(self):
        from datetime import datetime
        import pytz

        src = RateSource(abbr='TEST')
        src.save()

        ts = datetime.now().astimezone(pytz.UTC)
        l1 = RateLog(code=CurrencyCode.CZK, rate=0.1, ts=ts, source=src)
        l2 = RateLog(code=CurrencyCode.CZK, rate=0.2, ts=ts, source=src)
        l1.save()
        self.assertRaises(IntegrityError, l2.save)

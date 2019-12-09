# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
from django.db import models

from currencies.common.code import CurrencyCode
from .source import RateSource


class RateLog(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['source', 'ts', 'base', 'code'], name='rate_log_unique_cst'),
            models.CheckConstraint(check=~models.Q(rate__lte=0), name="rate_log_negative_or_zero_rate_cst")
        ]
    source = models.ForeignKey(RateSource, on_delete=models.CASCADE)
    ts = models.DateTimeField(db_index=True)
    base = models.CharField(max_length=3, choices=CurrencyCode.choices, db_index=True, default=CurrencyCode.USD)
    code = models.CharField(max_length=3, choices=CurrencyCode.choices, db_index=True)
    rate = models.DecimalField(max_digits=12, decimal_places=3, default=0)

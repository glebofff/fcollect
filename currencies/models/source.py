# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
from django.core.validators import MinLengthValidator
from django.db import models


class RateSource(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['abbr'], name='rate_source_unique_abbr_cst'),
            models.CheckConstraint(check=~models.Q(abbr=""), name="rate_source_not_empty_abbr_cst")
        ]

    abbr = models.CharField(max_length=64, db_index=True, validators=[MinLengthValidator(1)])
    last_poll = models.DateTimeField(auto_now_add=False, null=True)
    remote_ts = models.DateTimeField(auto_now_add=False, null=True)

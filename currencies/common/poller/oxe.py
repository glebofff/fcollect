# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
from currencies.common.poller import FetchException, ParseException
from .base import BasePoller
from django.conf import settings


class OpenExchangePoller(BasePoller):
    abbr = 'OXE'
    description = 'Open Exchange'
    url = 'https://openexchangerates.org/api/latest.json'
    api_key: str = getattr(settings, 'OXE_APP_ID', '')
    symbols: list = getattr(settings, 'OXE_SYMBOLS', None) or []
    _response = None

    def get_params(self):
        res =  {
            'app_id': self.api_key
        }
        if isinstance(self.symbols, list) and self.symbols:
            res['symbols'] = ','.join(self.symbols)

        return res




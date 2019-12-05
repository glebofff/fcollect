# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
import datetime
import pytz
from typing import Optional

from currencies.common.code import CurrencyCode
from currencies.models import RateSource

from .exceptions import AlreadyPolledException

_registry = {}


class MetaPoller(type):
    def __new__(cls, name, bases, attrs):

        res = super().__new__(cls, name, bases, attrs)
        if 'abbr' in attrs and attrs['abbr']:
            _registry[attrs['abbr']] = res

        return res


class BasePoller(object, metaclass=MetaPoller):
    abbr: str = ''
    description: str = ''
    url: str = ''
    api_key: str = ''
    api_pass: str = ''
    base: str = CurrencyCode.USD

    poll_period: datetime.timedelta = datetime.timedelta(days=1)
    last_poll: datetime.datetime = None

    def __init__(self,  url: str = ''):
        self.url = url or self.url
        self.now = datetime.datetime.now().astimezone(pytz.UTC)

        try:
            self.src = RateSource.objects.get(abbr=self.abbr)
        except RateSource.DoesNotExist:
            self.src = RateSource.objects.create(
                abbr=self.abbr,
                last_poll=None
            )

        self.last_poll = self.src.last_poll

    def get_params(self) -> Optional[dict]:
        return None

    def get_url(self) -> str:
        import urllib.parse
        params = self.get_params()

        if not isinstance(params, dict):
            return self.url
        url = self.url
        decoded = urllib.parse.urlencode(params)
        return f'{url}?{decoded}'

    def fetch(self):
        pass

    def parse(self):
        pass

    def populate_db(self, parsed: dict = None):
        if not isinstance(parsed, dict):
            return None

        from currencies.models import RateLog
        ts = datetime.datetime.fromtimestamp(parsed['timestamp']) or self.now

        RateLog.objects.bulk_create(
            [
                RateLog(
                    source=self.src,
                    base=self.base,
                    ts=ts,
                    code=code,
                    rate=rate
                )
                for code, rate in parsed['rates'].items()
            ]
        )

    def poll(self, force: bool = False):
        if all(
                [
                    self.last_poll,
                    self.now <= self.last_poll + self.poll_period,
                    not force
                ]
        ):
            raise AlreadyPolledException

        self.fetch()

        self.populate_db(
            self.parse()
        )

        self.last_poll = self.now
        self.src.last_poll = self.last_poll
        self.src.save()

# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
import datetime
import pytz
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from typing import Optional

from currencies.common.code import CurrencyCode
from currencies.models import RateSource

from .exceptions import AlreadyPolledException, ParseException, FetchException, PollerException

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

    def __init__(self,  url: str = None, abbr: str = None,
                 api_key: str = None, api_pass: str = None,
                 base: str = '', ts: datetime.datetime = None):

        self.url = url if url is not None else self.url
        self.abbr = abbr if abbr is not None else self.abbr
        self.api_key = api_key if api_key is not None else self.api_key
        self.api_pass = api_pass if api_pass is not None else self.api_pass
        self.base = base or self.base

        url_validator = URLValidator()
        try:
            url_validator(self.url)
        except ValidationError:
            raise PollerException('Invalid URL')

        if not CurrencyCode.is_valid(self.base):
            raise PollerException(f'Invalid Currency Code: {self.base}')

        self.now = ts if isinstance(ts, datetime.datetime) else datetime.datetime.now()
        self.now = self.now.astimezone(pytz.UTC)

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

    def fetch(self, force: bool=False) -> str:
        """
        Fetches data from url.
        """
        from urllib.request import urlopen
        from urllib.error import URLError

        try:
            with urlopen(self.get_url()) as response:
                return response.read()

        except URLError as e:
            raise FetchException(f'{e}')

    def parse(self, content) -> dict:
        """
        Parses and validates data returned by self.fetch
        """
        import json
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            raise ParseException('Invalid response')

        if set(data) < {'timestamp', 'base', 'rates'}:
            raise ParseException('Invalid payload')

        return {
            'timestamp': data['timestamp'],
            'base': data['base'],
            'rates': data['rates']
        }

    def populate_db(self, parsed: dict = None, ts: datetime.datetime = None):
        if not isinstance(parsed, dict):
            return None

        from currencies.models import RateLog

        RateLog.objects.bulk_create(
            [
                RateLog(
                    source=self.src,
                    base=self.base,
                    ts=ts or self.now,
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
                    self.last_poll and self.now <= self.last_poll + self.poll_period,
                    not force
                ]
        ):
            raise AlreadyPolledException

        parsed = self.parse(
            self.fetch()
        )

        if parsed['timestamp']:
            ts = datetime.datetime.fromtimestamp(parsed['timestamp']).astimezone(pytz.UTC)
            if not self.src.remote_ts or ts > self.src.remote_ts or force:
                self.populate_db(parsed=parsed)
        else:
            ts = None
            self.populate_db(parsed=parsed)

        self.last_poll = self.now
        self.src.last_poll = self.last_poll
        self.src.remote_ts = ts
        self.src.save()


def get_poller(abbr=None, **kwargs) -> Optional[BasePoller]:
    cls = _registry.get(abbr)
    if isinstance(cls, MetaPoller):
        return cls(**kwargs)
    return None


def list_pollers():
    return _registry.keys()

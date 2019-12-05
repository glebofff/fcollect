# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
from django.core.management import BaseCommand

from currencies.common import get_poller, list_pollers
from currencies.common.poller import PollerException


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--sources',
            type=list,
            default=list(list_pollers())
        )

        parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            default=False
        )

    def poll(self, abbr=None, **options):
        poller = get_poller(abbr)
        force = options['force']
        if poller is None:
            self.stderr.write(
                f'Invalid source {abbr}'
            )
            return

        try:
            self.stdout.write(f'Updating {abbr}, force: {force}')
            poller.poll(force=options['force'])

        except PollerException as e:
            msg = f'{e}' or f'{e.__class__.__name__}'
            self.stderr.write(msg)

    def handle(self, *args, **options):
        for abbr in options['sources']:
            self.poll(abbr=abbr, **options)


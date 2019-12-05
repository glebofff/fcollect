# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19


class PollerException(Exception):
    pass


class AlreadyPolledException(PollerException):
    pass


class FetchException(PollerException):
    pass


class ParseException(PollerException):
    pass

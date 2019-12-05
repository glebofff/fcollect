# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19
from django.utils.decorators import classproperty


class StrEnum(object):
    __descriptions__ = {}

    @classmethod
    def description(cls, cur):
        return cls.__descriptions__.get(cur)

    @classproperty
    def choices(cls):
        return tuple((k, v) for k, v in cls.__descriptions__.items())

    @classmethod
    def is_valid(cls, key):
        return key in cls.__descriptions__

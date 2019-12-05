# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19

import decimal, re


def to_fixed(v, digits=5):
    try:
        v_ = float(v)
    except ValueError:
        v_ = 0

    return '{v:.{digits}f}'.format(v=v_, digits=digits)


def to_decimal(v, digits=5, skip_bad_chars=False):
    try:
        if not v:
            return decimal.Decimal('0.0')

        if isinstance(v, str) and skip_bad_chars:
            v = re.sub('[^-+.0-9]', '', v)

        return decimal.Decimal(to_fixed(v, digits))

    except:
        return decimal.Decimal('0.0')

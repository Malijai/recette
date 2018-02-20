from __future__ import unicode_literals
from django import template
from django.apps import apps
import re

register = template.Library()


@register.filter
def int_format(value):
    value = str(value)
    m = re.search('\.',value)
    n = re.search(',',value)
    if m or n:
        entier, decimale = value .split('.')
        entier2, decimale2 = value .split(',')
        if decimale == '00':
            return entier
        elif decimale2 == '00':
            return entier2
        else:
            return value
    else:
        return value

from __future__ import unicode_literals
from django import template
from django.apps import apps
import re

register = template.Library()


@register.filter
def int_format(value):
    value = str(value)
    m = re.search('\.',value)
    if m:
        entier, decimale = value .split('.')
        if decimale == '00':
            return entier
        else:
            return value
    else:
        return value

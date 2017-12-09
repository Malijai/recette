from __future__ import unicode_literals
from django import template
from django.apps import apps

register = template.Library()


@register.simple_tag
def int_format(value):
    value = str(value)
    entier, decimale = value .split(',')
    if decimale == '00':
        return entier
    else:
        return value

from django import template
from django.utils.timesince import timesince
from datetime import datetime

register = template.Library()

@register.filter(name='time_ago')
def time_ago(value):
    now = datetime.now()
    return timesince(value, now, depth=1)
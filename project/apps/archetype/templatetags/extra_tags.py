from django import template
from datetime import datetime

register = template.Library()


@register.filter
def timestamp_to_date(value):
    try:
        return datetime.fromtimestamp(value)
    except AttributeError:
        return None
